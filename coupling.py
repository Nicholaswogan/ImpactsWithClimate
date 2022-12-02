import numpy as np

from ImpactAtmosphere import SteamAtm, SteamAtmContinuous
from photochem import EvoAtmosphere, zahnle_earth
from photochem.utils._format import FormatSettings_main, yaml, MyDumper, Loader
from clima import AdiabatClimate

def make_atmosphere_txt(c, sol, atmosphere_out, eddy, RH, P_top, T_trop, T_guess, zero_out):
    N_i = np.empty(len(c.species_names))
    for i,sp in enumerate(c.species_names):
        if sp in zero_out:
            N_i[i] = 1.0e-20
        else:
            N_i[i] = sol[sp][-1]*sol['Ntot'][-1]
    c.RH = np.ones(len(c.species_names))*RH
    c.P_top = P_top
    c.T_trop = T_trop
    T = c.surface_temperature_column(N_i, T_guess=T_guess) 
    eddy_ = np.ones(len(c.z))*eddy 
    c.out2atmosphere_txt(atmosphere_out, eddy_)    

def make_settings(infile, outfile, ztop, nz, RH, rainfall_rate, trop_alt):

    fil = open(infile,'r')
    data = yaml.load(fil,Loader=Loader)
    fil.close()

    data['atmosphere-grid']['bottom'] = 0.0
    data['atmosphere-grid']['top'] = float(ztop)
    data['atmosphere-grid']['number-of-layers'] = int(nz)
    
    data['planet']['water']['relative-humidity'] = float(RH)
    
    if rainfall_rate > 0:
        data['planet']['water']['gas-rainout'] = True
        data['planet']['water']['rainfall-rate'] = float(rainfall_rate)
        data['planet']['water']['tropopause-altitude'] = float(trop_alt)
    else:
        data['planet']['water']['gas-rainout'] = False    
    
    data = FormatSettings_main(data)

    fil = open(outfile,'w')
    yaml.dump(data,fil,Dumper=MyDumper,sort_keys=False,width=70)
    fil.close()
    
def couple2photochem(c, sol, settings_in, settings_out, atmosphere_out, \
                     eddy, RH, P_top, T_trop, T_guess, zero_out, nz, rainfall_rate):
    make_atmosphere_txt(c, sol, atmosphere_out, eddy, RH, P_top, T_trop, T_guess, zero_out)
    
    ind = (c.T-c.T_trop==0).argmax()
    trop_alt = c.z[ind]
    
    ztop = c.z[-1]+0.5*c.dz[-1]
    
    make_settings(settings_in, settings_out, ztop, nz, RH, rainfall_rate, trop_alt)

def impact_evolve(init, settings_in, outfile, eddy, RH, P_top, T_trop, T_guess, zero_out, nz, rainfall_rate, 
                  P_top_min, atol, rtol, t_eval, restart_from_file, T_surf_guess, perfect_conversion, 
                  Fe_react_frac, stm_mechanism, Ni_area, stm_rtol, stm_atol):
    settings_out = outfile+"_settings.yaml"
    atmosphere_out = outfile+"_atmosphere.txt"
    
    if not restart_from_file:
        N_H2O_ocean = init['N_H2O_ocean']
        N_CO2 = init['N_CO2']
        N_N2  = init['N_N2']
        M_i = init['M_i']
        stm = SteamAtm(stm_mechanism, Fe_react_frac=Fe_react_frac, Ni_area=Ni_area)
        stm.rtol = stm_rtol
        stm.atol = stm_atol
        sol_stm = stm.impact(N_H2O_ocean,N_CO2,N_N2,M_i)
        if perfect_conversion:
            # We convert all CO2 to CH4 using H2 in the atmosphere.
            CO2 = sol_stm['CO2'][-1]
            sol_stm['CO2'][-1] = sol_stm['CO2'][-1] - CO2
            sol_stm['H2'][-1] = sol_stm['H2'][-1] - 4*CO2
            sol_stm['CH4'][-1] = sol_stm['CH4'][-1] + CO2
            sol_stm['H2O'][-1] = sol_stm['H2O'][-1] + 2*CO2

        c = AdiabatClimate('input/adiabat_species.yaml', \
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

def impact_evolve_continuous(init, settings_in, outfile, eddy, RH, P_top, T_trop, T_guess, zero_out, nz, rainfall_rate, 
                             P_top_min, atol, rtol, t_eval, restart_from_file, T_surf_guess, perfect_conversion, 
                             Fe_react_frac, stm_mechanism, Ni_area, stm_rtol, stm_atol):
    settings_out = outfile+"_settings.yaml"
    atmosphere_out = outfile+"_atmosphere.txt"
    
    if not restart_from_file:
        N_H2O_ocean = init['N_H2O_ocean']
        N_CO2 = init['N_CO2']
        N_N2  = init['N_N2']
        M_i = init['M_i']
        stm = SteamAtmContinuous(stm_mechanism, Fe_react_frac=Fe_react_frac, Ni_area=Ni_area)
        stm.rtol = stm_rtol
        stm.atol = stm_atol
        sol_stm = stm.impact(N_H2O_ocean,N_CO2,N_N2,M_i,include_condensing_phase=False)
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

class Constants:
    yr = 365*24*60*60
cons = Constants()