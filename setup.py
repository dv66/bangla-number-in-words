import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="banglanum2words",
    version="0.0.1",
    author="Syed Mostofa Monsur",
    author_email="mostofamonsur9396@gmail.com",
    description="Converts a Bangla numeric string to literal words.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dv66/bangla-number-in-words",
    project_urls={
        "Bug Tracker": "https://github.com/dv66/bangla-number-in-words/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
		'num2words==0.5.10'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
