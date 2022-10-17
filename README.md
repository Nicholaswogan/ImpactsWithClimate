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
git checkout 7ffb1eae9675f3a1f61d94169799b33352470351
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf photochem

# clima
git clone --recursive --branch=dev https://github.com/Nicholaswogan/clima
cd clima
git checkout c6b05bdf2d5eccdc9db124e0d3fe6d04d8e44c55
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf clima

# ImpactAtmosphere 
git clone --recursive --branch=main https://github.com/Nicholaswogan/ImpactAtmosphere
cd ImpactAtmosphere
git checkout 9ea5fb6c3219a8c77efc374524436c515739b318
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf ImpactAtmosphere
```