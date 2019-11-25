import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyparse-nfbr", 
    version="0.0.1",
    author="Sidon",
    author_email="sidoncd@gmail.com",
    description="Parse em NFebr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'xmltodict==0.12.0'
    ],
    python_requires='>=3.6',


)
