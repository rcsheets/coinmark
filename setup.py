from setuptools import setup, find_packages

setup(
    name='coinmark',
    packages=['coinmark'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    #test_suite = 'tests',
)
