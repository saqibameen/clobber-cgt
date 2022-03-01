from distutils.core import Extension, setup
from Cython.Build import cythonize

# define an extension that will be cythonized and compiled
ext = Extension(name="clobber_1d_cy", sources=["clobber_1d_cy.pyx" ])
ext_2 = Extension(name="cgt_cy", sources=["cgt_cy.pyx"])
ext_3 = Extension(name="transposition_table_simple_cy", sources=["transposition_table_simple_cy.pyx"])


setup(ext_modules=cythonize(ext))
setup(ext_modules=cythonize(ext_2))
setup(ext_modules=cythonize(ext_3))