import numpy as np

def scale(tableX):
    mean_speed=0.0
    mean_direction=0.0
    mean_mileage=0.0
    max_speed=0
    min_speed=1000000000000
    max_direction= 0
    min_direction = 1000000000000
    max_mileage = 0.0
    min_mileage = 1000000000000.0
    size=tableX.shape
    for i in range(size[0]):
        mean_speed+=tableX[i][0]
        mean_direction+=tableX[i][1]
        #mean_mileage+=tableX[i][2]
        max_speed=max(max_speed,tableX[i][0])
        min_speed = min(min_speed, tableX[i][0])
        max_direction = max(max_direction, tableX[i][1])
        min_direction = min(min_direction, tableX[i][1])
        #max_mileage = max(max_mileage, tableX[i][2])
        #min_mileage = min(min_mileage, tableX[i][2])

    mean_speed=mean_speed/tableX.size
    mean_direction=mean_direction/tableX.size
    #mean_mileage=mean_mileage/tableX.size

    for i in range(size[0]):
        tableX[i][0]=(float(tableX[i][0])-mean_speed)/float(max_speed-min_speed)
        tableX[i][1] = (float(tableX[i][1]) - mean_direction) / float(max_direction - min_direction)
        #tableX[i][2] = (float(tableX[i][2]) - mean_mileage) / float(max_mileage - min_mileage)
    return tableX

