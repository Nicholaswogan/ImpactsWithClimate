import numpy as np
from threadpoolctl import threadpool_limits

from coupling import impact_evolve, cons

def imp4(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 4.0e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/nominal/imp4"
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
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*1e4),100)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def nominal(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 2.0e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/nominal/nominal"
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
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*30e6),1000)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def pretty_big(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 1.5e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/nominal/pretty_big"
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
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*30e6),1000)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def pretty_big_no_rain(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 1.5e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/nominal/pretty_big_no_rain"
    params['eddy'] = 1e6
    params['RH'] = 1.0
    params['P_top'] = 1.0e-1
    params['T_trop'] = 200
    params['T_guess'] = 400
    params['zero_out'] = ['NH3']
    params['nz'] = 100
    params['rainfall_rate'] = -1

    params['P_top_min'] = 1.0e-7
    params['atol'] = 1e-26
    params['rtol'] = 1e-3
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*30e6),1000)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def pretty_big_lower_vdep(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 1.5e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean_lowvdep.yaml"
    params['outfile'] = "results/nominal/pretty_big_lower_vdep"
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
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*30e6),1000)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def pretty_big_warm_strat(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 1.5e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/nominal/pretty_big_warm_strat"
    params['eddy'] = 1e6
    params['RH'] = 1.0
    params['P_top'] = 1.0e-1
    params['T_trop'] = 230
    params['T_guess'] = 400
    params['zero_out'] = ['NH3']
    params['nz'] = 100
    params['rainfall_rate'] = 1

    params['P_top_min'] = 1.0e-7
    params['atol'] = 1e-25
    params['rtol'] = 1e-3
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*30e6),1000)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def sorta_pretty_big(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 1.2e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/nominal/sorta_pretty_big"
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
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*30e6),1000)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def sorta_big(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 1.0e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/nominal/sorta_big"
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
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*30e6),1000)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def less_big(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 6.0e23
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/nominal/less_big"
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
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*30e6),1000)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def vesta(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 2.589e23
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/nominal/vesta"
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
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*30e6),1000)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def perfect_vesta(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 2.589e23
    params['init'] = init
    params['perfect_conversion'] = True

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/nominal/perfect_vesta"
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
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*10e6),1000)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    params['Fe_react_frac'] = 1.0
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

if __name__ == "__main__":
    threadpool_limits(limits=4)
    impact_evolve(**imp4())
    
    
    
    
    
