from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in promptlytics/__init__.py
from promptlytics import __version__ as version

setup(
	name="promptlytics",
	version=version,
	description="Prompt Management and Analytics Platform",
	author="Hybrowlabs Technologies",
	author_email="chinmay@hybrowlabs.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
