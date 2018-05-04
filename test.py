import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from math import sqrt
from math import pi
import matplotlib.pyplot as plt
import pandas as pd

monitored_folder = 'C:\\Users\\H_Abb\\Desktop\\Space_Hackathon'
mag, tempir, uvlight, magx, magy, magz,dist,orientx,orienty,orientz = [], [], [], [], [], [],[],[],[],[]

MAG_BASE = 3.22389238
TEMP_IR_BASE = 25.3
UV_LIGHT_INDEX_BASE = 4.68
MARS_RADIUS = 3397000
DISTANCE_FROM_SURFACE = 200000

print('MAG_BASE: ', MAG_BASE)
print('TEMP_IR_BASE: ', TEMP_IR_BASE)
print('UV_LIGHT_INDEX_BASE: ', UV_LIGHT_INDEX_BASE)


def checkMag():
    if(len(tempir) > 5 and ((sum(mag[-5:]) / 5) - MAG_BASE) / MAG_BASE > 0.01):
        print('Solar winds detected')


def checkUVLight():
    if(len(tempir) > 5 and ((sum(uvlight[-5:]) / 5) - UV_LIGHT_INDEX_BASE) / UV_LIGHT_INDEX_BASE > 0.01):
        print('Object detected')

def lineGraph(xlabel,ylabel,title,X,y):
    plt.scatter(X,y,color='red')
    plt.plot(X,y,color = 'blue')
    plt.title(title)
    plt.xlim(170,200)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


dataset = pd.read_csv('data.csv')
magx.append(dataset.iloc[:, 3:4].values.tolist()[0])
magy.append(dataset.iloc[:, 4:5].values.tolist()[0])
magz.append(dataset.iloc[:, 5:6].values.tolist()[0])
tempir.append(dataset.iloc[:, 1:2].values.tolist()[0])
uvlight.append(dataset.iloc[:, 2:3].values.tolist()[0])
orientx.append(dataset.iloc[:, 6:7].values.tolist()[0])
orienty.append(dataset.iloc[:, 7:8].values.tolist()[0])
orientz.append(dataset.iloc[:, 8:9].values.tolist()[0])
for x, y, z in zip(magx, magy, magz):
    mag.append(sqrt(x * x + y * y + z * z))
for x, y,z in zip(orientx,orienty,orientz):
    orientation = sqrt(x*x+y*y+z*z)
    dist.append(x)
lineGraph('Distance (m)','Temperature (C)','IR output',dist,tempir)
lineGraph('Distance (m)','UV Index (mW/cm^2)','UV output',dist,uvlight)
for i in range(len(tempir)):
    if((abs((sum(tempir[-5:]) / 5) - TEMP_IR_BASE) / TEMP_IR_BASE) > 0.02):
        checkMag()
        checkUVLight()
