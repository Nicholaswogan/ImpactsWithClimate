import numpy as np
from photochem.utils._format import FormatSettings_main, yaml, MyDumper, Loader
from photochem.utils._format import FormatSettings_main, yaml, MyDumper, Loader

def make_atmosphere_txt(c, sol, atmosphere_out, eddy, RH, P_top, T_trop, T_guess, zero_out):
    N_i = np.empty(len(c.species_names))
    for i,sp in enumerate(c.species_names):
        if sp in zero_out:
            N_i[i] = 1.0e-20
        else:
            N_i[i] = sol[sp][-1]*sol['Ntot'][-1]
    c.RH = RH
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
    
    