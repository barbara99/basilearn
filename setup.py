from setuptools import setup, find_packages

import io

# Read README with proper encoding
with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="basilearn",
    version="0.1.32",
    packages=find_packages(include=["basilearn", "basilearn.*"]),
    install_requires=[
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
    entry_points={
    'console_scripts': [
        'basilearn-run = basilearn.run:main',  
    ]
},

    
)
