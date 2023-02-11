import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def read_version(file_name):
    with open(file_name) as version:
        return version.read()


setuptools.setup(
    name="example-package",
    version=read_version("example-package/version.txt"),
    author="Tom Stanley",
    author_email="tom@ilingu.com",
    description="package description",
    long_description=long_description,
    url="",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'example-package=example_package:entry_point',
        ],
    },
    package_data={
        "": ['version.txt'],
    },
    classifiers=[],
    python_requires='>=3.6',
    install_requires=[]
)
