import os
from setuptools import setup


setup(
    version="0.2.0",
    name="dcm-preparation-module-api",
    description="api for preparation-module-containers",
    author="LZV.nrw",
    install_requires=[
    ],
    packages=[
        "dcm_preparation_module_api"
    ],
    package_data={
        "dcm_preparation_module_api": [
            "dcm_preparation_module_api/openapi.yaml",
        ],
    },
    include_package_data=True,
)
