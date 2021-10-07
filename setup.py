import ast
import io
import re
import os
from setuptools import find_packages, setup


DEPENDENCIES = [
    "requests",
]
EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "tests*"]
CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()


def get_version():
    main_file = os.path.join(CURDIR, "hello_pipx", "main.py")
    _version_re = re.compile(r"__version__\s+=\s+(?P<version>.*)")
    with open(main_file, "r", encoding="utf8") as f:
        match = _version_re.search(f.read())
        version = match.group("version") if match is not None else '"unknown"'
    return str(ast.literal_eval(version))


setup(
    name="hello_pipx",
    version=get_version(),
    author="Chris Anderson",
    author_email="bogus@gmail.com",
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cva/hello_pipx",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    keywords=[],
    scripts=[],
    entry_points={"console_scripts": ["hello_pipx=hello_pipx.main:main"]},
    zip_safe=False,
    install_requires=DEPENDENCIES,
    test_suite="tests.test_project",
    python_requires=">=3.6",
    # license and classifier list:
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    license="License :: OSI Approved :: MIT License",
    classifiers=[
        "Programming Language :: Python",
        # "Programming Language :: Python :: 3",
        # "Operating System :: OS Independent",
        # "Private :: Do Not Upload"
    ],
)
