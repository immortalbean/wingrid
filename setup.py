from setuptools import setup, find_packages

setup(
    name="wingrid",
    version="0.1",
    description="A grid-based UI/windowing system for Pygame",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.7",
)