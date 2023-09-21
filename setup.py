from setuptools import setup,find_packages
from typing import List

requirements_file = "requirements.txt"
remove_package = "-e ."

def get_requirements()->List[str]:
    with open(requirements_file) as f:
        requirements_list = f.readlines()

    requirements_list = [requirement_name.replace("\n","") for requirement_name in requirements_list]

    if remove_package in requirements_list:
        requirements_list.remove(remove_package)

    return requirements_list

setup(name='Insurance',
      version='0.0.1',
      description='Insurance Industry lavel project',
      author='Karthik',
      author_email='mkarthik0002@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements()
     )