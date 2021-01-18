import setuptools

setuptools.setup(
name="packagename",
version="0.0.2",
author="Ankit singh",
author_email="ankitsingh300307@gmail.com",
description="My package",
long_description="Long description",
long_description_content_type="text/markdown",
url="www.documnetation_or_github_url",
packages=setuptools.find_packages(),
install_requires=["pygame"],
classifiers=[ "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

],
python_requires=">2.0",

)