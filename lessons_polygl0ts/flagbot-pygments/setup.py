import setuptools

setuptools.setup(
    name="flagbot-pygments", # Replace with your own username
    version="0.0.1",
    author="Leonardo Galli",
    author_email="leonardo.galli@vis.ethz.ch",
    description="Custom Theme for our Lessons",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://gitlab.ethz.ch/vis/ctf/lessons",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "pygments.styles": "flagbot=flagbot:Flagbot"
    },
    
)