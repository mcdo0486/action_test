from setuptools import setup, find_packages

setup(
    name='action_test',
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest >= 2.9.1',
        'pytest-qt >= 2.4.0',
        'pyvisa-sim >= 0.4.0',
    ]
)