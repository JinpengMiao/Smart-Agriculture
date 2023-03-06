#!/usr/bin/python3

import time
import math
# import pandas as pd
import csv
import os

# Map 'area#' to location which represented with 'x' and 'y' coodinates
# area# = :
#   non-overlapped area : “side#-sensor#” 
#   overlapped area : “side#" + "-"" + "sensor_1#” + "-" + “sensor_2#” 
# mapping #4:
area_angel = {
            'A-1' : {'x': 0, 'y': 3.5}, 
            'A-1-2' : {'x': 1.25, 'y': 4}, 
            'A-2-1' : {'x': 1.25, 'y': 4},
            'A-2' : {'x': 2.5, 'y': 3.5}, 
            'A-2-3' : {'x': 3.75, 'y': 4},
            'A-3-2' : {'x': 3.75, 'y': 4}, 
            'A-3' : {'x': 5, 'y': 3.5}, 
            'A-3-4' : {'x': 6.25, 'y': 4}, 
            'A-4-3' : {'x': 6.25, 'y': 4},
            'A-4' : {'x': 7.5, 'y': 3.5}, 
            'A-4-5' : {'x': 8.75, 'y': 4},
            'A-5-4' : {'x': 8.75, 'y': 4}, 
            'A-5' : {'x': 10, 'y': 3.5}, 
            'A-5-6' : {'x': 11.25, 'y': 4}, 
            'A-6-5' : {'x': 11.25, 'y': 4},
            'A-6' : {'x': 12.5, 'y': 3.5}, 
            'A-6-7' : {'x': 13.75, 'y': 4},
            'A-7-6' : {'x': 13.75, 'y': 4},
            'A-7' : {'x': 15, 'y': 3.5}, 
            'A-7-8' : {'x': 16.25, 'y': 4}, 
            'A-8-7' : {'x': 16.25, 'y': 4},
            'A-8' : {'x': 17.5, 'y': 3.5}, 
            'A-8-9' : {'x': 18.75, 'y': 4},
            'A-9-8' : {'x': 18.75, 'y': 4}, 
            'A-9' : {'x': 20, 'y': 3.5}, 
            'A-9-10' : {'x': 21.25, 'y': 4}, 
            'A-10-9' : {'x': 21.25, 'y': 4},
            'A-10' : {'x': 22.5, 'y': 3.5}, 
            'A-10-11' : {'x': 23.75, 'y': 4},
            'A-11-10' : {'x': 23.75, 'y': 4},
            'A-11' : {'x': 25, 'y': 3.5}, 
            'A-1-2-3' : {'x': 2.5, 'y': 7},
            'A-1-3-2' : {'x': 2.5, 'y': 7},
            'A-2-1-3' : {'x': 2.5, 'y': 7},
            'A-2-3-1' : {'x': 2.5, 'y': 7},
            'A-3-1-2' : {'x': 2.5, 'y': 7},
            'A-3-2-1' : {'x': 2.5, 'y': 7},
            'A-4-2-3' : {'x': 5, 'y': 7},
            'A-4-3-2' : {'x': 5, 'y': 7},
            'A-2-4-3' : {'x': 5, 'y': 7},
            'A-2-3-4' : {'x': 5, 'y': 7},
            'A-3-4-2' : {'x': 5, 'y': 7},
            'A-3-2-4' : {'x': 5, 'y': 7},
            'A-4-5-3' : {'x': 7.5, 'y': 7},
            'A-4-3-5' : {'x': 7.5, 'y': 7},
            'A-5-4-3' : {'x': 7.5, 'y': 7},
            'A-5-3-4' : {'x': 7.5, 'y': 7},
            'A-3-4-5' : {'x': 7.5, 'y': 7},
            'A-3-5-4' : {'x': 7.5, 'y': 7},
            'A-4-5-6' : {'x': 10, 'y': 7},
            'A-4-6-5' : {'x': 10, 'y': 7},
            'A-5-4-6' : {'x': 10, 'y': 7},
            'A-5-6-4' : {'x': 10, 'y': 7},
            'A-6-4-5' : {'x': 10, 'y': 7},
            'A-6-5-4' : {'x': 10, 'y': 7},
            'A-7-5-6' : {'x': 12.5, 'y': 7},
            'A-7-6-5' : {'x': 12.5, 'y': 7},
            'A-5-7-6' : {'x': 12.5, 'y': 7},
            'A-5-6-7' : {'x': 12.5, 'y': 7},
            'A-6-7-5' : {'x': 12.5, 'y': 7},
            'A-6-5-7' : {'x': 12.5, 'y': 7},
            'A-7-8-6' : {'x': 15, 'y': 7},
            'A-7-6-8' : {'x': 15, 'y': 7},
            'A-8-7-6' : {'x': 15, 'y': 7},
            'A-8-6-7' : {'x': 15, 'y': 7},
            'A-6-7-8' : {'x': 15, 'y': 7},
            'A-6-8-7' : {'x': 15, 'y': 7},
            'A-7-8-9' : {'x': 17.5, 'y': 7},
            'A-7-9-8' : {'x': 17.5, 'y': 7},
            'A-8-7-9' : {'x': 17.5, 'y': 7},
            'A-8-9-7' : {'x': 17.5, 'y': 7},
            'A-9-7-8' : {'x': 17.5, 'y': 7},
            'A-9-8-7' : {'x': 17.5, 'y': 7},
            'A-10-8-9' : {'x': 20, 'y': 7},
            'A-10-9-8' : {'x': 20, 'y': 7},
            'A-8-10-9' : {'x': 20, 'y': 7},
            'A-8-9-10' : {'x': 20, 'y': 7},
            'A-9-10-8' : {'x': 20, 'y': 7},
            'A-9-8-10' : {'x': 20, 'y': 7},
            'A-10-11-9' : {'x': 22.5, 'y': 7},
            'A-10-9-11' : {'x': 22.5, 'y': 7},
            'A-11-10-9' : {'x': 22.5, 'y': 7},
            'A-11-9-10' : {'x': 22.5, 'y': 7},
            'A-9-10-11' : {'x': 22.5, 'y': 7},
            'A-9-11-10' : {'x': 22.5, 'y': 7},
            
            'B-1' : {'x': 0, 'y': 3.5}, 
            'B-1-2' : {'x': 1.25, 'y': 4}, 
            'B-2-1' : {'x': 1.25, 'y': 4},
            'B-2' : {'x': 2.5, 'y': 3.5}, 
            'B-2-3' : {'x': 3.75, 'y': 4},
            'B-3-2' : {'x': 3.75, 'y': 4}, 
            'B-3' : {'x': 5, 'y': 3.5}, 
            'B-3-4' : {'x': 6.25, 'y': 4}, 
            'B-4-3' : {'x': 6.25, 'y': 4},
            'B-4' : {'x': 7.5, 'y': 3.5}, 
            'B-4-5' : {'x': 8.75, 'y': 4},
            'B-5-4' : {'x': 8.75, 'y': 4}, 
            'B-5' : {'x': 10, 'y': 3.5}, 
            'B-5-6' : {'x': 11.25, 'y': 4}, 
            'B-6-5' : {'x': 11.25, 'y': 4},
            'B-6' : {'x': 12.5, 'y': 3.5}, 
            'B-6-7' : {'x': 13.75, 'y': 4},
            'B-7-6' : {'x': 13.75, 'y': 4},
            'B-7' : {'x': 15, 'y': 3.5}, 
            'B-7-8' : {'x': 16.25, 'y': 4}, 
            'B-8-7' : {'x': 16.25, 'y': 4},
            'B-8' : {'x': 17.5, 'y': 3.5}, 
            'B-8-9' : {'x': 18.75, 'y': 4},
            'B-9-8' : {'x': 18.75, 'y': 4}, 
            'B-9' : {'x': 20, 'y': 3.5}, 
            'B-9-10' : {'x': 21.25, 'y': 4}, 
            'B-10-9' : {'x': 21.25, 'y': 4},
            'B-10' : {'x': 22.5, 'y': 3.5}, 
            'B-10-11' : {'x': 23.75, 'y': 4},
            'B-11-10' : {'x': 23.75, 'y': 4},
            'B-11' : {'x': 25, 'y': 3.5}, 
            'B-1-2-3' : {'x': 2.5, 'y': 7},
            'B-1-3-2' : {'x': 2.5, 'y': 7},
            'B-2-1-3' : {'x': 2.5, 'y': 7},
            'B-2-3-1' : {'x': 2.5, 'y': 7},
            'B-3-1-2' : {'x': 2.5, 'y': 7},
            'B-3-2-1' : {'x': 2.5, 'y': 7},
            'B-4-2-3' : {'x': 5, 'y': 7},
            'B-4-3-2' : {'x': 5, 'y': 7},
            'B-2-4-3' : {'x': 5, 'y': 7},
            'B-2-3-4' : {'x': 5, 'y': 7},
            'B-3-4-2' : {'x': 5, 'y': 7},
            'B-3-2-4' : {'x': 5, 'y': 7},
            'B-4-5-3' : {'x': 7.5, 'y': 7},
            'B-4-3-5' : {'x': 7.5, 'y': 7},
            'B-5-4-3' : {'x': 7.5, 'y': 7},
            'B-5-3-4' : {'x': 7.5, 'y': 7},
            'B-3-4-5' : {'x': 7.5, 'y': 7},
            'B-3-5-4' : {'x': 7.5, 'y': 7},
            'B-4-5-6' : {'x': 10, 'y': 7},
            'B-4-6-5' : {'x': 10, 'y': 7},
            'B-5-4-6' : {'x': 10, 'y': 7},
            'B-5-6-4' : {'x': 10, 'y': 7},
            'B-6-4-5' : {'x': 10, 'y': 7},
            'B-6-5-4' : {'x': 10, 'y': 7},
            'B-7-5-6' : {'x': 12.5, 'y': 7},
            'B-7-6-5' : {'x': 12.5, 'y': 7},
            'B-5-7-6' : {'x': 12.5, 'y': 7},
            'B-5-6-7' : {'x': 12.5, 'y': 7},
            'B-6-7-5' : {'x': 12.5, 'y': 7},
            'B-6-5-7' : {'x': 12.5, 'y': 7},
            'B-7-8-6' : {'x': 15, 'y': 7},
            'B-7-6-8' : {'x': 15, 'y': 7},
            'B-8-7-6' : {'x': 15, 'y': 7},
            'B-8-6-7' : {'x': 15, 'y': 7},
            'B-6-7-8' : {'x': 15, 'y': 7},
            'B-6-8-7' : {'x': 15, 'y': 7},
            'B-7-8-9' : {'x': 17.5, 'y': 7},
            'B-7-9-8' : {'x': 17.5, 'y': 7},
            'B-8-7-9' : {'x': 17.5, 'y': 7},
            'B-8-9-7' : {'x': 17.5, 'y': 7},
            'B-9-7-8' : {'x': 17.5, 'y': 7},
            'B-9-8-7' : {'x': 17.5, 'y': 7},
            'B-10-8-9' : {'x': 20, 'y': 7},
            'B-10-9-8' : {'x': 20, 'y': 7},
            'B-8-10-9' : {'x': 20, 'y': 7},
            'B-8-9-10' : {'x': 20, 'y': 7},
            'B-9-10-8' : {'x': 20, 'y': 7},
            'B-9-8-10' : {'x': 20, 'y': 7},
            'B-10-11-9' : {'x': 22.5, 'y': 7},
            'B-10-9-11' : {'x': 22.5, 'y': 7},
            'B-11-10-9' : {'x': 22.5, 'y': 7},
            'B-11-9-10' : {'x': 22.5, 'y': 7},
            'B-9-10-11' : {'x': 22.5, 'y': 7},
            'B-9-11-10' : {'x': 22.5, 'y': 7},
            
            'C-1' : {'x': 0, 'y': 3.5}, 
            'C-1-2' : {'x': 1.25, 'y': 4}, 
            'C-2-1' : {'x': 1.25, 'y': 4},
            'C-2' : {'x': 2.5, 'y': 3.5}, 
            'C-2-3' : {'x': 3.75, 'y': 4},
            'C-3-2' : {'x': 3.75, 'y': 4}, 
            'C-3' : {'x': 5, 'y': 3.5}, 
            'C-3-4' : {'x': 6.25, 'y': 4}, 
            'C-4-3' : {'x': 6.25, 'y': 4},
            'C-4' : {'x': 7.5, 'y': 3.5}, 
            'C-4-5' : {'x': 8.75, 'y': 4},
            'C-5-4' : {'x': 8.75, 'y': 4}, 
            'C-5' : {'x': 10, 'y': 3.5}, 
            'C-5-6' : {'x': 11.25, 'y': 4}, 
            'C-6-5' : {'x': 11.25, 'y': 4},
            'C-6' : {'x': 12.5, 'y': 3.5}, 
            'C-6-7' : {'x': 13.75, 'y': 4},
            'C-7-6' : {'x': 13.75, 'y': 4},
            'C-7' : {'x': 15, 'y': 3.5}, 
            'C-7-8' : {'x': 16.25, 'y': 4}, 
            'C-8-7' : {'x': 16.25, 'y': 4},
            'C-8' : {'x': 17.5, 'y': 3.5}, 
            'C-8-9' : {'x': 18.75, 'y': 4},
            'C-9-8' : {'x': 18.75, 'y': 4}, 
            'C-9' : {'x': 20, 'y': 3.5}, 
            'C-9-10' : {'x': 21.25, 'y': 4}, 
            'C-10-9' : {'x': 21.25, 'y': 4},
            'C-10' : {'x': 22.5, 'y': 3.5}, 
            'C-10-11' : {'x': 23.75, 'y': 4},
            'C-11-10' : {'x': 23.75, 'y': 4},
            'C-11' : {'x': 25, 'y': 3.5}, 
            'C-1-2-3' : {'x': 2.5, 'y': 7},
            'C-1-3-2' : {'x': 2.5, 'y': 7},
            'C-2-1-3' : {'x': 2.5, 'y': 7},
            'C-2-3-1' : {'x': 2.5, 'y': 7},
            'C-3-1-2' : {'x': 2.5, 'y': 7},
            'C-3-2-1' : {'x': 2.5, 'y': 7},
            'C-4-2-3' : {'x': 5, 'y': 7},
            'C-4-3-2' : {'x': 5, 'y': 7},
            'C-2-4-3' : {'x': 5, 'y': 7},
            'C-2-3-4' : {'x': 5, 'y': 7},
            'C-3-4-2' : {'x': 5, 'y': 7},
            'C-3-2-4' : {'x': 5, 'y': 7},
            'C-4-5-3' : {'x': 7.5, 'y': 7},
            'C-4-3-5' : {'x': 7.5, 'y': 7},
            'C-5-4-3' : {'x': 7.5, 'y': 7},
            'C-5-3-4' : {'x': 7.5, 'y': 7},
            'C-3-4-5' : {'x': 7.5, 'y': 7},
            'C-3-5-4' : {'x': 7.5, 'y': 7},
            'C-4-5-6' : {'x': 10, 'y': 7},
            'C-4-6-5' : {'x': 10, 'y': 7},
            'C-5-4-6' : {'x': 10, 'y': 7},
            'C-5-6-4' : {'x': 10, 'y': 7},
            'C-6-4-5' : {'x': 10, 'y': 7},
            'C-6-5-4' : {'x': 10, 'y': 7},
            'C-7-5-6' : {'x': 12.5, 'y': 7},
            'C-7-6-5' : {'x': 12.5, 'y': 7},
            'C-5-7-6' : {'x': 12.5, 'y': 7},
            'C-5-6-7' : {'x': 12.5, 'y': 7},
            'C-6-7-5' : {'x': 12.5, 'y': 7},
            'C-6-5-7' : {'x': 12.5, 'y': 7},
            'C-7-8-6' : {'x': 15, 'y': 7},
            'C-7-6-8' : {'x': 15, 'y': 7},
            'C-8-7-6' : {'x': 15, 'y': 7},
            'C-8-6-7' : {'x': 15, 'y': 7},
            'C-6-7-8' : {'x': 15, 'y': 7},
            'C-6-8-7' : {'x': 15, 'y': 7},
            'C-7-8-9' : {'x': 17.5, 'y': 7},
            'C-7-9-8' : {'x': 17.5, 'y': 7},
            'C-8-7-9' : {'x': 17.5, 'y': 7},
            'C-8-9-7' : {'x': 17.5, 'y': 7},
            'C-9-7-8' : {'x': 17.5, 'y': 7},
            'C-9-8-7' : {'x': 17.5, 'y': 7},
            'C-10-8-9' : {'x': 20, 'y': 7},
            'C-10-9-8' : {'x': 20, 'y': 7},
            'C-8-10-9' : {'x': 20, 'y': 7},
            'C-8-9-10' : {'x': 20, 'y': 7},
            'C-9-10-8' : {'x': 20, 'y': 7},
            'C-9-8-10' : {'x': 20, 'y': 7},
            'C-10-11-9' : {'x': 22.5, 'y': 7},
            'C-10-9-11' : {'x': 22.5, 'y': 7},
            'C-11-10-9' : {'x': 22.5, 'y': 7},
            'C-11-9-10' : {'x': 22.5, 'y': 7},
            'C-9-10-11' : {'x': 22.5, 'y': 7},
            'C-9-11-10' : {'x': 22.5, 'y': 7},    

            'D-1' : {'x': 0, 'y': 3.5}, 
            'D-1-2' : {'x': 1.25, 'y': 4}, 
            'D-2-1' : {'x': 1.25, 'y': 4},
            'D-2' : {'x': 2.5, 'y': 3.5}, 
            'D-2-3' : {'x': 3.75, 'y': 4},
            'D-3-2' : {'x': 3.75, 'y': 4}, 
            'D-3' : {'x': 5, 'y': 3.5}, 
            'D-3-4' : {'x': 6.25, 'y': 4}, 
            'D-4-3' : {'x': 6.25, 'y': 4},
            'D-4' : {'x': 7.5, 'y': 3.5}, 
            'D-4-5' : {'x': 8.75, 'y': 4},
            'D-5-4' : {'x': 8.75, 'y': 4}, 
            'D-5' : {'x': 10, 'y': 3.5}, 
            'D-5-6' : {'x': 11.25, 'y': 4}, 
            'D-6-5' : {'x': 11.25, 'y': 4},
            'D-6' : {'x': 12.5, 'y': 3.5}, 
            'D-6-7' : {'x': 13.75, 'y': 4},
            'D-7-6' : {'x': 13.75, 'y': 4},
            'D-7' : {'x': 15, 'y': 3.5}, 
            'D-7-8' : {'x': 16.25, 'y': 4}, 
            'D-8-7' : {'x': 16.25, 'y': 4},
            'D-8' : {'x': 17.5, 'y': 3.5}, 
            'D-8-9' : {'x': 18.75, 'y': 4},
            'D-9-8' : {'x': 18.75, 'y': 4}, 
            'D-9' : {'x': 20, 'y': 3.5}, 
            'D-9-10' : {'x': 21.25, 'y': 4}, 
            'D-10-9' : {'x': 21.25, 'y': 4},
            'D-10' : {'x': 22.5, 'y': 3.5}, 
            'D-10-11' : {'x': 23.75, 'y': 4},
            'D-11-10' : {'x': 23.75, 'y': 4},
            'D-11' : {'x': 25, 'y': 3.5}, 
            'D-1-2-3' : {'x': 2.5, 'y': 7},
            'D-1-3-2' : {'x': 2.5, 'y': 7},
            'D-2-1-3' : {'x': 2.5, 'y': 7},
            'D-2-3-1' : {'x': 2.5, 'y': 7},
            'D-3-1-2' : {'x': 2.5, 'y': 7},
            'D-3-2-1' : {'x': 2.5, 'y': 7},
            'D-4-2-3' : {'x': 5, 'y': 7},
            'D-4-3-2' : {'x': 5, 'y': 7},
            'D-2-4-3' : {'x': 5, 'y': 7},
            'D-2-3-4' : {'x': 5, 'y': 7},
            'D-3-4-2' : {'x': 5, 'y': 7},
            'D-3-2-4' : {'x': 5, 'y': 7},
            'D-4-5-3' : {'x': 7.5, 'y': 7},
            'D-4-3-5' : {'x': 7.5, 'y': 7},
            'D-5-4-3' : {'x': 7.5, 'y': 7},
            'D-5-3-4' : {'x': 7.5, 'y': 7},
            'D-3-4-5' : {'x': 7.5, 'y': 7},
            'D-3-5-4' : {'x': 7.5, 'y': 7},
            'D-4-5-6' : {'x': 10, 'y': 7},
            'D-4-6-5' : {'x': 10, 'y': 7},
            'D-5-4-6' : {'x': 10, 'y': 7},
            'D-5-6-4' : {'x': 10, 'y': 7},
            'D-6-4-5' : {'x': 10, 'y': 7},
            'D-6-5-4' : {'x': 10, 'y': 7},
            'D-7-5-6' : {'x': 12.5, 'y': 7},
            'D-7-6-5' : {'x': 12.5, 'y': 7},
            'D-5-7-6' : {'x': 12.5, 'y': 7},
            'D-5-6-7' : {'x': 12.5, 'y': 7},
            'D-6-7-5' : {'x': 12.5, 'y': 7},
            'D-6-5-7' : {'x': 12.5, 'y': 7},
            'D-7-8-6' : {'x': 15, 'y': 7},
            'D-7-6-8' : {'x': 15, 'y': 7},
            'D-8-7-6' : {'x': 15, 'y': 7},
            'D-8-6-7' : {'x': 15, 'y': 7},
            'D-6-7-8' : {'x': 15, 'y': 7},
            'D-6-8-7' : {'x': 15, 'y': 7},
            'D-7-8-9' : {'x': 17.5, 'y': 7},
            'D-7-9-8' : {'x': 17.5, 'y': 7},
            'D-8-7-9' : {'x': 17.5, 'y': 7},
            'D-8-9-7' : {'x': 17.5, 'y': 7},
            'D-9-7-8' : {'x': 17.5, 'y': 7},
            'D-9-8-7' : {'x': 17.5, 'y': 7},
            'D-10-8-9' : {'x': 20, 'y': 7},
            'D-10-9-8' : {'x': 20, 'y': 7},
            'D-8-10-9' : {'x': 20, 'y': 7},
            'D-8-9-10' : {'x': 20, 'y': 7},
            'D-9-10-8' : {'x': 20, 'y': 7},
            'D-9-8-10' : {'x': 20, 'y': 7},
            'D-10-11-9' : {'x': 22.5, 'y': 7},
            'D-10-9-11' : {'x': 22.5, 'y': 7},
            'D-11-10-9' : {'x': 22.5, 'y': 7},
            'D-11-9-10' : {'x': 22.5, 'y': 7},
            'D-9-10-11' : {'x': 22.5, 'y': 7},
            'D-9-11-10' : {'x': 22.5, 'y': 7}}

