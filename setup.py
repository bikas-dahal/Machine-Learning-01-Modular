from setuptools import find_packages, setup 
from typing import  List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path):
    '''
    This function will return a list of requirements from the file path
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines() 
        requirements = [line.replace('\n', "") for line in requirements ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        
    return requirements




setup(
    name='ml_01',
    packages=find_packages(),
    version='0.1.0',
    description='Machine Learning 01',
    author='bikas-dahal',
    license='MIT',
    author_email='bikkydahal@gmail.com',
    install_requires=get_requirements('requirements.txt'),
)