# -*- coding: utf-8 -*-

"""
***************************************************************************
    demoReadGpkg.py
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
"""

import os
import sys 
import pandas as pd 
from geopandas import read_file
from shapely.geometry import Polygon
from datetime import datetime

script_path = os.path.dirname(__file__)
sys.path.append(os.path.join(script_path,".."))

from trajectory import Trajectory 

xmin, xmax, ymin, ymax = 116.36850352835575,116.37029459899574,39.904675309969896,39.90772814977718 
polygon = Polygon([(xmin, ymin), (xmin, ymax), (xmax, ymax), (xmax, ymin), (xmin, ymin)])
t_start = datetime.now()
df = read_file(os.path.join(script_path,'testdata_geolife.gpkg'))
df['t'] = pd.to_datetime(df['t'])
df = df.set_index('t')
#print(df)
intersections = []
for key, values in df.groupby(['trajectory_id']):
    traj = Trajectory(key, values)
    for intersection in traj.intersection(polygon):
        intersections.append(intersection)
t_end = datetime.now()        
print("Found {} intersections in {}".format(len(intersections),t_end-t_start))
