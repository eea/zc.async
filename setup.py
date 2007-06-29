import os

from setuptools import setup, find_packages

setup(
    name='zc.async',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'':'src'},

    url='http://svn.zope.org/zc.async',
    zip_safe=False,
    author='Gary Poster',
    description='Perform durable tasks asynchronously',
    license='ZPL',
    install_requires=[
        'ZODB3',
        'pytz',
        'rwproperty',
        'twisted ==2.1dev',
        'uuid',
        'zc.queue',
        'zc.set',
        'zc.twist',
        'zope.app.appsetup',
        'zope.bforest',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.testing',
        ],
    include_package_data=True,
    )