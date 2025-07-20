from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements

    '''
    requirements=[]
    with open (file_path) as file_obj:     # Revise File Handling to understand it better 
        requirements=file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        # the `-e .` in the requirements.txt file should not come in the requirements list, so we need to remove it 
        if '-e .' in requirements:
            requirements.remove('-e .')

        return requirements



setup(
    name="mlproject",                  # 🔸 Name of your project
    version="0.0.1",                       # 🔸 Version
    author="Ayush Pandey",                    # 🔸 Author name
    author_email= "ayush18805@gmail.com",
    description="A simple ML project",     # 🔸 Short description

    packages= find_packages(),              # 🔍 Automatically finds your code folders
    install_requires= get_requirements('requirements.txt')      # 📦 Dependencies

)
