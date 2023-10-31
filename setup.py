from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in site_management/__init__.py
from site_management import __version__ as version

setup(
	name="site_management",
	version=version,
	description="site mangement system",
	author="rachana",
	author_email="rachanavarade1998@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
