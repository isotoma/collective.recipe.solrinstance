# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages

version = '3.9.dev0'


def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


requires = ['setuptools']
if sys.version_info >= (3,):
    requires += [
        'Genshi>=0.7.0',
        'zc.buildout>=2.0.0a1',
        ]
else:
    requires += [
        'Genshi',
        'zc.buildout<2.0.0a1'
        ]


setup(
    name='collective.recipe.solrinstance',
    version=version,
    description="zc.buildout to configure a solr instance",
    long_description=(
        read('README.rst')
        + '\n' +
        read('CHANGES.rst')
        + '\n' +
        'Contributors\n'
        '***********************\n'
        + '\n' +
        read('CONTRIBUTORS.rst')
        + '\n' +
        'Download\n'
        '***********************\n'),
    classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Topic :: Software Development :: Build Tools',
    ],
    keywords='',
    author='Kai Lautaportti',
    author_email='kai.lautaportti@hexagonit.fi',
    url='http://pypi.python.org/pypi/collective.recipe.solrinstance',
    license='ZPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    setup_requires=[
        'setuptools',
    ],
    tests_require=[
        'zope.exceptions',
        'zope.interface',
        'zope.testing',
    ],
    test_suite='collective.recipe.solrinstance.tests.test_suite',
    entry_points={
        "zc.buildout": [
            "default = collective.recipe.solrinstance:SolrSingleRecipe",
            "mc = collective.recipe.solrinstance:MultiCoreRecipe",
        ]
    },
)
