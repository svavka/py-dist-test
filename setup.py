from setuptools import setup, find_packages 
from os.path import join, dirname 

setup(
    name='helloworld',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    entry_points={
        'console_scripts':
            ['hellowolrd=helloworld.core:print_message']
    }
)