from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='generic_ml',
version='0.0.1',
author='shrihari',
author_email='shriharinair@htic.iitm.ac.in',
packages=find_packages(),                                  #when find_packages() run it checks for how many folders have __init__.py
install_requires=get_requirements('requirements.txt')

)