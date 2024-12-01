from setuptools import setup, find_packages

import io

# Read README with proper encoding
with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="basilearn",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.8.1",
        "beautifulsoup4>=4.11.0",
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "setuptools>=56.0.0",
    ],
    author="Barbara Asiamah",
    author_email="barbaraasiamah99@gmail.com",
    description="A library for educational content and interactive learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education",
    ],
    python_requires=">=3.7",
    keywords="education, interactive-learning, python, library",
    
)
