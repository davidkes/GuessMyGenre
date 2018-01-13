# GuessMyGenre
In order to use this program, the user must have some python packages/modules installed. The user will require the
following python packages/modules:

1. numpy
2. scipy
3. scikit-learn
4. pandas

The easiest way to install these packages is to use the anaconda software. Go to https://www.continuum.io/downloads to
download and install the latest version of the anaconda software for the python version the user is currently using.

Once anaconda is installed correctly, open the command prompt and type in following to create a new python environment

    conda create --name [environment name] python-[python version]

for example,

    conda create -- name myenvironment python-3.5

Now, the user must active the environment with the following:

    activate [environmen name]

for example,

    activate myenvironment

Now, to install the python packages/modules use in the following:

    conda install [package name]

for example,

    conda install numpy
    conda install scipy
    conda install scikit-learn
    conda install panda

Now, the user can open the new python environment from the new environment directory or import the environment using
a python interpreter such as pyCharm.
