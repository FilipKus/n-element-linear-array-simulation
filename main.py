import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.widgets import Slider

def update(val):
    beta_new = beta_slider.val
    # w = 1000000
    l = 0.5
    k = (2*np.pi)/l
    d = l/4
    theta = np.linspace(0, 2*np.pi, 10000)
    line.set_data(theta, update_polar_data(l, k, d, beta_new, theta))
    
    


def update_polar_data(l, k, d, beta, theta):
    # phi = k*d*np.cos(theta) + beta
    # array_factor = np.sin(phi)/(2*np.sin(0.5*phi))
    # array_factor = 20*np.log10(array_factor/2)
    array_factor = np.cos(0.5*(k*d*np.sin(theta)+beta))
    # array_factor = np.abs(array_factor) / np.max(np.abs(array_factor))
    # array_factor = 20*np.log10(array_factor) 

    a = k*l/2
    # Handle small theta values to avoid division by zero
    epsilon = 1e-6
    sin_theta = np.where(np.abs(np.sin(theta)) < epsilon, epsilon, np.sin(theta))

    single_element = ((np.cos(a*np.cos(theta)) - np.cos(a))/sin_theta)
    single_element = single_element ** 2    
    # single_element = 10*np.log10(single_element)
    single_element = np.abs(single_element) / np.max(np.abs(single_element))
    # single_element = 20*np.log10(single_element)

    b = array_factor*single_element
    b = 20*np.log10(b) 
    

    return b


# w = 1000000
l = 0.5
k = (2*np.pi)/l
d = l/4
beta = -1*np.pi/2
# theta = np.pi/2
theta = np.linspace(0, 2*np.pi, 10000)
# array_factor = np.cos(0.5*(k*d*np.cos(theta)+beta))




fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.plot(theta, update_polar_data(l, k, d, beta, theta))
ax.grid(True)      
ax.set_title("Test Plot")
# ax.set_yscale('log')
ax.set_ylim([-40, 0])
line, = ax.plot(theta, update_polar_data(l, k, d, beta, theta))

ax_beta_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
beta_slider = Slider(ax_beta_slider, 'Blue', -4*np.pi, 4*np.pi)

beta_slider.on_changed(update)

plt.show()