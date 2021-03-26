import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discord-logger-rewrite", # Replace with your own username
    version="0.0.1",
    author="VineyS",
    author_email="vineypsunu@gmail.com",
    description="A Rewritten Edition of discord_logger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VineyS/python_discord_logger_rewrite",
    packages=setuptools.find_packages(),
    install_requires=["discord-webhook == 0.8.0", "pyyaml == 5.4"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
