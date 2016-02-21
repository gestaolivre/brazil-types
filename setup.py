# -*- coding: utf-8 -*-
u"""Instalation files for brazil-types."""

from setuptools import setup, find_packages
from setuptools.command.test import test as test_command
from brazil_types import __version__


class PyTest(test_command):
    u"""Helper class to execute unit tests."""

    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        u"""Initialize the test options."""
        test_command.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        u"""Finalize the test options."""
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        u"""Run tests."""
        import sys
        import pytest

        errno = pytest.main(self.pytest_args)

        sys.exit(errno)


setup(
    name='brazil-types',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    version=__version__,
    description='Biblioteca com os tipos de dados usados no Brasil.',
    long_description='Biblioteca com os tipos de dados usados no Brasil.',
    author='Sergio Garcia',
    author_email='contato@gestaolivre.org',
    url='https://github.com/gestaolivre/brazil-types',
    download_url='https://github.com/gestaolivre/brazil-types/releases',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='brazil types receita federal',
    install_requires=['six'],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
