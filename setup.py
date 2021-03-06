import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='FlavorTexts',
    packages=['FlavorTexts'],
    version='0.1.0',
    description='A pure-python recreation of Zack Freedman\'s FlavorText Arduino IDE Library',
    author='A-c0rN',
    author_email='acrn@gwes-eas.network',
    license='ODbL-1.0',
    install_requires=['FlavorTexts'],
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/A-c0rN/FlavorTexts',
    keywords='random text insane',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: Other/Proprietary License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        "Topic :: Software Development :: Libraries",
        'Topic :: Utilities',
    ]
)