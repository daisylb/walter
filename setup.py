from setuptools import find_packages, setup

setup(
    name='walter',
    description='My awesome project',
    url='https://gitlab.com/excitedleigh/walter/',
    author='Leigh Brenecki',
    author_email='lbrenecki@cmv.com.au',
    license='MIT',
    setup_requires=["setuptools_scm>=1.11.1"],
    use_scm_version=True,
    packages=find_packages(),
    include_package_data=True,

    install_requires=[
        'appdirs',
        'attrs',
        'begins',
    ],
    extras_require={
        'dev': [
            'pytest',
            'prospector',
            'pytest-asyncio',
            'hypothesis',
            'hypothesis-pytest',
        ]
    },
    entry_points={
        'console_scripts': ['walter=walter.cli:main.start'],
    },
)
