from setuptools import setup

__version__ = "1.0.0"

setup(
    name="noop-storage-provider",
    version=__version__,
    zip_safe=False,
    author="michaelkaye",
    description="A storage provider that does nothing.",
    url="https://github.com/michaelkaye/noop-synapse-storage-provider",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    py_modules=["noop_storage_provider"],
    install_requires=[
    ],
)
