import numpy as np

from ImpactAtmosphere import SteamAtm
from coupling import couple2photochem
from photochem import EvoAtmosphere, zahnle_earth
from clima import WaterAdiabatClimate

from threadpoolctl import threadpool_limits

class Constants:
    yr = 365*24*60*60
cons = Constants()

def impact_evolve_Ni(init, settings_in, outfile, eddy, RH, P_top, T_trop, T_guess, zero_out, nz, rainfall_rate, P_top_min, atol, rtol, t_eval, restart_from_file, T_surf_guess, perfect_conversion, Ni_area):
    settings_out = outfile+"_settings.yaml"
    atmosphere_out = outfile+"_atmosphere.txt"
    
    if not restart_from_file:
        N_H2O_ocean = init['N_H2O_ocean']
        N_CO2 = init['N_CO2']
        N_N2  = init['N_N2']
        M_i = init['M_i']
        stm = SteamAtm('Methanation_Ni.yaml', Ni_area = Ni_area)
        sol_stm = stm.impact(N_H2O_ocean,N_CO2,N_N2,M_i)
        if perfect_conversion:
            # We convert all CO2 to CH4 using H2 in the atmosphere.
            CO2 = sol_stm['CO2'][-1]
            sol_stm['CO2'][-1] = sol_stm['CO2'][-1] - CO2
            sol_stm['H2'][-1] = sol_stm['H2'][-1] - 4*CO2
            sol_stm['CH4'][-1] = sol_stm['CH4'][-1] + CO2
            sol_stm['H2O'][-1] = sol_stm['H2O'][-1] + 2*CO2

        c = WaterAdiabatClimate('input/adiabat_species.yaml', \
                                'input/adiabat_settings.yaml', \
                                'input/Sun_4.0Ga.txt')

        couple2photochem(c, sol_stm, settings_in, settings_out, atmosphere_out, \
                    eddy, RH, P_top, T_trop, T_guess, zero_out, nz, rainfall_rate)
    
    pc = EvoAtmosphere(zahnle_earth,\
                       settings_out,\
                       "input/Sun_4.0Ga.txt",\
                       atmosphere_out)

    pc.var.mxsteps = 100000
    pc.var.max_error_reinit_attempts = 100
    pc.T_trop = T_trop
    pc.P_top_min = P_top_min
    pc.P_top_max = 1e10
    pc.top_atmos_adjust_frac = 0.02

    pc.var.atol = atol  
    pc.var.rtol = rtol      
    t_start = 0.0
    if restart_from_file:
        pc.T_surf = T_surf_guess
    success = pc.evolve(outfile+'.dat',t_start, pc.wrk.usol, t_eval, overwrite=False, restart_from_file=restart_from_file)


def nominal_Ni(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 2.0e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/nominal_Ni"
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

    params['Ni_area'] = 1.0

    return params

def pretty_big_Ni(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 1.5e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/pretty_big_Ni"
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

    params['Ni_area'] = 1.0

    return params

def sorta_pretty_big_Ni(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 1.2e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/sorta_pretty_big"
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

    params['Ni_area'] = 1.0

    return params

def sorta_big_Ni(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 1.0e24
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/sorta_big_Ni"
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

    params['Ni_area'] = 1.0

    return params

def less_big_Ni(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 6.0e23
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/less_big_Ni"
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

    params['Ni_area'] = 1.0

    return params

def vesta_Ni(restart_from_file=False, T_surf_guess=300):
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.5
    init['N_N2'] = 36.
    init['M_i'] = 2.589e23
    params['init'] = init
    params['perfect_conversion'] = False

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/vesta_Ni"
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

    params['Ni_area'] = 1.0

    return params

if __name__ == "__main__":
    threadpool_limits(limits=4)
    impact_evolve_Ni(**pretty_big_Ni(restart_from_file=True,T_surf_guess=380))