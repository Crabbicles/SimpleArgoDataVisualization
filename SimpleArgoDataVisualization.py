# https://earth-env-data-science.github.io/assignments/numpy_matplotlib.html
# I have no idea if I did this right as there is no example project available anywhere

import numpy as np
from matplotlib import pyplot as plt
import pooch

url = "https://www.ldeo.columbia.edu/~rpa/float_data_4901412.zip"
files = pooch.retrieve(url, processor=pooch.Unzip(),
                       known_hash="2a703c720302c682f1662181d329c9f22f9f10e1539dc2d6082160a469165009")
# print(files)
# date.npy, T.npy, S.npy, P.npy, levels.npy, lon.npy, lat.npy

date = np.load(files[0])
t = np.load(files[1])
s = np.load(files[2])
p = np.load(files[3])
level = np.arange(0,75)  # Arbitrary "Levels" from Argo Robot, Would need to implement which data point [x] position was the NaN, but for now
                         # I am just setting it to the number of common data points (75, after 3 were NaN across datasets)
lon = np.load(files[5])
lat = np.load(files[6])

# Calculate Mean for each "Level"
t_mean = np.nanmean(t, axis=0)
s_mean = np.nanmean(s, axis=0)
p_mean = np.nanmean(p, axis=0)

# Calculate standard deviation
t_std = np.nanstd(t, axis=0)
s_std = np.nanstd(s, axis=0)
p_std = np.nanstd(p, axis=0)

fig, axarr = plt.subplots(2, 2)

plt.sca(axarr[0, 0])
plt.errorbar(t_mean, level, yerr=t_std)
plt.xlabel("Mean Temperature");
plt.ylabel("Level")

plt.sca(axarr[1, 0])
plt.errorbar(s_mean, level, yerr=s_std)
plt.xlabel("Salinity");
plt.ylabel("Level")

plt.sca(axarr[0, 1])
plt.errorbar(p_mean, level, yerr=p_std)
plt.xlabel("Pressure");
plt.ylabel("Level")

plt.sca(axarr[1, 1])
plt.scatter(lat, lon)
plt.xlabel("Latitude");
plt.ylabel("Longitude")

plt.show()
