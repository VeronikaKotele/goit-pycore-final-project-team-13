from setuptools import setup, find_packages

setup(
    name="personal-assistant",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        # Add your dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
        ]
    },
    author="Team 13",
    description="A personal assistant bot for managing contacts and notes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)