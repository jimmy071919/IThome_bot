from setuptools import setup, find_packages

setup(
    name="ithome-bot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "line-bot-sdk",
        "python-dotenv",
        "apscheduler",
        "requests",
        "beautifulsoup4"
    ],
)
