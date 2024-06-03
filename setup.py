from pathlib import Path

from setuptools import setup

from setuptools import find_packages


INSTALL_REQUIRE = [
    "requests[socks]==2.31.0",
    "pydantic==2.6.4",
]


EXTRA_REQUIRE = {}

DOCS_PATH = Path(__file__).parents[0] / "docs/README.md"
PATH = Path("README.md")
if not PATH.exists():
    with Path.open(DOCS_PATH, encoding="utf-8") as f1:
        with Path.open(PATH, "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

setup(
    name="odibets-api",
    version="0.0.1",
    license="MIT",
    author="Smartwa",
    maintainer="Smartwa",
    author_email="simatwacaleb@proton.me",
    description="Unofficial API for Odibets in Python",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/Simatwa/odibets-api",
    project_urls={
        "Bug Report": "https://github.com/Simatwa/odibets-api/issues/new",
        "Homepage": "https://github.com/Simatwa/odibets-api",
        "Source Code": "https://github.com/Simatwa/odibets-api",
        "Issue Tracker": "https://github.com/Simatwa/odibets-api/issues",
        "Download": "https://github.com/Simatwa/odibets-api/releases",
        "Documentation": "https://github.com/Simatwa/odibets-api/blob/main/docs",
    },
    entry_points={
        "console_scripts": [
            # "odibets-api = betika_api.console:main",
        ],
    },
    install_requires=INSTALL_REQUIRE,
    extras_require=EXTRA_REQUIRE,
    python_requires=">=3.10",
    keywords=[
        "Soccer",
        "Betting",
        "Football",
        "Odibets",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: Free For Home Use",
        "Intended Audience :: Customer Service",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
