from setuptools import setup, find_packages

setup(
    name="project-structure-extractor",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "Click",
    ],
    entry_points='''
        [console_scripts]
        extract-structure=project_structure_extractor.cli:cli
    ''',
    author="Hamed Haghjo",
    author_email="hamedhaghjo@hotmail.com",
    description="CLI tool to extract the structure of a project into a .txt file.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RealWorga/project-structure-extractor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)