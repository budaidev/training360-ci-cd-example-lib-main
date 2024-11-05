from setuptools import setup, find_packages

setup(
    name='training360_example_lib',
    version='1.0.0',
    description='A simple library',
    author='Nadai Endre Levente',
    author_email='nnlete@gmail.com',
    packages=find_packages(),
    install_requires=[
        'fuzzywuzzy',
    ],
)
