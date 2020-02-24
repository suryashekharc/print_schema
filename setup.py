from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), "README.md"), 'r') as f:
    long_desc = f.read()

setup(
    name='print_schema',
    version='1.0.1',
    packages=['print_schema'],
    url='https://github.com/suryashekharc/print_schema',
    license='MIT',
    author='Surya Shekhar Chakraborty',
    author_email='suryaschak@gmail.com',
    description='Prints the schema of Python objects',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    install_requires=['requests'],
    python_requires=">=3.5"
)
