import os
import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

soundfiles = os.listdir('./sounds')
for i in range(len(soundfiles)):
    soundfiles[i] = 'sounds/'+soundfiles[i]

setuptools.setup(
    name="pi-clock",
    version="1.0.6",
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
    # package_dir={'pi-clock':'./'},
    # package_data={'pi-clock':soundfiles},
    data_files=[('sounds',soundfiles)],
    # zip_safe=False,
)
