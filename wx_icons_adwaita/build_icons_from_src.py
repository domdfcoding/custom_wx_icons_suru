#!/usr/bin/python3
#
"""
Script to chop up SVGs into individual sizes

This takes around half an hour to run so be patient.
"""
#  
#  Based on `render-icon-theme.py` from the GNOME Project's adwaita-icon-theme
#  https://github.com/GNOME/adwaita-icon-theme
#  http://www.gnome.org
#
#  Also based on `render-bitmaps.py` from Ubuntu's Suru Icon Theme
#  https://github.com/ubuntu/yaru/blob/master/icons
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#


import os
from gnome_icon_builder import main


output_dir = "./Adwaita"

# DPI multipliers to render at
dpis = [1]


main(os.path.join('.', 'svg_src'), dpis, output_dir)
