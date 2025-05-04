from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="solscan-analyzer",
    description="SolScan is a Solidity static analysis framework written in Python 3.",
    url="https://github.com/khulnasoft-lab/solscan",
    author="KhulnaSoft Lab",
    version="0.9.6",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "packaging",
        "prettytable>=3.3.0",
        "pycryptodome>=3.4.6",
        "crytic-compile>=0.3.3,<0.4.0",
        # "crytic-compile@git+https://github.com/crytic/crytic-compile.git@dev#egg=crytic-compile",
        "web3>=6.0.0",
        "eth-abi>=4.0.0",
        "eth-typing>=3.0.0",
        "eth-utils>=2.1.0",
    ],
    extras_require={
        "lint": [
            "black==22.3.0",
            "pylint==3.3.7",
        ],
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-xdist",
            "deepdiff",
            "numpy",
            "coverage[toml]",
            "filelock",
            "pytest-insta",
        ],
        "doc": [
            "pdoc",
        ],
        "dev": [
            "solscan-analyzer[lint,test,doc]",
            "openai",
        ],
    },
    license="AGPL-3.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "solscan = solscan.__main__:main",
            "solscan-check-upgradeability = solscan.tools.upgradeability.__main__:main",
            "solscan-find-paths = solscan.tools.possible_paths.__main__:main",
            "solscan-simil = solscan.tools.similarity.__main__:main",
            "solscan-flat = solscan.tools.flattening.__main__:main",
            "solscan-format = solscan.tools.solscan_format.__main__:main",
            "solscan-check-erc = solscan.tools.erc_conformance.__main__:main",
            "solscan-check-kspec = solscan.tools.kspec_coverage.__main__:main",
            "solscan-prop = solscan.tools.properties.__main__:main",
            "solscan-mutate = solscan.tools.mutator.__main__:main",
            "solscan-read-storage = solscan.tools.read_storage.__main__:main",
            "solscan-doctor = solscan.tools.doctor.__main__:main",
            "solscan-documentation = solscan.tools.documentation.__main__:main",
            "solscan-interface = solscan.tools.interface.__main__:main",
        ]
    },
)
