from setuptools import setup

__version__ = '0.0.1'

with open("README.md") as f:
    long_description = f.read()

setup(
    name='mnxref',
    version=__version__,
    url='https://github.com/ecell/mnxref',
    license='MIT',
    py_modules=['mnxref'],
    python_requires='>=3.6',
    author='Kozo Nishida',
    author_email='knishida@riken.jp',
    install_requires=['sparqlwrapper'],
    description='A SPARQL wrapper package for MetaNetX RDF endpoint',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=['License :: OSI Approved :: MIT License',]
)
