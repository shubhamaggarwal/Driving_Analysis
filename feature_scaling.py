import numpy as np


def scale(tableX):
    std_dev_speed = tableX.describe().ix['std'][0]
    std_dev_heading = tableX.describe().ix['std'][1]
    mean_speed = tableX.describe().ix['mean'][0]
    mean_heading = tableX.describe().ix['mean'][1]
    tableX['speed'] = (tableX['speed'] - mean_speed)/std_dev_speed
    tableX['heading'] = (tableX['heading'] - mean_heading)/std_dev_heading
    return tableX

