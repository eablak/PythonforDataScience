from setuptools import setup, find_packages

"""
To create a Python package, we need to write a setup.py file.

- Name: The name of the package.
- Version: The version of the package (e.g., 0.0.1).
- Description: A short description of what the package does.
- Author: The person who wrote the package.
- Author Email: The email address of the author.
- URL: The location of the package's source code (usually a repository).
- Packages: Automatically finds the packages used in the project.
    This is done using the find_packages() function from setuptools.
- Classifiers: A list of classifiers that describe the package, 
    such as supported programming languages, license type, etc.
- Entry Points: This is used to define entry points for executable scripts, 
    such as console scripts.
"""

setup(
    name='ft_package',
    version='0.0.1',
    description='A sample test package',
    author='eablak',
    author_email='eablak@student.42istanbul.com.tr',
    url='https://github.com/eablak/PythonforDataScience/\
Starting/ex_09/ft_package',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [],
    },
    license='MIT',
)
