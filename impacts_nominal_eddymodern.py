import numpy as np
from threadpoolctl import threadpool_limits
from pathos.multiprocessing import ProcessingPool as Pool

from coupling import impact_evolve, cons

def nominal(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 10.0**23.0
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/evolution/imp_23_00"
    params['eddy'] = "ModernEarth"
    params['RH'] = 1.0
    params['P_top'] = 1.0e-1
    params['T_trop'] = 200
    params['T_guess'] = 400
    params['zero_out'] = ['NH3']
    params['nz'] = 100
    params['rainfall_rate'] = 1

    params['P_top_min'] = 1.0e-7
    params['atol'] = 1e-25
    params['rtol'] = 1e-3
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*1e4),10)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0
    params['stm_rtol'] = 1e-10
    params['stm_atol'] = 1e-20

    return params

def nominal_imp_23_00(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**23.00
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_23_00"
    params['T_guess'] = 330
    return params

def nominal_imp_23_10(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**23.10
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_23_10"
    params['T_guess'] = 330
    return params

def nominal_imp_23_20(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**23.20
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_23_20"
    params['T_guess'] = 310
    return params

def nominal_imp_23_30(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**23.30
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_23_30"
    params['T_guess'] = 320
    return params

def nominal_imp_23_40(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**23.40
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_23_40"
    params['T_guess'] = 330
    return params

def nominal_imp_23_50(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**23.50
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_23_50"
    params['T_guess'] = 340
    return params

def nominal_imp_23_60(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**23.60
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_23_60"
    params['T_guess'] = 340
    return params

def nominal_imp_23_70(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**23.70
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_23_70"
    params['T_guess'] = 340
    return params

def nominal_imp_23_80(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**23.80
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_23_80"
    params['T_guess'] = 350
    return params

def nominal_imp_23_90(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**23.90
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_23_90"
    params['T_guess'] = 350
    return params

def nominal_imp_24_00(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**24.00
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_24_00"
    params['T_guess'] = 350
    return params

def nominal_imp_24_10(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**24.10
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_24_10"
    params['T_guess'] = 370
    return params

def nominal_imp_24_20(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**24.20
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_24_20"
    params['T_guess'] = 370
    return params

def nominal_imp_24_30(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**24.30
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_24_30"
    params['T_guess'] = 380
    return params

def nominal_imp_24_40(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**24.40
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_24_40"
    params['T_guess'] = 410
    return params

def nominal_imp_24_50(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**24.50
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_24_50"
    params['T_guess'] = 430
    return params

def nominal_imp_24_60(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**24.60
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_24_60"
    params['T_guess'] = 440
    return params

def nominal_imp_24_70(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**24.70
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_24_70"
    params['T_guess'] = 450
    return params

def nominal_imp_24_80(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**24.80
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_24_80"
    params['T_guess'] = 460
    return params

def nominal_imp_24_90(restart_from_file=False, T_surf_guess=300):
    params = nominal(restart_from_file, T_surf_guess)
    params['init']['M_i'] = 10.0**24.90
    params['outfile'] = "results/evolution/nominal_eddymodern/imp_24_90"
    params['T_guess'] = 470
    return params

if __name__ == "__main__":
    threadpool_limits(limits=2)
    models = [
        nominal_imp_23_00, 
        nominal_imp_23_10, 
        nominal_imp_23_20, 
        nominal_imp_23_30,
        nominal_imp_23_40, 
        nominal_imp_23_50, 
        nominal_imp_23_60, 
        nominal_imp_23_70,
        nominal_imp_23_80, 
        nominal_imp_23_90, 
        nominal_imp_24_00, 
        nominal_imp_24_10,
        nominal_imp_24_20, 
        nominal_imp_24_30, 
        nominal_imp_24_40, 
        nominal_imp_24_50, 
        nominal_imp_24_60,
        nominal_imp_24_70,
        nominal_imp_24_80,
        nominal_imp_24_90
    ]

    def wrap(model):
        impact_evolve(**model())
    p = Pool(40)
    p.map(wrap, models)