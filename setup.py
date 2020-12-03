import re
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("adventofcode_library/_version.py", "r") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

setup(
    name="adventofcode-library",
    version=version,
    author="Johan Niklasson",
    author_email="johan@niklasson.me",
    description="Library that downloads your input and send your results to adventofcode.com, directly from your code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vonNiklasson/adventofcode-library",
    install_requires=[
        "python-dotenv==0.15.0",
        "requests==2.25.0"
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
