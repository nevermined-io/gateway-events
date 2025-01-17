#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import os
from os.path import join

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

# Installed by pip install ocean-events-handler
# or pip install -e .
install_requirements = [
    'common-utils-py==0.2.8',
    'contracts-lib-py==0.4.0',
    'ocean-secret-store-client==0.0.2',
    'PyYAML==4.2b4',
]

# Required to run setup.py:
setup_requirements = ['pytest-runner', ]

test_requirements = [
    'codacy-coverage',
    'coverage',
    'docker',
    'mccabe',
    'pylint',
    'pytest',
    'pytest-watch',
    'tox',
]

# Possibly required by developers of ocean-events-handler:
dev_requirements = [
    'bumpversion',
    'pkginfo',
    'twine',
    'watchdog',
]

docs_requirements = [
    'Sphinx',
    'sphinxcontrib-apidoc',
]

packages = []
for d, _, _ in os.walk('nevermined_gateway_events'):
    if os.path.exists(join(d, '__init__.py')):
        packages.append(d.replace(os.path.sep, '.'))

setup(
    author="nevermined-io",
    author_email='root@nevermined.io',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="🐳 Publisher events handler agent dealing with Keeper Contract events.",
    extras_require={
        'test': test_requirements,
        'dev': dev_requirements + test_requirements + docs_requirements,
        'docs': docs_requirements,
    },
    install_requires=install_requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='gateway-events',
    name='gateway-events',
    packages=packages,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/nevermined-io/gateway-events',
    version='0.2.3',
    zip_safe=False,
)
