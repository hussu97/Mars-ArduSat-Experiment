import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from math import sqrt
import matplotlib.pyplot as plt
import pandas as pd

monitored_folder = 'C:\\Users\\H_Abb\\Desktop\\Space_Hackathon'
mag, tempir, uvlight, magx, magy, magz,dist = [], [], [], [], [], [],[]

MAG_BASE = 3.22389238
TEMP_IR_BASE = 25.3
UV_LIGHT_INDEX_BASE = 4.68

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
    plt.gca().set_ylim([-20,120])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


class FolderMonitor(FileSystemEventHandler):
    def on_modified(self, event):
        dataset = pd.read_csv('data.csv')
        magx.append(dataset.iloc[-1:, :1].values.tolist()[0][0])
        magy.append(dataset.iloc[-1:, 1:2].values.tolist()[0][0])
        magz.append(dataset.iloc[-1:, 2:3].values.tolist()[0][0])
        tempir.append(dataset.iloc[-1:, 3:4].values.tolist()[0][0])
        uvlight.append(dataset.iloc[-1:, 4:5].values.tolist()[0][0])
        dist.append(dataset.iloc[-1:, 5:6].values.tolist()[0][0])
        for x, y, z in zip(magx, magy, magz):
            mag.append(sqrt(x * x + y * y + z * z))
        del mag[len(dataset):]
        del tempir[len(dataset):]
        del uvlight[len(dataset):]
        del dist[len(dataset):]
        if(len(tempir) > 5 and (abs((sum(tempir[-5:]) / 5) - TEMP_IR_BASE) / TEMP_IR_BASE) > 0.02):
            checkMag()
            checkUVLight()
        if(len(dist)>5):
            print('hi')
            lineGraph('Distance (m)','Temperature (C)','IR output',dist,tempir)


observer = Observer()
observer.schedule(FolderMonitor(), monitored_folder, recursive=True)
observer.start()
try:
    time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
