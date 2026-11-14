from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() ## /n is added want to replace with black
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(

    name='MLproject',
    version='0.0.1',
    author='kushal',
    author_email='hkush6431@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)