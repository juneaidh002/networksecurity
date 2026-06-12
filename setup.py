'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration
of your projec, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup 
from typing import List 

def get_requirements() -> List[str]:
    """
    This function will return list of requirments
    """
    try:
        hyphen_e = '-e .'
        requirements = []
        with open('requirements.txt','r') as file:
            # Read lines from file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty and -e .
                if requirement and requirement != hyphen_e:
                    requirements.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found")
    return requirements

setup(
    name="NetworkSecurity",
    version = "0.0.1",
    author="Juneaidh",
    author_email="juneaidhshaik@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
