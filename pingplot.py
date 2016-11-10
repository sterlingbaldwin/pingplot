#!/usr/bin/python
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import sqrt
from numpy import mean
from subprocess import Popen, PIPE

global host
global data
global loop_count

parser = argparse.ArgumentParser(description='network ping graph')
parser.add_argument('--host', help='the hostname or IP address to ping')
args = parser.parse_args()
host = args.host

def ping(host):
    res = Popen(['ping', '-c', '1', '-t', '5', host], stdout=PIPE).communicate()
    ms = 0
    if b'time=' not in res[0]:
        print res
        return 0
    for s in res[0].split():
        if 'time' in s:
            ms = float(s[5:])
            break
    return ms

def rms(x, axis=None):
    return sqrt(mean(x**2, axis=axis))

fig, ax = plt.subplots()
data = np.array(np.zeros(200))
data2 = np.zeros(200)
x = np.arange(0, 200)
line, = ax.plot(x, data)
line2, = ax.plot(x, data2)

def animate(i):
    new_data = ping(host)
    data[i] = new_data
    line.set_ydata(data)
    new_range = np.arange(0, i+1)
    data2[i] = rms(data[0:i])
    ax.relim()
    ax.autoscale_view()
    return line,

ani = animation.FuncAnimation(
    fig,
    animate,
    np.arange(1, 200),
    interval=25,
    blit=False)
plt.show()
