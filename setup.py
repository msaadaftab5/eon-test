from setuptools import setup, find_packages

setup(
    name='eon_case_study_dependencies',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A description of your project',
    packages=find_packages(include=['aws_utils']),
    install_requires=[],
    python_requires='>=3.9',
)