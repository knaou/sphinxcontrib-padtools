from setuptools import setup, find_packages

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = 'README file is not found'

setup(
    name='sphinxcontrib-padtools',
    version='0.1.0',
    url='https://github.com/dummy',
    license='BSD',
    author='Naoya KOUYAMA',
    author_email='monaou@gmail.com',
    description='Sphinx "padtools" extension; embed PAD diagram by using padtools',
    long_description=readme,
    zip_safe=False,
    classifiers=[
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=['sphinxcontrib'],
    install_requires=[
        'Sphinx>=3.5',
        'sphinxcontrib-imagehelper',
        ],
)
