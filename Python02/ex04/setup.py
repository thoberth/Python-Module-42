import setuptools

setuptools.setup(
    name='my_minipack',
    version="0.0.1",
    author='Thomas BERTHET',
    author_email='thoberth@student.42.fr',
    description="How to create a package in python.",
    long_description_content_type="text/markdown",
    url="None",
    packages=setuptools.find_packages(),
    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.7',
)
