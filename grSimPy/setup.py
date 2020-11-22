from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(name='grSimPy',
      description='This is an api to use grSim in python',
      long_description=long_description,  # Optional
      version='0.0.1',
      package_dir={'': 'src'},  # Optional
      packages=find_packages(where='src'),  # Required
      install_requires=[]  # And any other dependencies foo needs
)