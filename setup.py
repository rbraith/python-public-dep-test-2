from setuptools import setup, find_packages

setup(
    name="public-python-test-2",
    version="0.1.0",
    description="A dumb test.",
    author="Richard Braithwaite",
    author_email="r.braithwaite@live.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = [
        "public-python-test-1 @ git+https://github.com/rbraith/python-public-dep-test-1.git@v0.2.0",
    ],
)
