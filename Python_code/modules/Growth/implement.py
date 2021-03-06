import numpy as np
from math import *
from scipy.integrate import solve_ivp
import pandas as pd

def update_growth(self,time_step):
    self.wall_volume = return_lv_wall_volume(self,time_step)
#    self.wall_thickness = return_lv_wall_thickness(self,time_step)
    self.number_of_hs = return_number_of_hs(self,time_step)

# stress driven growth


def return_lv_wall_volume(self,time_step,cb_force):
    f = cb_force#self.syscon.mean_active_force
    f_null = self.cb_force_null#self.cb_stress_null

    #window = self.ma_window
    """wv_0 = self.wall_volume
    dwvdt_0 = self.G_wv*(f-f_null)*self.wall_volume
    wv = dwvdt_0*time_step+wv_0"""

    wv_0 = self.wall_volume
    self.wv_rate = np.roll(self.wv_rate,-1)
    dwvdt_0 = self.G_wv*self.wall_volume*(f-f_null)
    self.wv_rate[-1] = dwvdt_0
    dwvdt = np.mean(self.wv_rate)
    wv = dwvdt*time_step+wv_0

    self.wall_volume = wv
    return self.wall_volume

def return_number_of_hs(self,time_step,pas_force):
    p = pas_force #self.syscon.mean_passive_force #
    p_null = self.pas_force_null#self.passive_stress_null

    """n_1 = self.n_of_hs
    dndt_0 = self.G_n_hs * self.n_of_hs* (p - p_null)
    n=dndt_0*time_step+n_1"""

    n_1 = self.n_of_hs
    self.n_hs_rate = np.roll(self.n_hs_rate,-1 )
    dndt_0 = self.G_n_hs * self.n_of_hs* (p - p_null)
    self.n_hs_rate[-1] = dndt_0
    dndt = np.mean(self.n_hs_rate)
    n=dndt*time_step+n_1

    self.n_of_hs = n

    if self.n_of_hs<=self.min_n_hs:
        print('too less')
    if self.n_of_hs>=self.max_n_hs:
        print('n_hs',self.n_of_hs)

    return self.n_of_hs


def return_lv_wall_thickness(self,time_step):

    if self.growth["driven_signal"][0] == "stress":

        f = self.hs.myof.cb_force
        f_null = self.cb_stress_null
#        window_null = int(self.start_index)
#        self.cb_array = np.append(self.cb_array,f)
#        f_null =np.mean(self.cb_array)
#        self.cb_stress_null = f_null

#        window = self.ma_window

        tw_1 = self.tw
        self.tw_rate = np.roll(self.tw_rate,-1)
        dwdt_0 = self.G_tw*(f-f_null)*self.tw
        self.tw_rate[-1] = dwdt_0
        dwdt=np.mean(self.tw_rate)
        tw = dwdt*time_step+tw_1
        self.tw = tw

        if self.tw <= self.min_tw:
            self.tw = self.min_tw

    if self.growth["driven_signal"][0] == "ATPase":

        """A = self.hs.ATPase
        self.ATPase_array = np.append(self.ATPase_array,A)
        A_null = np.mean(self.ATPase_array)
        self.ATPase_null = A_null

        window = self.ma_window

        tw_1 = self.tw
        dwdt_0 = self.G_tw*(A-A_null)*self.tw
        self.tw_rate = np.append(self.tw_rate,dwdt_0)
        dwdt = np.mean(self.tw_rate[-window:])
        tw = dwdt*time_step+tw_1
        self.tw = tw"""

        self.ATPase_array = np.append(self.ATPase_array,self.hs.ATPase)
        self.ATPase_null = np.mean(self.ATPase_array)
        dwdt_0 = self.G_tw*(self.hs.ATPase-self.ATPase_null)*self.tw
        self.tw_rate = np.append(self.tw_rate,dwdt_0)
        dwdt = np.mean(self.tw_rate[-self.ma_window:])
        self.tw = dwdt*time_step + self.tw

    return self.tw


def update_data_holder(self,time_step):

    self.gr_time = self.gr_time + time_step
    self.data_buffer_index += 1
    self.gr_data['pas_force_null'] = \
        pd.Series(np.full(self.data_buffer_size,self.pas_force_null))
    if self.growth["driven_signal"][0] == "stress":

        self.gr_data['cb_force_null'] = \
            pd.Series(np.full(self.data_buffer_size,self.cb_force_null))
    if self.growth["driven_signal"][0] == "ATPase":
        self.gr_data.at[self.data_buffer_index,'ATPase_null'] = self.ATPase_null
    # 1000 is to convert liter to mili liter
#    self.gr_data.at[self.data_buffer_index, 'ventricle_wall_thickness'] = self.wall_thickness
    self.gr_data.at[self.data_buffer_index, 'ventricle_wall_volume'] = self.wall_volume
    self.gr_data.at[self.data_buffer_index, 'number_of_hs'] = self.n_of_hs
