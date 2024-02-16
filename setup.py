from setuptools import setup, find_packages

def get_requirements():
    requirements = []
    with open('requirements.txt', 'r') as f:
         requirements.append(f.read().splitlines())
         requirements.remove('-e .')
         return requirements
setup(
    name='YourPackageName',
    version='1.0',
    packages=find_packages(),
    install_requires = get_requirements(),
    author='Aman Raj',
    author_email='araj232@email.com',
    description='This is a python package for image recognition for autonomous vehicles, it uses pre-trained vision transformers and was finetune on public dataset to achieve state of the art results on object detection and image segmentation tasks ',
    url='https://github.com/iAmanSharan/Image_Recognition_For_Autonomous_Vehicles_Vision_Transformer'
)
