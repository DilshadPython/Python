Download from https://www.anaconda.com/download

Installation:

$ bash ~/Downloads/Anaconda3-2023.09-0-Linux-x86_64.sh
$ bash ~/Downloads/Anaconda3-2023.09-0-Linux-x86_64.sh -u   (For update)

# Create Anaconda first file:7
===================================================
~ conda create --name env310 python=3.10  # PRESS ENTER
Retrieving notices: ...working... done
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/dilmac/anaconda3/envs/env310

  added / updated specs:
    - python==3.10


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    libffi-3.3                 |       he6710b0_2          50 KB
    openssl-1.1.1w             |       h7f8727e_0         3.7 MB
    pip-23.3.1                 |  py310h06a4308_0         2.7 MB
    python-3.10.0              |       h12debd9_5        23.5 MB
    setuptools-68.0.0          |  py310h06a4308_0         936 KB
    wheel-0.41.2               |  py310h06a4308_0         109 KB
    xz-5.4.5                   |       h5eee18b_0         646 KB
    ------------------------------------------------------------
                                           Total:        31.6 MB

The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main 
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-5.1-1_gnu 
  bzip2              pkgs/main/linux-64::bzip2-1.0.8-h7b6447c_0 
  ca-certificates    pkgs/main/linux-64::ca-certificates-2023.08.22-h06a4308_0 
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.38-h1181459_1 
  libffi             pkgs/main/linux-64::libffi-3.3-he6710b0_2 
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-11.2.0-h1234567_1 
  libgomp            pkgs/main/linux-64::libgomp-11.2.0-h1234567_1 
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-11.2.0-h1234567_1 
  libuuid            pkgs/main/linux-64::libuuid-1.41.5-h5eee18b_0 
  ncurses            pkgs/main/linux-64::ncurses-6.4-h6a678d5_0 
  openssl            pkgs/main/linux-64::openssl-1.1.1w-h7f8727e_0 
  pip                pkgs/main/linux-64::pip-23.3.1-py310h06a4308_0 
  python             pkgs/main/linux-64::python-3.10.0-h12debd9_5 
  readline           pkgs/main/linux-64::readline-8.2-h5eee18b_0 
  setuptools         pkgs/main/linux-64::setuptools-68.0.0-py310h06a4308_0 
  sqlite             pkgs/main/linux-64::sqlite-3.41.2-h5eee18b_0 
  tk                 pkgs/main/linux-64::tk-8.6.12-h1ccaba5_0 
  tzdata             pkgs/main/noarch::tzdata-2023c-h04d1e81_0 
  wheel              pkgs/main/linux-64::wheel-0.41.2-py310h06a4308_0 
  xz                 pkgs/main/linux-64::xz-5.4.5-h5eee18b_0 
  zlib               pkgs/main/linux-64::zlib-1.2.13-h5eee18b_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                            
Preparing transaction: done                                                                                                                 
Verifying transaction: done                                                                                                                 
Executing transaction: done                                                                                                                 
#                                                                                                                                           
# To activate this environment, use                                                                                                         
#                                                                                                                                           
#     $ conda activate env310
#
# To deactivate an active environment, use
#
#     $ conda deactivate


- TO ACTIVATE CURRENT VIRTUALENV (env310) RUN:
~ conda activate env310

- TO DISPLAY LIST OF INSTALLATION TOOLS IN THE ENV310 RUN:
~ conda list

- INSTALL EXTRA TOOLS IN ENV310
~ conda install -c pytorch pytorch
Channels:
 - pytorch
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/dilmac/anaconda3/envs/env310

  added / updated specs:
    - pytorch


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    filelock-3.13.1            |  py310h06a4308_0          21 KB
    gmpy2-2.1.2                |  py310heeb90bb_0         517 KB
    jinja2-3.1.2               |  py310h06a4308_0         215 KB
    llvm-openmp-14.0.6         |       h9e868ea_0         4.4 MB
    markupsafe-2.1.1           |  py310h7f8727e_0          34 KB
    mpmath-1.3.0               |  py310h06a4308_0         834 KB
    networkx-3.1               |  py310h06a4308_0         2.8 MB
    python-3.10.13             |       h955ad1f_0        26.8 MB
    pytorch-2.1.1              |     py3.10_cpu_0        77.2 MB  pytorch
    pytorch-mutex-1.0          |              cpu           3 KB  pytorch
    pyyaml-6.0.1               |  py310h5eee18b_0         180 KB
    sympy-1.12                 |  py310h06a4308_0        10.5 MB
    typing_extensions-4.7.1    |  py310h06a4308_0          55 KB
    ------------------------------------------------------------
                                           Total:       123.5 MB

The following NEW packages will be INSTALLED:

  blas               pkgs/main/linux-64::blas-1.0-mkl 
  filelock           pkgs/main/linux-64::filelock-3.13.1-py310h06a4308_0 
  gmp                pkgs/main/linux-64::gmp-6.2.1-h295c915_3 
  gmpy2              pkgs/main/linux-64::gmpy2-2.1.2-py310heeb90bb_0 
  intel-openmp       pkgs/main/linux-64::intel-openmp-2023.1.0-hdb19cb5_46306 
  jinja2             pkgs/main/linux-64::jinja2-3.1.2-py310h06a4308_0 
  llvm-openmp        pkgs/main/linux-64::llvm-openmp-14.0.6-h9e868ea_0 
  markupsafe         pkgs/main/linux-64::markupsafe-2.1.1-py310h7f8727e_0 
  mkl                pkgs/main/linux-64::mkl-2023.1.0-h213fc3f_46344 
  mpc                pkgs/main/linux-64::mpc-1.1.0-h10f8cd9_1 
  mpfr               pkgs/main/linux-64::mpfr-4.0.2-hb69a4c5_1 
  mpmath             pkgs/main/linux-64::mpmath-1.3.0-py310h06a4308_0 
  networkx           pkgs/main/linux-64::networkx-3.1-py310h06a4308_0 
  pytorch            pytorch/linux-64::pytorch-2.1.1-py3.10_cpu_0 
  pytorch-mutex      pytorch/noarch::pytorch-mutex-1.0-cpu 
  pyyaml             pkgs/main/linux-64::pyyaml-6.0.1-py310h5eee18b_0 
  sympy              pkgs/main/linux-64::sympy-1.12-py310h06a4308_0 
  tbb                pkgs/main/linux-64::tbb-2021.8.0-hdb19cb5_0 
  typing_extensions  pkgs/main/linux-64::typing_extensions-4.7.1-py310h06a4308_0 
  yaml               pkgs/main/linux-64::yaml-0.2.5-h7b6447c_0 

The following packages will be UPDATED:

  libffi                                     3.3-he6710b0_2 --> 3.4.4-h6a678d5_0 
  openssl                                 1.1.1w-h7f8727e_0 --> 3.0.12-h7f8727e_0 
  python                                  3.10.0-h12debd9_5 --> 3.10.13-h955ad1f_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                                                                                            
Preparing transaction: done                                                                                                                 
Verifying transaction: done                                                                                                                 
Executing transaction: done        

# END of conda install -c pytorch pytorch

~ conda deactivate

~ conda install -c pytorch pytorch 
~ conda remove pytorch 

# Display a list of enviroments has been created with conda:
conda env list
# conda environments:
#
base                  *  /home/dilmac/anaconda3
env27                    /home/dilmac/anaconda3/envs/env27
env310                   /home/dilmac/anaconda3/envs/env310
pandaenv                 /home/dilmac/anaconda3/envs/pandaenv



