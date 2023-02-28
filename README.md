# Wogan-2022-Impacts

Following commands download all code needed to reproduce results. Must have a Fortran and C compiler.

```sh
# create conda environment
conda create -n postimp -c conda-forge python=3.9 numpy scipy pyyaml scikit-build cython jupyter cantera matplotlib pathos threadpoolctl numba h5py

# activate
conda activate postimp 

# photochem
git clone --recursive --branch=dev https://github.com/Nicholaswogan/photochem
cd photochem
git checkout 07344cac846ddf62f9f0ccbdc4ee9186b09b034f
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf photochem

# clima
git clone --recursive --branch=dev https://github.com/Nicholaswogan/clima
cd clima
git checkout 96dd6d7d086713811a5bde50757527e329233a98
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf clima

# ImpactAtmosphere 
git clone --recursive --branch=main https://github.com/Nicholaswogan/ImpactAtmosphere
cd ImpactAtmosphere
git checkout 56638251dc697c1d3d53bd1af7276f737be1e406
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf ImpactAtmosphere
```