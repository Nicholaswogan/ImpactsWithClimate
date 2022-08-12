from photochem import EvoAtmosphere, zahnle_earth, io
import numpy as np
from matplotlib import pyplot as plt
from threadpoolctl import threadpool_limits
import impact_simulations as imp
from impact_simulations import cons
import subprocess

def make_movie(params, location, istart):
    sol1 = io.evo_read_evolve_output(params['outfile']+".dat")
    sol_pc = io.reformat_output_dict(sol1)

    pc = EvoAtmosphere(zahnle_earth,\
                params['outfile']+"_settings.yaml",\
                "input/Sun_4.0Ga.txt",\
                params['outfile']+"_atmosphere.txt")

    species = ['H2','N2','CO2','H2O','CH4','CO','HCN']

    for i in range(istart,len(sol_pc['time'])):
        plt.rcParams.update({'font.size': 15})
        fig,ax = plt.subplots(1,1,figsize=[7,5])
        fig.patch.set_facecolor("w")
        
        den = np.sum(sol1['usol'][:,:,i],axis=0)
        pc.regrid_prep_atmosphere(sol1['usol'][:,:,i],sol1['top_atmos'][i])
        for sp in species:
            ax.plot(sol_pc[sp][:,i]/den,sol1['alt'][:,i],label=sp)

        ax.grid()
        ax.legend(ncol=2,bbox_to_anchor=(1,1.0),loc='upper left')
        ax.set_xscale('log')
        ax.set_xlim(1e-10,2)

        ax.set_ylim(0,sol_pc['alt'][-1,0])
        message = 'Time = '+'%.5e'%(sol_pc['time'][i]/cons.yr)+' yr' \
          +'\nSurface Pressure = '+'%.5f'%pc.var.surface_pressure+' bar' \
          +'\nSurface Temperature = '+'%.2f'%pc.T_surf+' K'
        ax.text(0.02, 1.04, message, \
            size = 15,ha='left', va='bottom',transform=ax.transAxes)
        ax.set_ylabel('Altitude (km)')
        ax.set_xlabel('Mixing Ratio')

        plt.savefig(location+'image-'+"{:04d}".format(i)+'.png',dpi=150,bbox_inches='tight')
        plt.close()
        fmt = '{:10}'
        print(fmt.format(i),fmt.format(len(sol_pc['time'])),end='\r')

def make_actual_movie(location):
    cmd = 'rm '+location+'output.mp4'
    subprocess.call(cmd,shell=True)
    cmd = 'ffmpeg -framerate 10 -i '+location+'image-%04d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" '+location+'output.mp4'
    subprocess.call(cmd,shell=True)

if __name__ == "__main__":
    threadpool_limits(limits=4)

    location = '../movie2/'
    istart = 433

    make_movie(imp.pretty_big(), location, istart)
    make_actual_movie(location)

