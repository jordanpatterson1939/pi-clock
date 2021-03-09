import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pi-clock",
    version="1.0.1",
    scripts=["piclock"],
    author="Jordan Patterson",
    author_email="jordanpatterson1939@gmail.com",
    description="Set alarms, stopwatches and timers from the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jordanpatterson1939/pi-clock",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['playsound','getkey'],
    python_requires='>=3',
    include_package_data=True,
)
