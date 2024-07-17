from setuptools import setup, find_packages

setup(
    name='eon_case_study_dependencies',
    version='1.0.0',
    author='Muhammad Saad',
    author_email='msaadaftab5@gmail.com',
    description='This project contains some self written utility back end '
                'for aws services helping development on local stack',
    packages=find_packages(include=['aws_utils']),
    install_requires=[],
    python_requires='>=3.9',
)