import numpy as np
import matplotlib.pyplot as plt
import time, datetime
import matplotlib.dates as mdates

data = np.genfromtxt('all.txt', dtype='str', delimiter="\n")
print(data.shape)

results = []
for s in data:
    if "Coffee" in s:
        ts = s.split(" ")[0]
        res = time.mktime(datetime.datetime.strptime(ts, "%Y-%m-%d").timetuple())
        results.append(res)


# convert the epoch format to matplotlib date format 
mpl_data = mdates.epoch2num(results)

# plot it
fig, ax = plt.subplots(1,1)
ax.hist(mpl_data, bins=100)

locator = mdates.AutoDateLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))
plt.savefig("kahvi.jpg")