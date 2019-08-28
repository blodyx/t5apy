import setuptools

import t5apy


with open('README.md', 'r') as f:
    long_description = f.read()


setuptools.setup(
    name=t5apy.__name__,
    version=t5apy.__version__,
    description=t5apy.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/didadadida93/t5apy',
    author=t5apy.__author__,
    author_email=t5apy.__author_email__,
    packages=['t5apy'],
    license=t5apy.__license__,
    install_requires=[
        'mock',
    ]
    classifiers=[
        'License :: OIS Approved :: MIT License',
    ],
)
