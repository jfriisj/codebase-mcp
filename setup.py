from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="codebase-mcp",
    version="0.1.0",
    description="A codebase management tool with a FastAPI backend and an MCP server.",
    author="jfriisj",
    author_email="",
    url="https://github.com/jfriisj/codebase-mcp",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "codebase-mcp-server=main:main",
            "codebase-mcp-mcp=mcp_server:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
