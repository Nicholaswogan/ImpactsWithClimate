# Wogan-2022-Impacts

Following commands download all code needed to reproduce results. Must have a Fortran and C compiler.

```sh
# create conda environment
conda create -n postimp -c conda-forge python=3.9 numpy scipy pyyaml scikit-build cython jupyter cantera matplotlib pathos

# activate
conda activate postimp 

# photochem
wget https://github.com/Nicholaswogan/photochem/archive/f30b95ee5df976060144b59319ad0071b0fde6fa.zip
unzip f30b95ee5df976060144b59319ad0071b0fde6fa.zip
cd photochem-f30b95ee5df976060144b59319ad0071b0fde6fa
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf photochem-f30b95ee5df976060144b59319ad0071b0fde6fa f30b95ee5df976060144b59319ad0071b0fde6fa.zip

# clima
wget https://github.com/Nicholaswogan/clima/archive/.zip
unzip .zip
cd photochem-
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf photochem- .zip

# ImpactAtmosphere v4.2.7
wget https://github.com/Nicholaswogan/ImpactAtmosphere/archive/2528c64c101bbde56db1886c6b59ca3df7cd05f0.zip
unzip 2528c64c101bbde56db1886c6b59ca3df7cd05f0.zip
cd ImpactAtmosphere-2528c64c101bbde56db1886c6b59ca3df7cd05f0
python -m pip install --no-deps --no-build-isolation . -v
cd ..
rm -rf ImpactAtmosphere-2528c64c101bbde56db1886c6b59ca3df7cd05f0 2528c64c101bbde56db1886c6b59ca3df7cd05f0.zip
```