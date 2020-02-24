from setuptools import setup

setup(
    name='print_schema',
    version='1.0.1',
    packages=['print_schema'],
    url='https://github.com/suryashekharc/print_schema',
    license='MIT',
    author='Surya Shekhar Chakraborty',
    author_email='suryaschak@gmail.com',
    description='Prints the schema of Python objects',
    install_requires=['requests'],
    python_requires=">=3.5"
)
