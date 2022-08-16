# Wogan-2022-Impacts

Following commands download all code needed to reproduce results. Must have a Fortran and C compiler.

```sh
# create conda environment
conda create -n postimp -c conda-forge python=3.9 numpy scipy pyyaml scikit-build cython jupyter cantera matplotlib pathos threadpoolctl

# activate
conda activate postimp 

# photochem
git clone --recursive --branch=dev https://github.com/Nicholaswogan/photochem
cd photochem
git checkout f43fb88643caf3630d3542faef827e2848751939
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf photochem

# clima
git clone --recursive --branch=dev https://github.com/Nicholaswogan/clima
cd clima
git checkout 04656063738825f5d91978ee5def7751f999f3df
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf clima

# ImpactAtmosphere v4.2.7
git clone --recursive --branch=main https://github.com/Nicholaswogan/ImpactAtmosphere
cd ImpactAtmosphere
git checkout 2528c64c101bbde56db1886c6b59ca3df7cd05f0
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf ImpactAtmosphere
```