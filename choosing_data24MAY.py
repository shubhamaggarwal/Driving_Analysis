import pandas as pd
import numpy as np
import matplotlib.pyplot as pt

columns = [1, 3, 4, 7, 8]

df = pd.read_csv('driver_gps_log_stat_log.csv',
 names = ['ID', 'OBDTIME', 'GPS_TIME', 'SPEED', 'DIR'], 
 header = 0, 
 usecols = columns
)


driver1 = (df.ID == '213GL2014014870')
driver2 = (df.ID == '213GL2014013511')
driver3 = (df.ID == '213GL2014013573')



fig = pt.figure()
fig1 = fig.add_subplot(3,1,1)
fig2 = fig.add_subplot(3,1,2)
fig3 = fig.add_subplot(3,1,3)


fig1.scatter(df[driver1]['GPS_TIME'], df[driver1]['DIR'], color = 'blue')
fig1.set_xlabel('Time')
fig1.set_ylabel('Speed')
fig1.set_title('Driver 1 Speed vs Time Graph')
fig1.legend('Driver1')


fig2.scatter(df[driver2]['GPS_TIME'], df[driver2]['DIR'], color = 'red')
fig2.set_xlabel('Time')
fig2.set_ylabel('Speed')
fig2.set_title('Driver 2 Speed vs Time Graph')
fig2.legend('Driver2')

fig3.scatter(df[driver3]['GPS_TIME'], df[driver3]['DIR'], color = 'green')
fig3.set_xlabel('Time')
fig3.set_ylabel('Speed')
fig3.set_title('Driver 3 Speed vs Time Graph')
fig3.legend('Driver3')

pt.show()