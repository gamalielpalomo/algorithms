from distutils.core import setup
from Cython.Build import cythonize

setup(name='BubbleSort', ext_modules=cythonize("BubbleLoops.pyx"))