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
git checkout 8deb2684223a61303f2b2f837aca4bd668ad5d0f
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf photochem

# clima
git clone --recursive --branch=dev https://github.com/Nicholaswogan/clima
cd clima
git checkout 12b56645c6fe4490f5c2d7bb61655e5f480cbe13
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf clima

# ImpactAtmosphere 
git clone --recursive --branch=main https://github.com/Nicholaswogan/ImpactAtmosphere
cd ImpactAtmosphere
git checkout b308e45da71b8739e91d070c92a0a8082aebb81f
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf ImpactAtmosphere
```