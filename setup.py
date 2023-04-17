from setuptools import setup

setup(
    name="tdpxg-instagram-profile-analyzer",
    version="1.0",
    packages=["tdpxg"],
    install_requires=[
        "instaloader",
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "tdpxg-instagram-profile-analyzer=tdpxg.tdpxg:main",
        ]
    },
)
