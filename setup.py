from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(filepath:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name='StudentPerformance_ML',
    version='0.0.1',
    #description='Student Performance Prediction',
    #long_description='',
    #url='https://github.com/JackP27/StudentPerformance_ML',
    author='Jack P',
    author_email="13mscit118@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)