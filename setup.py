package_name = "escape"


if __name__ == "__main__":
    from sys import version_info as v
    from setuptools import setup, find_packages
    with open("requirements.txt") as f: requirements = f.read().splitlines()
    with open("README.md", encoding="utf8") as f: long_description = f.read()
    setup(
        name='pyescape',
        version="2019.10.16.8.31.59.29937",
        author="yehonadav",
        author_email="yonadav.barilan@gmail.com",
        description="escape characters functions and utilities",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/qaviton/escape",
        packages=[pkg for pkg in find_packages() if pkg.startswith(package_name)],
        license="apache-2.0",
        classifiers=[
            f"Programming Language :: Python :: {v[0]}.{v[1]}",
        ],
        install_requires=requirements
    )
