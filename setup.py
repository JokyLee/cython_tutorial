from distutils.core import setup
from Cython.Build import cythonize

setup(
    # ext_modules = cythonize("helloworld.pyx")
    ext_modules = cythonize("sin_from_math.pyx")
    # ext_modules = cythonize("primes.pyx")
)
