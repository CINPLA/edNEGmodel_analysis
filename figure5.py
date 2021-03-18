import numpy as np
from scipy.ndimage import uniform_filter1d
from scipy.interpolate import interp1d

# load data from figure 3
data = np.load('data/figure3.npz')
t = data['t'][:-1]
phi_e_n = data['phi_e_n']
phi_e_g = data['phi_e_g']
phi_e_diff = data['phi_e_diff'][:-1]
phi_e_sum = phi_e_n + phi_e_g + phi_e_diff

# interpolate
f_phi_e_n = interp1d(t, phi_e_n, 'cubic')
f_phi_e_g = interp1d(t, phi_e_g, 'cubic')
f_phi_e_diff = interp1d(t, phi_e_diff, 'cubic')
f_phi_e_sum = interp1d(t, phi_e_sum, 'cubic')

tt = np.linspace(int(t[0]), int(t[-1]), len(t))
phi_e_n = f_phi_e_n(tt)
phi_e_g = f_phi_e_g(tt)
phi_e_diff = f_phi_e_diff(tt)
phi_e_sum = f_phi_e_sum(tt)
fig3_t = tt

# calculate moving average
dt = np.diff(tt)[0]
size = int(10/dt)
fig3_phi_DC_n = uniform_filter1d(phi_e_n, size)
fig3_phi_DC_g = uniform_filter1d(phi_e_g, size)
fig3_phi_DC_diff = uniform_filter1d(phi_e_diff, size)
fig3_phi_DC_sum = uniform_filter1d(phi_e_sum, size)

# load data from figure 4
data = np.load('data/figure4.npz')
t = data['t'][:-1]
phi_e_n = data['phi_e_n']
phi_e_g = data['phi_e_g']
phi_e_diff = data['phi_e_diff'][:-1]
phi_e_sum = phi_e_n + phi_e_g + phi_e_diff

# interpolate
f_phi_e_n = interp1d(t, phi_e_n, 'cubic')
f_phi_e_g = interp1d(t, phi_e_g, 'cubic')
f_phi_e_diff = interp1d(t, phi_e_diff, 'cubic')
f_phi_e_sum = interp1d(t, phi_e_sum, 'cubic')

tt = np.linspace(int(t[0]), int(t[-1]), len(t))
phi_e_n = f_phi_e_n(tt)
phi_e_g = f_phi_e_g(tt)
phi_e_diff = f_phi_e_diff(tt)
phi_e_sum = f_phi_e_sum(tt)
fig4_t = tt

# calculate moving average
dt = np.diff(tt)[0]
size = int(10/dt)
fig4_phi_DC_n = uniform_filter1d(phi_e_n, size)
fig4_phi_DC_g = uniform_filter1d(phi_e_g, size)
fig4_phi_DC_diff = uniform_filter1d(phi_e_diff, size)
fig4_phi_DC_sum = uniform_filter1d(phi_e_sum, size)

# save data
np.savez('data/figure5', \
fig3_phi_DC_n = fig3_phi_DC_n, \
fig3_phi_DC_g = fig3_phi_DC_g, \
fig3_phi_DC_diff = fig3_phi_DC_diff, \
fig3_phi_DC_sum = fig3_phi_DC_sum, \
fig4_phi_DC_n = fig4_phi_DC_n, \
fig4_phi_DC_g = fig4_phi_DC_g, \
fig4_phi_DC_diff = fig4_phi_DC_diff, \
fig4_phi_DC_sum = fig4_phi_DC_sum, \
fig3_t = fig3_t, fig4_t = fig4_t)

