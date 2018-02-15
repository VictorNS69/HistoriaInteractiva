#!/usr/bin/env python3

__AUTHOR__ = "Victor Nieves Sanchez"
__COPYRIGHT__ = "Copyright 2018, Victor Nieves Sanchez"
__CREDITS__ = ["Victor Nieves Sanchez"]
__LICENSE__ = "GPL"
__VERSION__ = "1.0.0"
__PYTHON__= "3.6.4"
__EMAIL__ = "vnievess@gmail.com"



from setuptools import setup

setup(name='Historia Interactiva',
	version=__VERSION__,
	description='Juego interactivo.',
	author=__AUTHOR__,
	author_email=__EMAIL__,
	url='https://github.com/VictorNS69/',
	license=__LICENSE__,
	classifiers=['Programming Language :: Python :: 3.5'],
	packages=['backend', 'images'],)

