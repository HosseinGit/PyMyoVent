---
Title: Getting Started
nav_order: 1
has_children: False
parent: Demos
---
# Getting Started
{:.no_toc}

* TOC
{:toc}
## Instruction

* Lunch [Anaconda](http://anaconda.org) prompt. 

* Navigate to **Python_code** folder in PyMyoVent's repository directory:
    * `$ cd path_to_PyMyoVent_repo\Python_code`

* Use the following command to run the `Getting_started` demo.
    * `$ python PyMyoVent.py run_default_model`
    * After a few seconds you should see this:
    ![prompt_line](getting_started_prompt.png) 

## Instruction file
* The instruction file is written in [JSON format](http://en.wikipedia.org/wiki/JSON#:~:text=JavaScript%20Object%20Notation%20(JSON%2C%20pronounced,or%20any%20other%20serializable%20value).) and is located at `path_to_PyMyoVent_repo\demo_files\getting_started\getting_started_model.json`.

````
{
  "output_parameters": {
    "excel_file": ["..\\temp\\getting_started\\getting_started.xlsx"],
    "csv_file": ["..\\temp\\getting_started\\getting_started.csv"],
    "input_file": ["..\\temp\\getting_started\\getting_started.json"],
    "summary_figure": ["..\\temp\\getting_started\\getting_started_summary.png"],
    "pv_figure": ["..\\temp\\getting_started\\getting_started_pv.png"],
    "baro_figure": ["..\\temp\\getting_started\\getting_started_baro.png"],
    "flows_figure": ["..\\temp\\getting_started\\getting_started_flows.png"],
    "hs_fluxes_figure": ["..\\temp\\getting_started\\getting_started_hs_fluxes.png"],
    "multi_threading":["..\\temp\\getting_started\\getting_started_multi_thread.png"]
  },
  "baroreflex": {
    "baro_scheme": ["fixed_heart_rate"],
    "fixed_heart_rate":{
      "simulation":{
        "no_of_time_points": [10000],
        "time_step": [0.001],
        "duty_ratio": [0.3],
        "basal_heart_period": [1,"s"]
      }
    },
    "simple_baroreceptor":{
      "simulation":{
        "start_index":[2000],
        "memory":[2,"s"],
        "no_of_time_points": [150000],
        "time_step": [0.001],
        "duty_ratio": [0.003],
        "basal_heart_period": [1,"s"]
      },
      "afferent": {
        "b_max": [2],
        "b_min": [0],
        "S": [0.067,"mmHg"],
        "P_n": [90,"mmHg"]
      },
      "regulation":{
        "heart_period":{
          "G_T": [0.03]
        },
        "k_1":{
          "G_k1": [-0.05]
        },
        "k_on":{
          "G_k_on":[0.02]
        },
        "ca_uptake":{
          "G_up": [-0.02]
        },
        "g_cal":{
          "G_gcal": [-0.03]
        }
      }
    }
  },
  "perturbations": {
    "perturbation_activation":[false],
    "volume":{
      "start_index": [],
      "stop_index": [],
      "increment": [0]
    },
    "valve":{
      "aortic":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      },
      "mitral":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      }
    },
    "compliance": {
      "aorta":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      },
      "capillaries": {
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      },
      "venous":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      }
    },
    "resistance": {
      "aorta":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      },
      "capillaries": {
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      },
      "venous":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      },
      "ventricle":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      }
    },
    "myosim":{
      "k_1":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      },
      "k_2":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      },
      "k_4_0":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      }
    },
    "ca_handling":{
      "ca_uptake":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      },
      "ca_leak":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      },
      "g_cal":{
        "start_index": [],
        "stop_index": [],
        "increment": [0]
      }
    }
  },
  "circulation":{
    "no_of_compartments": [6],
    "blood":{
      "volume":[5,"liters"]
    },
    "aorta":{
      "resistance": [40,"s"],
      "compliance": [0.0005,"liter_per_mmHg"]
    },
    "arteries":{
      "resistance": [20,"s"],
      "compliance": [0.0011,"liter_per_mmHg"]
    },
    "arterioles":{
      "resistance": [520,"s"],
      "compliance": [0.005,"liter_per_mmHg"]
    },
    "capillaries":{
      "resistance": [310,"s"],
      "compliance": [0.03,"liter_per_mmHg"]
    },
    "veins":{
      "resistance": [300,"s"],
      "compliance": [0.5,"liter_per_mmHg"]
    },
    "ventricle":{
      "resistance": [10,"s"],
      "wall_volume": [0.1,"liters"],
      "slack_volume": [0.08,"liters"],
      "wall_density": [1055,"g/l"],
      "body_surface_area": [1.90,"m^2"]
    }
  },
  "half_sarcomere":{
    "max_rate": [5000,"s^-1"],
    "temperature": [288, "Kelvin"],
    "cb_number_density": [6.9e16, "number of cb's/m^2"],
    "initial_hs_length": [900, "nm"],
    "ATPase_activation":[false],
    "delta_energy":[70,"kJ/mol"],
    "avagadro_number":[6.02e23,"mol^-1"],
    "reference_hs_length":[1100,"nm"],

    "myofilaments":{
      "kinetic_scheme": ["3state_with_SRX"],
      "k_1": [1.75,"s^-1"],
      "k_force": [1e-3, "(N^-1)(m^2)"],
      "k_2": [200, "s^-1"],
      "k_3": [100, "(nm^-1)(s^-1)"],
      "k_4_0": [200, "s^-1"],
      "k_4_1": [0.5, "nm^-4"],
      "k_cb": [0.001, "N*m^-1"],
      "x_ps": [5, "nm"],
      "k_on": [1e8, "(M^-1)(s^-1)"],
      "k_off": [200, "s^-1"],
      "k_coop": [5],
      "bin_min": [-10, "nm"],
      "bin_max": [10, "nm"],
      "bin_width": [1, "nm"],
      "filament_compliance_factor": [0.5],
      "thick_filament_length": [815, "nm"],
      "thin_filament_length": [1120, "nm"],
      "bare_zone_length": [80, "nm"],
      "k_falloff": [0.0024],
      "passive_mode": ["exponential"],
      "passive_exp_sigma": [500],
      "passive_exp_L": [80],
      "passive_l_slack": [900, "nm"]
    },
    "membranes": {
      "kinetic_scheme": ["simple_2_compartment"],
      "simple_2_compartment":{
        "Ca_content": [1e-3],
        "k_leak": [2e-3],
        "k_act": [5e-2],
        "k_serca": [10.0]
      },
      "Ten_Tusscher_2004":{
        "g_to_factor": [1],
        "g_Kr_factor": [1],
        "g_Ks_factor": [1],
        "Ca_a_rel_factor": [1],
        "Ca_V_leak_factor": [1],
        "Ca_Vmax_up_factor": [1],
        "g_CaL_factor": [1]
    }
  }
},
  "growth": {
    "growth_activation": [false],
    "start_index": [200000],
    "moving_average_window": [5000],
    "driven_signal": ["stress"],
    "concenrtric":{
      "G_stress_driven":[1e-6],
      "G_ATPase_driven":[-2]
    },
    "eccentric":{
      "G_number_of_hs":[-3e-6],
      "G_ATPase_driven":[0]
    }
  },
  "profiling":{
    "profiling_activation":[false]
  },
  "saving_to_spreadsheet":{
    "saving_data_activation":[false],
    "output_data_format":["csv"],
    "start_index":[0],
    "stop_index":[15000]
  },
  "multi_threads" :{
    "multithreading_activation":[false],
    "parameters_in":{
      "G_wall_thickness": {
        "values":[25,50,100,200,300],
        "param_out":["ventricle_wall_thickness"],
        "section": ["growth"]
      },
      "G_number_of_hs": {
        "values":[25,50,100,200,300],
        "param_out":["number_of_hs"],
        "section": ["growth"]
      }
    },
    "output_main_folder": ["..\\temp\\getting_started\\demo_i_j\\demo_i_j.json"]
  }
}


````

## Outputs

When the simulation is funished up, this set of output figures will be shown up in `path_to_PyMyoVent_repo\temp\getting_started` directory.

* Simmulation summary output

![summary](getting_started_summary.png)


* PV loop output

![PV](getting_started_pv.png)

* Fluxes output 
![Fluxes](getting_started_hs_fluxes.png)

* Blood flows output 

![Flows](getting_started_flows.png)

