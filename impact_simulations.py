import numpy as np

from ImpactAtmosphere import SteamAtm
from coupling import couple2photochem
from photochem import EvoAtmosphere, zahnle_earth
from clima import WaterAdiabatClimate

from threadpoolctl import threadpool_limits

class Constants:
    yr = 365*24*60*60
cons = Constants()

def impact_evolve(init, settings_in, outfile, eddy, RH, P_top, T_trop, T_guess, zero_out, nz, rainfall_rate, P_top_min, atol, rtol, t_eval):
    N_H2O_ocean = init['N_H2O_ocean']
    N_CO2 = init['N_CO2']
    N_N2  = init['N_N2']
    M_i = init['M_i']
    stm = SteamAtm('zahnle_earth_ct.yaml')
    sol_stm = stm.impact(N_H2O_ocean,N_CO2,N_N2,M_i)

    c = WaterAdiabatClimate('input/adiabat_species.yaml', \
                            'input/adiabat_settings.yaml', \
                            'input/Sun_4.0Ga.txt')

    settings_out = outfile+"_settings.yaml"
    atmosphere_out = outfile+"_atmosphere.txt"

    couple2photochem(c, sol_stm, settings_in, settings_out, atmosphere_out, \
                 eddy, RH, P_top, T_trop, T_guess, zero_out, nz, rainfall_rate)
    
    pc = EvoAtmosphere(zahnle_earth,\
                       settings_out,\
                       "input/Sun_4.0Ga.txt",\
                       atmosphere_out)

    pc.T_trop = T_trop
    pc.P_top_min = P_top_min
    pc.P_top_max = 1e10
    pc.top_atmos_adjust_frac = 0.02

    pc.var.atol = atol  
    pc.var.rtol = rtol      
    t_start = 0.0
    success = pc.evolve(outfile+'.dat',t_start, pc.wrk.usol, t_eval, overwrite=True)

def nominal():
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.1
    init['N_N2'] = 36.
    init['M_i'] = 2.589e23
    params['init'] = init

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/CO2=2.3e0_N2=3.6e1_M_i=2.0e24_eddy=1e6"
    params['eddy'] = 1e6
    params['RH'] = 1.0
    params['P_top'] = 1.0e-4
    params['T_trop'] = 200
    params['T_guess'] = 400
    params['zero_out'] = ['NH3']
    params['nz'] = 100
    params['rainfall_rate'] = 1

    params['P_top_min'] = 4.0e-8
    params['atol'] = 1e-25
    params['rtol'] = 1e-3
    params['t_eval'] = np.logspace(5,np.log10(cons.yr*10e6),500)

    return params

def pretty_big():
    params = {}

    init = {}
    init['N_H2O_ocean'] = 15.0e3
    init['N_CO2'] = 23.*0.1
    init['N_N2'] = 36.
    init['M_i'] = 1.0e24
    params['init'] = init

    params['settings_in'] = "input/settings_Hadean.yaml"
    params['outfile'] = "results/pretty_big"
    params['eddy'] = 1e6
    params['RH'] = 1.0
    params['P_top'] = 1.0e-3
    params['T_trop'] = 200
    params['T_guess'] = 400
    params['zero_out'] = ['NH3']
    params['nz'] = 100
    params['rainfall_rate'] = 1

    params['P_top_min'] = 1.0e-8
    params['atol'] = 1e-25
    params['rtol'] = 1e-3
    params['t_eval'] = np.logspace(5,np.log10(cons.yr*10e6),500)

    return params

if __name__ == "__main__":
    threadpool_limits(limits=1)
    # impact_evolve(**nominal())
    
    
    
    
    
