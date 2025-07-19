import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.widgets import Slider

def update(val):
    beta_new = beta_slider.val
    l = 0.3
    k = (2*np.pi)/l
    d = l/4
    theta = np.linspace(0, 2*np.pi, 100)
    line.set_data(theta, update_polar_data(l, k, d, beta_new, theta))
    
    


def update_polar_data(l, k, d, beta, theta):
    array_factor = np.cos(0.5*(k*d*np.cos(theta)+beta))
    return array_factor


l = 0.3
k = (2*np.pi)/l
d = l/4
beta = np.pi/2
# theta = np.pi/2
theta = np.linspace(0, 2*np.pi, 100)
# array_factor = np.cos(0.5*(k*d*np.cos(theta)+beta))




fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.plot(theta, update_polar_data(l, k, d, beta, theta))
ax.grid(True)      
ax.set_title("Test Plot")
line, = ax.plot(theta, update_polar_data(l, k, d, beta, theta))

ax_beta_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
beta_slider = Slider(ax_beta_slider, 'Blue', -4*np.pi, 4*np.pi)

beta_slider.on_changed(update)

plt.show()