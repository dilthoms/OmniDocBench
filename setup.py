from setuptools import setup, find_packages
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name='omnidocbench',
    version='1.0',
    install_requires=requirements,
    packages=find_packages()
)
