import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from set_style import set_style

set_style('default', w=1, h=3)

fig, [ax1, ax2, ax3] = plt.subplots(3,1)

data = np.load('../data/figure3.npz')

t = data['t']
phi_e_n = data['phi_e_n']*1000
phi_e_g = data['phi_e_g']*1000
phi_e_diff = data['phi_e_diff']*1000
phi_e_sum = phi_e_n + phi_e_g + phi_e_diff[:-1]

ax1.plot(t[:-1], phi_e_n, 'k', zorder=10, label='$\phi\mathrm{_{se,n}}$')
ax1.plot(t[:-1], phi_e_g, color='#9467bd', zorder=10, label='$\phi\mathrm{_{se,g}}$')
ax1.plot(t[:-1], phi_e_diff[:-1], color='tab:red', zorder=9, label='$\phi\mathrm{_{se,diff}}$')
ax1.plot(t[:-1], phi_e_sum, 'k--', label='$\phi\mathrm{_{se,sum}}$') 
ax1.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='lower right')
ax1.set_xlim([1.03, 1.045])
ax1.set_ylabel('$\phi\mathrm{_{se}}$ [mV]')

data = np.load('../data/figure5.npz')

t = data['fig3_t']
phi_DC_n = data['fig3_phi_DC_n']*1000
phi_DC_g = data['fig3_phi_DC_g']*1000
phi_DC_diff = data['fig3_phi_DC_diff']*1000
phi_DC_sum = data['fig3_phi_DC_sum']*1000
ax2.plot(t, phi_DC_n, 'k', zorder=10, label=r'$\bar{\phi}\mathrm{_{se,n}}$')
ax2.plot(t, phi_DC_g, color='#9467bd', zorder=10, label=r'$\bar{\phi}\mathrm{_{se,g}}$')
ax2.plot(t, phi_DC_diff, color='tab:red', zorder=9, label=r'$\bar{\phi}\mathrm{_{se,diff}}$')
ax2.plot(t, phi_DC_sum, color='grey', label=r'$\bar{\phi}\mathrm{_{se,sum}}$') 
ax2.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='lower right')
ax2.set_ylabel(r'$\bar{\phi}\mathrm{_{se}}$ [mV]')

t = data['fig4_t']
phi_DC_n = data['fig4_phi_DC_n']*1000
phi_DC_g = data['fig4_phi_DC_g']*1000
phi_DC_diff = data['fig4_phi_DC_diff']*1000
phi_DC_sum = data['fig4_phi_DC_sum']*1000
ax3.plot(t, phi_DC_n, 'k', zorder=10)
ax3.plot(t, phi_DC_g, color='#9467bd', zorder=10)
ax3.plot(t, phi_DC_diff, color='tab:red', zorder=9)
ax3.plot(t, phi_DC_sum, color='grey') 
ax3.set_ylabel(r'$\bar{\phi}\mathrm{_{se}}$ [mV]')

ax2.set_xlim(0,1400)
ax3.set_xlim(0,800)
ax3.set_xlabel('time [s]')

for ax in [ax1, ax2, ax3]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

panel = np.array(['A', 'B', 'C'])
i = 0
for ax in [ax1, ax2, ax3]:
    ax.text(-0.05, 1.2, panel[i], transform=ax.transAxes, fontsize=12, fontweight='bold', va='top', ha='right')
    i += 1

plt.tight_layout()
plt.savefig('figure5.pdf', dpi=600)
