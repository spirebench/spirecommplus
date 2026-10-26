from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='spirecommplus',
    version='0.6.0',
    packages=['spirecommplus', 'spirecommplus.ai', 'spirecommplus.spire', 'spirecommplus.communication'],
    url='https://github.com/spirebench/spirecommplus',
    license='MIT License',
    author='ForgottenArbiter',
    author_email='forgottenarbiter@gmail.com',
    description='A package for interfacing with Slay the Spire through CommunicationModPlus',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
