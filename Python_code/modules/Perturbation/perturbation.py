import numpy as np
import pandas as pd

class perturbation():
    #from implement import xx

    def __init__(self,pert_params,data_buffer_size):

        pert = pert_params
        #volume perturbation
        self.volume_perturbation = np.zeros(data_buffer_size+1)
        #aortic compliance perturbation
        self.aorta_compliance_perturbation=\
        np.zeros(data_buffer_size+1)
        #capillaries compliance perturbation
        self.capillaries_compliance_perturbation=\
        np.zeros(data_buffer_size+1)
        #venous compliance perturbation
        self.venous_compliance_perturbation =\
        np.zeros(data_buffer_size+1)
        #aortic resistance perturbation
        self.aorta_resistance_perturbation=\
        np.zeros(data_buffer_size+1)
        #capillaries resistance perturbation
        self.capillaries_resistance_perturbation=\
        np.zeros(data_buffer_size+1)
        #venous resistance perturbation
        self.venous_resistance_perturbation =\
        np.zeros(data_buffer_size+1)
        #ventricle resistance perturbation
        self.ventricle_resistance_perturbation =\
        np.zeros(data_buffer_size+1)

        #blood volume

        temp_vol=pert["volume"]
        start_index = int(temp_vol["start_index"][0])
        stop_index = int(temp_vol["stop_index"][0])
        increment = float(temp_vol["increment"][0])
        self.volume_perturbation[(start_index+1):(stop_index+1)] = increment
        #compliance
        temp_c = pert["compliance"]

        temp_ac = temp_c['aorta']
        start_index = int(temp_ac["start_index"][0])
        stop_index = int(temp_ac["stop_index"][0])
        increment = float(temp_ac["increment"][0])
        self.aorta_compliance_perturbation[(start_index+1):(stop_index+1)]=\
                            increment
        temp_cc = temp_c['capillaries']
        start_index = int(temp_cc["start_index"][0])
        stop_index = int(temp_cc["stop_index"][0])
        increment = float(temp_cc["increment"][0])
        self.capillaries_compliance_perturbation[(start_index+1):(stop_index+1)]=\
                    increment
        temp_vc = temp_c['venous']
        start_index = int(temp_vc["start_index"][0])
        stop_index = int(temp_vc["stop_index"][0])
        increment = float(temp_vc["increment"][0])
        self.venous_compliance_perturbation[(start_index+1):(stop_index+1)]=\
                    increment
        #resistance
        temp_r = pert["resistance"]

        temp_ar = temp_r['aorta']
        start_index = int(temp_ar["start_index"][0])
        stop_index = int(temp_ar["stop_index"][0])
        increment = float(temp_ar["increment"][0])
        self.aorta_resistance_perturbation[(start_index+1):(stop_index+1)]=\
        increment

        temp_cr = temp_r['capillaries']
        start_index = int(temp_cr["start_index"][0])
        stop_index = int(temp_cr["stop_index"][0])
        increment = float(temp_cr["increment"][0])
        self.capillaries_resistance_perturbation[(start_index+1):(stop_index+1)]=\
        increment

        temp_vr = temp_r['venous']
        start_index = int(temp_vr["start_index"][0])
        stop_index = int(temp_vr["stop_index"][0])
        increment = float(temp_vr["increment"][0])
        self.venous_resistance_perturbation[(start_index+1):(stop_index+1)]=\
        increment

        temp_vtr = temp_r['ventricle']
        start_index = int(temp_vtr["start_index"][0])
        stop_index = int(temp_vtr["stop_index"][0])
        increment = float(temp_vtr["increment"][0])
        self.ventricle_resistance_perturbation[(start_index+1):(stop_index+1)]=\
        increment