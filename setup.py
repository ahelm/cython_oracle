from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        Extension(
            "cython_oracle.oracle",
            ["cython_oracle/oracle.pyx", "liboracle/src/oracle.c"],
            include_dirs=["liboracle/src"],
        ),
        compiler_directives={"language_level": 3},
    )
)
