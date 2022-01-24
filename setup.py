from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in south_africa_compliance/__init__.py
from south_africa_compliance import __version__ as version

setup(
	name="south_africa_compliance",
	version=version,
	description="ERPNext app that includes compliance settings for South Africa",
	author="Frappe Technologies Private Limited",
	author_email="diksha@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
