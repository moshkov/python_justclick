import os
from setuptools import setup
from python_justclick import VERSION


PATH_BASE = os.path.dirname(__file__)
PATH_BIN = os.path.join(PATH_BASE, 'bin')

SCRIPTS = None
if os.path.exists(PATH_BIN):
    SCRIPTS = [os.path.join('bin', f) for f in os.listdir(PATH_BIN) if os.path.join(PATH_BIN, f)]

f = open(os.path.join(PATH_BASE, 'README.rst'))
README = f.read()
f.close()

setup(
    name='python_justclick',
    version='.'.join(map(str, VERSION)),
    url='https://github.com/moshkov/python_justclick',

    description='Python JustClick API',
    long_description=README,
    license='MIT License',

    author='Ivan Moshkov',
    author_email='ivan@moshkov.pro',

    packages=['python_justclick'],
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'requests',
    ],
    scripts=SCRIPTS,

    classifiers=[
        # As in https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License'
    ],
)

