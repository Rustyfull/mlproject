from setuptools import find_packages, setup
from typing import List

HYPING_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list requirements
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n',' ') for req in requirements]
        if HYPING_E_DOT in requirements:
            requirements.remove(HYPING_E_DOT)

    return  requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='elite',
    author_email='kanarusty2002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

