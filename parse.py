import numpy as np
import matplotlib.pyplot as plt
import time, datetime
import matplotlib.dates as mdates
import datetime as dt

data = np.genfromtxt("rv_data.txt", delimiter="\t", dtype=np.str)
print(data.shape)
from sklearn.linear_model import LinearRegression

#unique, counts = np.unique(data[:, 1], return_counts=True)
#inds = np.argsort(-counts)
#print(unique[inds][:10], counts[inds][:10])

results = dict()
to_find = ["Patkis 18g", "Suffeli", "Japp", "Mars", "Kismet"]
for s in to_find:
    results[s] = dict()

for i, s in enumerate(data):
    for find in to_find:
        if find in s[1]:

            ts = s[0].split(" ")[0]
            year_month = ts[:7]

            if year_month not in results[find]:
                results[find][year_month] = 0
            results[find][year_month] += 1

    if i % 100000 == 0:
        print("at", i)

plt.figure(figsize=(12,6), dpi=150)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator())

for key, value in results.items():
    value = np.array(list(value.items()), dtype=np.str)

    x, y = value[:, 1].astype(np.int), [dt.datetime.strptime(d,'%Y-%m').date() for d in value[:, 0]]
    plt.plot(y, x, label=key)

plt.gcf().autofmt_xdate()
plt.legend()
plt.savefig("koffee_pk.png")

"""
# convert the epoch format to matplotlib date format 
mpl_data = mdates.epoch2num(results)

# plot it
fig, ax = plt.subplots(1,1)
ax.hist(mpl_data, bins=100)

locator = mdates.AutoDateLocator()
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))
plt.savefig("kahvi.jpg")
"""