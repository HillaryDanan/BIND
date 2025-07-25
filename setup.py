from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bind-framework",
    version="0.1.0",
    author="Hillary Danan",
    author_email="hillarydanan@gmail.com",
    description="BIND: A framework for understanding consciousness emergence at information boundaries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HillaryDanan/BIND",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "plotly>=5.0.0",
        "torch>=1.9.0",
        "pandas>=1.3.0",
        "jupyter>=1.0.0",
        "tqdm>=4.62.0",
    ],
    extras_require={
        "dev": ["pytest>=6.0", "black>=21.0", "flake8>=3.9"],
    },
)
