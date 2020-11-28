import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bestpy",
    version="0.0.1",
    author="Gustav Odinger",
    description="A package to find out what's best",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gustavwilliam/bestpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