edge_to_camera = 0      # time spent for transmission from edge to camera
time_threshold = 120    # 120 sec is the threshold, refresh the record - treat it as a new animal
time_tolerance = 0.1    # < 0.1: same timestamp as the previous reading

# Store two previous readings: 
#   - One is the previous reading(possibly simultaneous reading; 
#   - The other is the reading before the previous reading , i.e. backup reading 
#     (in case there is one pair of simultaneous readings)
pre_time_1 = -1000
pre_x_1 = -1
pre_y_1 = -1
pre_side_1 = '-'
pre_sensor_1 = '-'
pre_time_2 = -1000
pre_x_2 = -1
pre_y_2 = -1
pre_side_2 = '-'
pre_sensor_2 = '-'
pre_time_3 = -1000
pre_x_3 = -1
pre_y_3 = -1
pre_side_3 = '-'
pre_sensor_3 = '-'
start_time = 0
field_length = 25
half_length = 12.5

# locate the animal based on the readings
#   - cur_side: which side of four sides of the fields('A', 'B', 'C', 'D') where the animal is
#   - cur_sensor: the sensor number which detected the animal
#   - cur_time: the time when sensor detected the animal, used to determine if it is a new animal (compared with the threshold, 120 seconds)
def locate_and_predict(cur_side, cur_sensor, cur_time, next_time, filename, counter):
    global edge_to_camera
    global time_threshold
    global time_tolerance  
    global pre_time_1
    global pre_x_1
    global pre_y_1
    global pre_side_1
    global pre_sensor_1
    global pre_time_2
    global pre_x_2
    global pre_y_2
    global pre_side_2
    global pre_sensor_2
    global pre_time_3
    global pre_x_3
    global pre_y_3
    global pre_side_3
    global pre_sensor_3
    global start_time
    
    correct_prev_predict = False
    animal_x = 0
    animal_y = 0
    animal_speed = 0
    # atan2 value, i.e. 2-argument arctangent: the angle in the plane (in radians) between the positive x-axis and the ray from (0, 0) to the point (x, y)
    animal_direction = 0    # (-180, 180]      
    angle = 0   # (-pi, pi]
    
    time_passing = cur_time - pre_time_1
    # the animal was detected at the first time
    if time_passing > time_threshold:
        area_number = cur_side + '-' + cur_sensor
        animal_x = area_angel[area_number]['x']
        animal_y = area_angel[area_number]['y']
        pre_time_1 = cur_time
        pre_x_1 = animal_x
        pre_y_1 = animal_y    
        pre_side_1 = cur_side
        pre_sensor_1 = cur_sensor
    # the animal was residing in an overlapped area
    elif time_passing < time_tolerance:   
        correct_prev_predict = True 
        area_number = cur_side + '-' + cur_sensor + '-' + pre_sensor_1  
        if cur_time - pre_time_2 < time_tolerance:
            area_number = area_number + '-' + pre_sensor_2
            animal_x = area_angel[area_number]['x']
            animal_y = area_angel[area_number]['y']
            # in case the animal stepped into an overlapped area at the very first time: speed is 0, no direction
            if pre_time_3 != -1000:
                # if the animal stepped into two different sides, update the relative coodinate
                if ord(pre_side_1) - ord(pre_side_3) == 1 or ord(pre_side_1) - ord(pre_side_3) == -3:
                    temp_x = pre_x_3
                    pre_x_3 = -pre_y_3
                    pre_y_3 = field_length - temp_x
                elif ord(pre_side_1) - ord(pre_side_3) == 2 or ord(pre_side_1) - ord(pre_side_3) == -2:
                    pre_x_3 = field_length - pre_x_3
                    pre_y_3 = -field_length - pre_y_3
                elif ord(pre_side_1) - ord(pre_side_3) == 3 or ord(pre_side_1) - ord(pre_side_3) == -1:
                    temp_x = pre_x_3
                    pre_x_3 = field_length + pre_y_3
                    pre_y_3 = -temp_x              
                x_offset = animal_x - pre_x_3
                y_offset = animal_y - pre_y_3
                move_dist = math.sqrt((x_offset) * (x_offset) + (y_offset) * (y_offset))
                animal_speed = move_dist / (pre_time_1 - pre_time_3)
                angle = math.atan2(y_offset, x_offset) 
                animal_direction = angle * 180 / math.pi
        else:
            if area_number in area_angel.keys():
                animal_x = area_angel[area_number]['x']
                animal_y = area_angel[area_number]['y']
                # in case the animal stepped into an overlapped area at the very first time: speed is 0, no direction
                if pre_time_2 != -1000:
                    # if the animal stepped into two different sides, update the relative coodinate
                    if ord(pre_side_1) - ord(pre_side_2) == 1 or ord(pre_side_1) - ord(pre_side_2) == -3:
                        temp_x = pre_x_2
                        pre_x_2 = -pre_y_2
                        pre_y_2 = field_length - temp_x
                    elif ord(pre_side_1) - ord(pre_side_2) == 2 or ord(pre_side_1) - ord(pre_side_2) == -2:
                        pre_x_2 = field_length - pre_x_2
                        pre_y_2 = -field_length - pre_y_2
                    elif ord(pre_side_1) - ord(pre_side_2) == 3 or ord(pre_side_1) - ord(pre_side_2) == -1:
                        temp_x = pre_x_2
                        pre_x_2 = field_length + pre_y_2
                        pre_y_2 = -temp_x              
                    x_offset = animal_x - pre_x_2
                    y_offset = animal_y - pre_y_2
                    move_dist = math.sqrt((x_offset) * (x_offset) + (y_offset) * (y_offset))
                    animal_speed = move_dist / (pre_time_1 - pre_time_2)
                    angle = math.atan2(y_offset, x_offset) 
                    animal_direction = angle * 180 / math.pi
        pre_side_3 = pre_side_2
        pre_time_3 = pre_time_2
        pre_x_3 = pre_x_2
        pre_y_3 = pre_y_2
        pre_sensor_3 = pre_sensor_2
        pre_side_2 = pre_side_1
        pre_time_2 = pre_time_1
        pre_x_2 = pre_x_1
        pre_y_2 = pre_y_1
        pre_sensor_2 = pre_sensor_1
        pre_side_1 = cur_side
        pre_time_1 = cur_time
        pre_x_1 = animal_x
        pre_y_1 = animal_y
        pre_sensor_1 = cur_sensor
    # the same animal moved to non-overlapped area
    else:
        area_number = cur_side + '-' + cur_sensor
        animal_x = area_angel[area_number]['x']
        animal_y = area_angel[area_number]['y']
        pre_x = 0
        pre_y = 0
        if cur_side == pre_side_1:
            pre_x = pre_x_1
            pre_y = pre_y_1
        # if the animal stepped into two different sides, update the relative coodinate
        if ord(cur_side) - ord(pre_side_1) == 1 or ord(cur_side) - ord(pre_side_1) == -3:
            temp_x = pre_x
            pre_x = -pre_y
            pre_y = field_length - temp_x
        elif ord(cur_side) - ord(pre_side_1) == 2 or ord(cur_side) - ord(pre_side_1) == -2:
            pre_x = field_length - pre_x
            pre_y = -field_length - pre_y
        elif ord(cur_side) - ord(pre_side_1) == 3 or ord(cur_side) - ord(pre_side_1) == -1:
            temp_x = pre_x
            pre_x = field_length + pre_y
            pre_y = -temp_x
        x_offset = animal_x - pre_x
        y_offset = animal_y - pre_y
        move_dist = math. sqrt((x_offset) * (x_offset) + (y_offset) * (y_offset))
        animal_speed = move_dist / (cur_time - pre_time_1)
        angle = math.atan2(y_offset, x_offset) 
        animal_direction = angle * 180 / math.pi
        pre_side_2 = pre_side_1
        pre_time_2 = pre_time_1
        pre_x_2 = pre_x_1
        pre_y_2 = pre_y_1
        pre_sensor_2 = pre_sensor_1
        pre_side_1 = cur_side
        pre_time_1 = cur_time
        pre_x_1 = animal_x
        pre_y_1 = animal_y
        pre_sensor_1 = cur_sensor

    # predict the animal based on the direction and location, relative to the origin of the same side
    if animal_speed != 0:
        t = next_time
        latency = t + edge_to_camera - cur_time
        dist = latency * animal_speed
        predict_x = animal_x + dist * math.cos(angle)
        predict_y = animal_y + dist * math.sin(angle)
        predict_side = cur_side
        # the animal is predicted to be inside the field
        if 0 < predict_x < field_length and -field_length < predict_y < 0:
            if predict_x > half_length and predict_y > -half_length:
                temp_side = chr(ord(cur_side) + 1)
                predict_side = temp_side if temp_side < 'E' else (chr(ord(temp_side) - 4))
                temp_yy = predict_y
                predict_y = field_length - predict_x
                predict_x = -temp_yy 
            elif predict_x > half_length and predict_y <= -half_length:
                temp_side = chr(ord(cur_side) + 2)
                predict_side = temp_side if temp_side < 'E' else (chr(ord(temp_side) - 4))
                predict_x = field_length - predict_x
                predict_y = field_length + predict_y  
            elif predict_x <= half_length and predict_y < -half_length:
                temp_side = chr(ord(cur_side) + 3)
                predict_side = temp_side if temp_side < 'E' else (chr(ord(temp_side) - 4))
                temp_yy = predict_y
                predict_y = predict_x
                predict_x = field_length + temp_yy                  
            else:
                predict_y = -predict_y
                
            # print("""
            #     The animal was residing at: side %c. From corner %c, walk %3.2f meters to the right and then %3.2f meters out of the field; 
            #     Running speed is: %3.2f m/s; 
            #     Running direction in degree is: %3d, relative to boundary of side %c;
            #     WARNING: The animal is predicted to be inside the field, close to corner %c! From corner %c, walk %3.2f meters to the right and then %3.2f meters into the field.
            #     """ 
            #     % (cur_side, cur_side, animal_x, animal_y, animal_speed, cur_side, animal_direction, predict_side, predict_side, predict_x, predict_y))
            processing_time = time.time() - start_time
            print("------------------------------------Separate Line-------------------------------------")
            print("Time spent on prediction: %.9f" %(processing_time))
            if correct_prev_predict:
                # print("Correction: WARNING: The animal is predicted to be inside the field, close to corner %c! From corner %c, walk %3.2f meters to the right and then %3.2f meters into the field. Filename: %s; Line#: %d" % (predict_side, predict_side, predict_x, predict_y, filename, counter))
                print("Correction: WARNING: Corner %c - (%3.2f, %3.2f); Filename: %s; Line#: %d" % (predict_side, predict_x, -predict_y, filename, counter))
            else:
                print("WARNING: Corner %c - (%3.2f, %3.2f); Filename: %s; Line#: %d" % (predict_side, predict_x, -predict_y, filename, counter))
                # print("WARNING: The animal is predicted to be inside the field, close to corner %c! From corner %c, walk %3.2f meters to the right and then %3.2f meters into the field. Filename: %s; Line#: %d" % (predict_side, predict_side, predict_x, predict_y, filename, counter))
        else:
            # calculate the real side and the corresponding coordinate
            if (predict_x >= field_length and predict_y <= 0):
                temp_x = predict_x
                predict_x = -predict_y
                predict_y = temp_x - field_length
                temp_side = chr(ord(cur_side) + 1)
                predict_side = 'A' if temp_side == 'E' else temp_side
            elif(predict_x <= field_length and predict_y <= -field_length):
                predict_x = field_length - predict_x
                predict_y = -predict_y - field_length
                temp_side = chr(ord(cur_side) + 2)
                predict_side = temp_side if temp_side < 'E' else (chr(ord(temp_side) - 4))
            elif(predict_x <= 0 and predict_y >= -field_length):
                temp_x = predict_x
                predict_x = predict_y + field_length
                predict_y = -temp_x
                temp_side = chr(ord(cur_side) + 3)
                predict_side = temp_side if temp_side < 'E' else (chr(ord(temp_side) - 4))
            
            # print [current location], [direction], [speed] and [predicted location]
            # print("""
            #     The animal was residing at: side %c. From corner %c, walk %3.2f meters to the right and then %3.2f meters ahead; 
            #     Running speed is: %3.2f m/s; 
            #     Running direction in degree is: %3d, relative to boundary of side %c;
            #     Predicted location is: side %c. From corner %c, walk %3.2f meters to the right and then %3.2f meters ahead.
            #     """ 
            #     % (cur_side, cur_side, animal_x, animal_y, animal_speed, animal_direction, cur_side, predict_side, predict_side, predict_x, predict_y))
            processing_time = time.time() - start_time
            print("------------------------------------Separate Line-------------------------------------")
            print("Time spent on prediction: %.9f" %(processing_time))
            if correct_prev_predict:
                # print("Correction: Predicted location is: side %c. From corner %c, walk %3.2f meters to the right and then %3.2f meters ahead. Filename: %s; Line#: %d" % (predict_side, predict_side, predict_x, predict_y, filename, counter))
                print("Correction: Corner %c - (%3.2f, %3.2f); Filename: %s; Line#: %d" % (predict_side, predict_x, predict_y, filename, counter))
            else:
                # print("Predicted location is: side %c. From corner %c, walk %3.2f meters to the right and then %3.2f meters ahead. Filename: %s; Line#: %d" % (predict_side, predict_side, predict_x, predict_y, filename, counter))
                print("Corner %c - (%3.2f, %3.2f); Filename: %s; Line#: %d" % (predict_side, predict_x, predict_y, filename, counter))
            # If the predicted location is far away from the field, release the warning
            # if(predict_y > 50 or predict_x > 150):
            #     print("The animal is predicted to run far away. The hazard value is expected to be low.")
    # else:
        # processing_time = time.time() - start_time
        # print("------------------------------------Separate Line-------------------------------------")
        # print("Time spent on prediction: %.9f" %(processing_time))  
        # if correct_prev_predict:
        #     # print("Correction: Predicted location is: side %c. From corner %c, walk %3.2f meters to the right and then %3.2f meters ahead. Filename: %s; Line#: %d" % (predict_side, predict_side, predict_x, predict_y, filename, counter))
        #     print("Correction: Remain at the same position. Corner %c - (%3.2f, %3.2f); Filename: %s; Line#: %d" % (cur_side, animal_x, animal_y, filename, counter))
        # else:
        #     # print("Predicted location is: side %c. From corner %c, walk %3.2f meters to the right and then %3.2f meters ahead. Filename: %s; Line#: %d" % (predict_side, predict_side, predict_x, predict_y, filename, counter))
        #     print("Remain at the same position. Corner %c - (%3.2f, %3.2f); Filename: %s; Line#: %d" % (cur_side, animal_x, animal_y, filename, counter))      
    # else:
    #     print("""
    #         The animal was firstly detected at: side %c, around (%3.2f, %3.2f);
    #         """ 
    #         % (cur_side, animal_x, animal_y))
        
