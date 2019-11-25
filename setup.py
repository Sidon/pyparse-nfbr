import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyparse-nfbr",
    version="0.0.1-alfa",
    author="Sidon",
    author_email="sidoncd@gmail.com",
    description="Parse em NFebr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/Sidon/pyparse-nfbr",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='==3.7.5',
)
