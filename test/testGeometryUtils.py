# -*- coding: utf-8 -*-

"""
***************************************************************************
    testGeometryUtils.py
    ---------------------
    Date                 : December 2018
    Copyright            : (C) 2018 by Anita Graser
    Email                : anitagraser@gmx.at
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************

ATTENTION!
If you use OSGeo4W, you need to run the following command first:
call C:\OSGeo4W64\bin\py3_env.bat

python3 testGeometryUtils.py -v

or if you want to run all tests at once:

python3 -m unittest discover . -v

"""

import sys 
import unittest
from shapely.geometry import Point

sys.path.append("..")

from trajectory import Trajectory 
from geometryUtils import azimuth, calculate_initial_compass_bearing

 
class TestGeometryUtils(unittest.TestCase):
 
    def test_compass_bearing_east(self):
        result = calculate_initial_compass_bearing(Point(0,0), Point(10,0))
        expected_result = 90
        self.assertEqual(result, expected_result) 
        
    def test_compass_bearing_west(self):
        result = calculate_initial_compass_bearing(Point(0,0), Point(-10,0))
        expected_result = 270
        self.assertEqual(result, expected_result) 
        
    def test_compass_bearing_north(self):
        result = calculate_initial_compass_bearing(Point(0,0), Point(0,10))
        expected_result = 0
        self.assertEqual(result, expected_result) 
        
    def test_compass_bearing_south(self):
        result = calculate_initial_compass_bearing(Point(0,0), Point(0,-10))
        expected_result = 180
        self.assertEqual(result, expected_result) 
 
    def test_azimuth_east(self):
        result = azimuth(Point(0,0), Point(1,0))
        expected_result = 90
        self.assertEqual(result, expected_result)
         
        result = azimuth(Point(0,0), Point(100,0))
        expected_result = 90
        self.assertEqual(result, expected_result) 
        
    def test_azimuth_west(self):
        result = azimuth(Point(0,0), Point(-10,0))
        expected_result = 270
        self.assertEqual(result, expected_result) 
        
    def test_azimuth_north(self):
        result = azimuth(Point(0,0), Point(0,1))
        expected_result = 0
        self.assertEqual(result, expected_result) 
            
    def test_azimuth_south(self):
        result = azimuth(Point(0,0), Point(0,-1))
        expected_result = 180
        self.assertEqual(result, expected_result) 
 
    def test_azimuth_northeast(self):
        result = azimuth(Point(0,0), Point(1, 1))
        expected_result = 45
        self.assertEqual(result, expected_result) 
        
    def test_azimuth_southeast(self):
        result = azimuth(Point(0,0), Point(1, -1))
        expected_result = 135
        self.assertEqual(result, expected_result) 
        
    def test_azimuth_southwest(self):
        result = azimuth(Point(0,0), Point(-1, -1))
        expected_result = 225
        self.assertEqual(result, expected_result) 
        
    def test_azimuth_northwest(self):
        result = azimuth(Point(100,100), Point(99, 101))
        expected_result = 315
        self.assertEqual(result, expected_result) 
        
        
if __name__ == '__main__':
    unittest.main()