# receive data from user input - simulate the data received from sensors
# while True:
#         sensor_data = input("Enter data received from sensors:")
#         if(sensor_data):
#             # parse received data - format: “side#-sensor# - timestamp”
#             print(time.time())
#             cur_side = sensor_data.split('-')[0]
#             cur_sensor = sensor_data.split('-')[1]
#             cur_time = float(sensor_data.split('-')[2])
#             locate_and_predict(cur_side, cur_sensor, cur_time)
            
# df = pd.read_csv("sensing_data.csv")
# if not df.empty:
# with open('sensing_data.csv', newline='') as data_file:
#     reader_obj = csv.reader(data_file)
#     for row in reader_obj:
#         # parse received data - format: “side#-sensor# - timestamp”
#         cur_side = row[0]
#         cur_sensor = row[1]
#         cur_time = float(row[2])
#         locate_and_predict(cur_side, cur_sensor, cur_time)
c = 0  
# for filename in os.listdir("/predict/layoutB/"):
for filename in os.listdir("/predict/layoutB/"):
    if filename.endswith('.csv'):
        f = open("/predict/layout4/" + filename, "r")
        ff = csv.reader(f)
        row = next(ff)
        c += 1
        pre_time_1 = -1000
        pre_x_1 = -1
        pre_y_1 = -1
        pre_side_1 = '-'
        pre_sensor_1 = '-'
        pre_time_2 = -1000
        pre_x_2 = -1
        pre_y_2 = -1
        pre_side_2 = '-'
        pre_sensor_2 = '-'
        pre_time_3 = -1000
        pre_x_3 = -1
        pre_y_3 = -1
        pre_side_3 = '-'
        pre_sensor_3 = '-'
        counter = 0
        while(True):
            try:
                # parse received data - format: “side#-sensor# - timestamp”
                counter += 1
                cur_side = row[0]
                cur_sensor = row[1]
                cur_time = float(row[2])
                next_row = next(ff)
                next_time = float(next_row[2])
                start_time = time.time()
                locate_and_predict(cur_side, cur_sensor, cur_time, next_time, filename, counter)
                row = next_row
            except:
                break
            
print (c)
