from setuptools import setup, find_packages

setup(
    name='mtga-sim',
    version='0.0.1',
    description="Simulates mgta board state",
    long_description="Simulates mgta board state",
    author='Edvard Englund',
    author_email='edvard.englund@medsci.uu.se',
    packages=find_packages(exclude=["tests*"]),
    entry_points={
        'console_scripts': [
            'mtga-sim = mtga_sim.cli:start'
        ]
    }
)
