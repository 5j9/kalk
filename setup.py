from setuptools import setup
from os.path import dirname

setup(
    name='kalk',
    version='0.4.0',
    long_description=open(
        f'{dirname(__file__)}/README.rst', encoding='utf-8').read(),
    long_description_content_type='text/x-rst',
    description='a simple cli RPN calculator written in Python',
    url='https://github.com/5j9/kalk',
    author='5j9',
    author_email='5j9@users.noreply.github.com',
    license='GNU General Public License v3 (GPLv3)',
    packages=['_kalk'],
    python_requires='>=3.9',
    install_requires=['regex', 'pyperclip'],
    tests_require=['pytest'],
    entry_points={'console_scripts': ['kalk = _kalk:main']},
    zip_safe=True,
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering',
    ],
    keywords='calculator kalkulator cli RPN')
