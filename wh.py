#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
wh.py

Copyright 2014 Daniel Maldonado

This file is part of WwebHardening project.

WPHardening is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

WPHardening is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with WPHardening.  If not, see <http://www.gnu.org/licenses/>.

"""
from core import show_banner
from core.api.console import Console


def main():
    show_banner()

if __name__ == "__main__":
    main()
    console = Console()
    try:
	    console.cmdloop("Hola!")
    except KeyboardInterrupt:
        console.do_quit(None)