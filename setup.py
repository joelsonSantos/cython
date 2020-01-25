from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["primes.pyx", "primes_python.py"], annotate=True),
)
