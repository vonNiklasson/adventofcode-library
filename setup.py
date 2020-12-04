import re
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("adventofcode/_version.py", "r") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

packages = []
for package in setuptools.find_packages():
    if not package.startswith('tests'):
        packages.append(package)

setuptools.setup(
    name="adventofcode-library",
    version=version,
    author="Johan Niklasson",
    author_email="johan@niklasson.me",
    description="Library that downloads your input and send your results to adventofcode.com, directly from your code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vonNiklasson/adventofcode-library",
    install_requires=[
        "requests==2.25.0"
    ],
    packages=packages,
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
