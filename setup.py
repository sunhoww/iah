from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in iah/__init__.py
from iah import __version__ as version

setup(
	name="iah",
	version=version,
	description="Customizations for IAH",
	author="Libermatic",
	author_email="info@libermatic.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
