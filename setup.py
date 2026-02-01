"""
Setup script for SOMA
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="soma-vla",
    version="0.1.0",
    author="SOMA Team",
    description="Strategic Orchestration and Memory-Augmented Agentic System for Zero-Shot VLA Generalization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LZY-1021/SOMA-Strategic-Orchestration-and-Memory-Augmented-Agentic-System-for-Zero-Shot-VLA-Generalization-",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
)
