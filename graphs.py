import matplotlib.pyplot as pt
import pandas as pd
import numpy as np

fig = pt.figure()
fig1 = fig.add_subplot(1,2,1)

columns = [0, 1, 2, 4]
df = pd.read_csv('data.csv', names = ['ID', 'Speed', 'Heading', 'TimeStamp'], header = None, usecols = columns)


driver1 = (df.ID == '213GL2014014870')
driver2 = (df.ID == '213GL2014013511')
driver3 = (df.ID == '213GL2014013573')

print(df[driver1].head())

# fig1.scatter(df[driver1]['TimeStamp'], df[driver1]['Speed'], color = 'blue')

'''
fig1.scatter(df[driver2]['ID'], df[driver2]['Speed'], color = 'red')
fig1.scatter(df[driver3]['ID'], df[driver3]['Speed'], color = 'green')
'''
#pt.show()
