from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='Minecraft Server Manager',
    version='0.0.1',
    author='Jonathyn Stiverson',
    author_email='jstiverson2002@gmail.com',
    description='A Python Application to easily manage and intergrate Minecraft Servers.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='com.jstiverson',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='<=3.8',
    install_requires=['sockets']
)
