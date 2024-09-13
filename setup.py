# coding: utf-8

"""
    imager200 API

      Welcome to imager200! the API for image processing and image workflow automation.

    The version of the OpenAPI document: 1.0
    Contact: contact@imager200.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "imager200-python-sdk"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="bindings for interacting with the imager200 API in Python",
    author="OpenAPI Generator community",
    author_email="contact@imager200.io",
    url="",
    keywords=["imager200 API", "image processing", "OpenAPI", "OpenAPI-Generator"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
      imager200 is an API for image processing and image workflow automation. This package provides bindings for interacting with the imager200 API in Python.
    """,  # noqa: E501
    package_data={"imager200_python_sdk": ["py.typed"]},
)
