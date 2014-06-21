#!/usr/bin/env python

from setuptools import setup

setup(
    name='DjangoTest',
    version='1.0',
    description='DjangoTest',
    author='David Bernick',
    author_email='dbernick@gmail.com',
    install_requires=['django',
                      'django-guardian',
                      'boto',
                      'django-social-auth',
                      'django-bootstrap3',
                      'djangorestframework',
                      'markdown',
                      'django-filter',
                      'south'
                      ],
)