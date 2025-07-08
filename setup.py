# setup.py

from setuptools import setup, find_packages

setup(
    name="css_selector_checker",
    version="1.0.0",
    description="A CLI tool to check CSS selectors on web page.",
    author="administrator",
    packages=find_packages(),
    install_requires=[
        "playwright",
        ],
    entry_points={
        "console_scripts": [
            "css_selector_checker=css_selector_checker.locator:run", ],
        },
)
