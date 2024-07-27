from setuptools import setup, find_packages

setup(
    name="simple_create_repo",
    version="1.1.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
        "click"
    ],
    author="diter89ahmedchiper",
    author_email="typingoflist09@gmail.com",
    description="A Python library to create GitHub repositories using GitHub API",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/diter89/simple_create_repo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'create-repo=simple_create_repo.cli:main',
        ],
    },
    python_requires='>=3.6',
)
