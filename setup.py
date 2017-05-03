from setuptools import setup, find_packages 
from os.path import join, dirname 
import helloworld


setup(
    name='helloworld',
    version=helloworld.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    entry_points={
        'console_scripts':
            [
                'hellowolrd=helloworld.core:print_message',
                'serve=helloworld.web:run_server'
            ]
    },
    install_requires=[
        'Flask'
    ],
    include_package_data=True
)
