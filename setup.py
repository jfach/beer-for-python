from distutils.core import setup

setup(
	# Application name:
	name="pybeer",

	# Version number:
	version="0.1.12",
	description="Access quality beer data through Python.",
	# Application author details:
	author="Jordan Facibene",
	author_email="jordan.facibene13@stjohns.edu",
	download_url = 'https://github.com/Jfach/beer-for-python/tarball/0.1.12',

	# Packages
	packages=["pybeer"],

	install_requires=[
		"mechanize",
	]
)