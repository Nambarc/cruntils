import setuptools

setuptools.setup(
    name="cruntils",
    version="0.0.10",
    description="A collection of utilities, mainly for me.",
    author="Nambarc",
    packages=["cruntils"],
    include_package_data=True,
    package_data={"": ["EGM96_WW_15M_GH.GRD"]},
    install_requires=[
        "setuptools>=61.0",
        "pyserial>=3.5"
    ]
)