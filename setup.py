import io
import os

from setuptools import setup, find_packages


VERSION = '0.0.7'
here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.rst'), encoding="utf8").read()

setup(
    name='jsx-lexer',
    description='A JSX lexer for Pygments',
    long_description=README,
    version=VERSION,
    url='https://github.com/fcurella/jsx-lexer',
    author='Flavio Curella',
    author_email='flavio.curella@gmail.com',
    classifiers=[
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    keywords='pygments highlight jsx react',
    install_requires=[
        'Pygments >= 2.1'
    ],
    test_suite='tests',
    license='MIT License',
    packages=find_packages(exclude=["docs", "tests", "tests.*"]),
    entry_points="""
        [pygments.lexers]
        jsx=jsx:JsxLexer
    """
)
