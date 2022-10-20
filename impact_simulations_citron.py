import numpy as np
from threadpoolctl import threadpool_limits

from coupling import impact_evolve, cons
from citron_interpolation import make_iron_interpolator

def imp1_citron(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 1.0e25
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/Citron/imp1_citron"
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

    Fe = make_iron_interpolator(2.0, 45)
    params['Fe_react_frac'] = Fe(init['M_i']).item()
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def imp2_citron(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 8.0e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/Citron/imp2_citron"
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

    Fe = make_iron_interpolator(2.0, 45)
    params['Fe_react_frac'] = Fe(init['M_i']).item()
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def imp3_citron(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 6.0e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/Citron/imp3_citron"
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

    Fe = make_iron_interpolator(2.0, 45)
    params['Fe_react_frac'] = Fe(init['M_i']).item()
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def imp4_citron(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 4.0e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/Citron/imp4_citron"
    params['eddy'] = 1e6
    params['RH'] = 1.0
    params['P_top'] = 1.0e-1
    params['T_trop'] = 200
    params['T_guess'] = 350
    params['zero_out'] = ['NH3']
    params['nz'] = 100
    params['rainfall_rate'] = 1

    params['P_top_min'] = 1.0e-7
    params['atol'] = 1e-25
    params['rtol'] = 1e-3
    params['t_eval'] = np.logspace(np.log10(cons.yr),np.log10(cons.yr*1e4),100)
    params['restart_from_file'] = restart_from_file
    params['T_surf_guess'] = T_surf_guess

    Fe = make_iron_interpolator(2.0, 45)
    params['Fe_react_frac'] = Fe(init['M_i']).item()
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def nominal_citron(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 2.0e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/Citron/nominal_citron"
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

    Fe = make_iron_interpolator(2.0, 45)
    params['Fe_react_frac'] = Fe(init['M_i']).item()
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

def vesta_citron(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 2.589e23
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/Citron/vesta_citron"
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

    Fe = make_iron_interpolator(2.0, 45)
    params['Fe_react_frac'] = Fe(init['M_i']).item()
    params['stm_mechanism'] = 'zahnle_earth_ct.yaml'
    params['Ni_area'] = 0.0

    return params

if __name__ == "__main__":
    threadpool_limits(limits=2)
    impact_evolve(**imp4_citron())