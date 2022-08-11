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
git checkout f30b95ee5df976060144b59319ad0071b0fde6fa
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf photochem

# clima
git clone --recursive --branch=dev https://github.com/Nicholaswogan/clima
cd clima
git checkout 21a1ac129e6b456ca26a84ff15a819190d78dc2a
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf clima

# ImpactAtmosphere v4.2.7
wget https://github.com/Nicholaswogan/ImpactAtmosphere/archive/2528c64c101bbde56db1886c6b59ca3df7cd05f0.zip
unzip 2528c64c101bbde56db1886c6b59ca3df7cd05f0.zip
cd ImpactAtmosphere-2528c64c101bbde56db1886c6b59ca3df7cd05f0
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf ImpactAtmosphere-2528c64c101bbde56db1886c6b59ca3df7cd05f0 2528c64c101bbde56db1886c6b59ca3df7cd05f0.zip
```