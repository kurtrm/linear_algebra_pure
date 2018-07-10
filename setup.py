"""Setup for decision tree module."""
from setuptools import setup


extra_packages = {
    'testing': ['pytest', 'pytest-cov']
}


setup(
    name='linear_algebra_pure',
    description='Implements import matrix operations in pure Python.',
    version=0.0,
    author='Kurt Maurer',
    author_email='kurtrm@gmail.com',
    extras_require=extra_packages
)
