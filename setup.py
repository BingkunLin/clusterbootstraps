import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="clusterbootstraps",
    version="3.0.0",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Bank1999/clusterbootstraps",
    author="Bingkun Lin/Shiyue Shen/Ziyi Zhan/Zizhong Yan",
    author_email="linbingkun.iesr18u@foxmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["clusterbootstraps"],
    include_package_data=True,
    install_requires=["numpy", "pandas","statsmodels.api","prettytable"],
    entry_points={
        "console_scripts": [
            "Bank1999=clusterbootstraps.pair:Pair","Bank1999=clusterbootstraps.wild:Wild"
        ]
    },
)
