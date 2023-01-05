import numpy as np
from threadpoolctl import threadpool_limits

from coupling import impact_evolve, cons

def nominal_full(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 10.0**24.2
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/evolution/nominal_full"
    params['eddy'] = 1e6
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
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*30e6),2000)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0
    params['stm_rtol'] = 1e-10
    params['stm_atol'] = 1e-20

    return params

def nominal_Ni_full(restart_from_file=False, T_surf_guess=300):
    params = nominal_full(restart_from_file, T_surf_guess)
    params['outfile'] = "results/evolution/nominal_Ni_full"

    params['stm_mechanism'] = 'Methanation_Ni.yaml'
    params['Ni_area'] = 10.0
    params['top_atmos_adjust_frac'] = 0.01
    params['T_guess'] = 380

    return params

def nominal_NH3_full(restart_from_file=False, T_surf_guess=300):
    params = nominal_full(restart_from_file, T_surf_guess)
    params['outfile'] = "results/evolution/nominal_NH3_full"

    params['top_atmos_adjust_frac'] = 0.01
    params['settings_in'] = "input/settings_Hadean_noNH3rain.yaml"
    params['zero_out'] = []

    return params

if __name__ == "__main__":
    threadpool_limits(limits=4)
    impact_evolve(**nominal_NH3_full(restart_from_file=True, T_surf_guess=370))
    
    
    
    
    
