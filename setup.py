from setuptools import setup

setup(
    name='passgen',
    version='0.1',
    packages=['passgen'],
    test_suite='pytest',
    tests_require=['pytest'],
    url='',
    license='',
    author='Piper Thunstrom',
    author_email='pathunstrom@gmail.com',
    description='Piper\'s password generator',
    entry_points={
        "console_scripts": ["passgen=passgen:main"]
    }
)
