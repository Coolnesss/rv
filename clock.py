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
to_find = ["Coffee", "Powerking"]
for s in to_find:
    results[s] = dict()

for i, s in enumerate(data):
    for find in to_find:
        if find in s[1]:
            ts = s[0].split(" ")[1]
            time = ts[:2]

            if time not in results[find]:
                results[find][time] = 0
            results[find][time] += 1

    if i % 100000 == 0:
        print("at", i)

plt.figure(figsize=(12,6), dpi=150)
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H'))
#plt.gca().xaxis.set_major_locator(mdates.HourLocator())

for key, value in results.items():
    value = np.array(list(value.items()), dtype=np.str)

    x, y = value[:, 1].astype(np.int), value[:, 0].astype(np.int)#[dt.datetime.strptime(d,'%H').date() for d in value[:, 0]]
    inds = np.argsort(x)
    x, y = x[inds], y[inds]
    plt.hist(y,x, label=key)

#plt.gcf().autofmt_xdate()
plt.legend()
plt.savefig("clock.png")
