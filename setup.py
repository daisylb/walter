from os.path import dirname, join

from setuptools import find_packages, setup

setup(
    name="walter",
    description="A better configuration library for Django and other "
    "Python projects",
    long_description=open(join(dirname(__file__), "README.rst")).read(),
    url="https://gitlab.com/excitedleigh/walter/",
    author="Leigh Brenecki",
    author_email="leigh@brenecki.id.au",
    license="MIT",
    setup_requires=["setuptools_scm>=1.11.1"],
    use_scm_version=True,
    packages=find_packages(),
    include_package_data=True,
    install_requires=["appdirs", "attrs", "begins",],
    extras_require={
        "dev": [
            "pytest",
            "prospector",
            "pytest-asyncio",
            "hypothesis",
            "hypothesis-pytest",
        ],
        "docs": ["sphinx>=1.5,<1.6", "sphinx-rtd-theme>=0.1.9,<0.2",],
    },
)
