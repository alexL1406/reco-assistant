import setuptools

with open("README.md", "r") as fh:
    README = fh.read()

setuptools.setup(
    name="reco-assistant",
    version="0.3.0",
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
)


install_requires = [
    'pyaudio'
    'wave'
    'request'
    'text2num'
    'pydub'
]
