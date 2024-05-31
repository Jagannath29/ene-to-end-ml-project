# Responsible for creating my ML application as a package. 
# With the help of setup.py, i will be able to create my entire ML app as a package, from there anybody can install it and use it.


from setuptools import find_packages, setup

from typing import List


HYFEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    it returns all the libraries what is inside requriements.txt
    '''
    requirements = []
    with open(file_path) as obj:
        requirements = obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYFEN_E_DOT in requirements:
            requirements.remove(HYFEN_E_DOT)

setup(
    name = 'mlPro',
    version='0.0.1',
    author='Jagannath',
    author_email='khadkajagannath83@gmail.com',
    packages=find_packages(), # sees how many folder in init.py from src.
    install_requires = get_requirements('requirements.txt')
)