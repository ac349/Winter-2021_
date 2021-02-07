import matplotlib.pyplot as pp
import numpy as np
#this file plots temprature and humidity as a function of time
temp_list = [30.7, 30.6, 30.6, 30.6, 30.6]
humidity_list = [41.9, 41.9, 41.9, 41.9, 41.9]

t = np.arange(0,5,1)
y1 = temp_list
y2 =humidity_list

fig, ax1 = pp.subplots()
ax1.set_xlabel('time (h)')
ax1.set_ylabel('temperature (°c)')
ax1.plot(t,y1, color = "red")
ax1.tick_params(axis = 'y') 

ax2 = ax1.twinx()
ax2.set_ylabel("humidity (%)")
ax2.plot(t, y2, color = "blue")
ax2.tick_params(axis='y')
fig.tight_layout()
pp.show()
