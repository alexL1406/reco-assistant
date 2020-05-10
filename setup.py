import setuptools

with open("README.md", "r") as fh:
    README = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

install_requires = required

setuptools.setup(
    name="reco-assistant",
    version="0.4.0",
    author="alexL1406",
    author_email="leurent.alexis@gmail.com",
    description="Reco-Assistant",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    install_requires=install_requires
)
