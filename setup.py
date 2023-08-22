from setuptools import setup, find_packages

setup(
    name='regast',
    version='0.1.0',
    description='A static analyzer for Solidity, built upon regex and ASTs.',
    author='MiloTruck',
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=['tree-sitter'],
    include_package_data=True,
    extra_requires={
        'dev': ['pytest']
    },
    entry_points={
        'console_scripts': [
            'regast=regast.__main__:main'
        ]
    },
)