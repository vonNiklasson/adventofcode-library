from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="adventofcode-library",
    version="0.0.1",
    author="Johan Niklasson",
    author_email="johan@niklasson.me",
    description="Library that downloads your input and send your results to adventofcode.com, directly from your code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vonNiklasson/adventofcode-library",
    install_requires=[
        "python-dotenv==0.15.0",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires=">=3.5",
)
