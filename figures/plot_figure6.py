import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from set_style import set_style

set_style('figure6', w=2, h=4)

fig = plt.figure()
gs = gridspec.GridSpec(4,4)
ax1 = plt.subplot(gs[0,0])
ax2 = plt.subplot(gs[0,1])
ax3 = plt.subplot(gs[1,0])
ax4 = plt.subplot(gs[1,1])
ax5 = plt.subplot(gs[2,0])
ax6 = plt.subplot(gs[2,1])
ax7 = plt.subplot(gs[3,0])
ax8 = plt.subplot(gs[3,1])
axarr = np.array([[ax1, ax2], [ax3, ax4], [ax5, ax6], [ax7, ax8]])
axy = plt.subplot(gs[0:2,2:])
axz = plt.subplot(gs[2:,2:])

data = np.load('../data/figure6_with_glia_4.npz')
phi_msn = data['phi_msn']*1000
cK_se = data['cK_se']
V_n = data['V_sn'] + data['V_dn']
dV_n = (V_n-V_n[0])/V_n[0]*100
t = data['t']
axarr[0,0].plot(t, phi_msn, 'k')
axarr[2,0].plot(t, cK_se, 'k', zorder=10)
axarr[3,0].plot(t, dV_n, 'k', zorder=10)

data = np.load('../data/figure6_with_glia_17.npz')
phi_msn = data['phi_msn']*1000
cK_se = data['cK_se']
V_n = data['V_sn'] + data['V_dn']
dV_n = (V_n-V_n[0])/V_n[0]*100
t = data['t']
axarr[0,1].plot(t, phi_msn, 'k')
axarr[2,1].plot(t, cK_se, 'k', zorder=10)
axarr[3,1].plot(t, dV_n, 'k', zorder=10)

data = np.load('../data/figure6_no_glia_4.npz')
phi_msn = data['phi_msn']*1000
cK_se = data['cK_se']
V_n = data['V_sn'] + data['V_dn']
dV_n = (V_n-V_n[0])/V_n[0]*100
t = data['t']
axarr[1,0].plot(t, phi_msn, '#d62728')
axarr[2,0].plot(t, cK_se, '#d62728', zorder=10)
axarr[3,0].plot(t, dV_n, '#d62728', zorder=10)

data = np.load('../data/figure6_no_glia_17.npz')
phi_msn = data['phi_msn']*1000
cK_se = data['cK_se']
V_n = data['V_sn'] + data['V_dn']
dV_n = (V_n-V_n[0])/V_n[0]*100
t = data['t']
axarr[1,1].plot(t, phi_msn, '#d62728')
axarr[2,1].plot(t, cK_se, '#d62728', zorder=10)
axarr[3,1].plot(t, dV_n, '#d62728', zorder=10)

axarr[3,0].set_xlabel('time [s]')
axarr[3,1].set_xlabel('time [s]')

for axa in axarr:
    for ax in axa:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
axy.spines['top'].set_visible(False)
axy.spines['right'].set_visible(False)
axz.spines['top'].set_visible(False)
axz.spines['right'].set_visible(False)

for i in range(0,2):
    for j in range(0,2):
        axarr[i,j].set_ylim([-90, 20])
        axarr[i,j].set_yticks([-70, 0])
        axarr[i,j].set_xlim(0,10)
        axarr[i,j].set_xticks([0,2,4,6,8,10])

axarr[2,0].axvline(10, color='k', zorder=1)
axarr[3,0].axvline(10, color='k', zorder=1)
axarr[2,1].axvline(10, color='k', zorder=1)
axarr[3,1].axvline(10, color='k', zorder=1)

axarr[0,0].set_title('$\phi\mathrm{_{msn}}$ (with glia)')
axarr[0,1].set_title('$\phi\mathrm{_{msn}}$ (with glia)')
axarr[1,0].set_title('$\phi\mathrm{_{msn}}$ (no glia)')
axarr[1,1].set_title('$\phi\mathrm{_{msn}}$ (no glia)')
axarr[2,0].set_title('$\mathrm{[K^+]_{se}}$')
axarr[2,1].set_title('$\mathrm{[K^+]_{se}}$')
axarr[3,0].set_title('Neuronal swelling')
axarr[3,1].set_title('Neuronal swelling')

axarr[0,0].set_ylabel('mV')
axarr[1,0].set_ylabel('mV')
axarr[2,0].set_ylabel('mM')
axarr[3,0].set_ylabel('\%')

axarr[2,0].set_xlim(0,20)
axarr[2,0].set_ylim(3,12)
axarr[2,0].set_yticks([3,6,9,12])
axarr[2,0].set_xticks([0,5,10,15,20])

axarr[2,1].set_xlim(0,20)
axarr[2,1].set_ylim(3,22)
axarr[2,1].set_yticks([3,10,20])
axarr[2,1].set_xticks([0,5,10,15,20])

axarr[3,0].set_xlim(0,90)
axarr[3,0].set_ylim(0,3)
axarr[3,0].set_yticks([0,1,2,3])
axarr[3,0].set_xticks([0,30,60,90])

axarr[3,1].set_xlim(0,90)
axarr[3,1].set_ylim(0,22)
axarr[3,1].set_yticks([0,10,20])
axarr[3,1].set_xticks([0,30,60,90])

data = np.load('../data/figure6.npz')

ff_with_glia = data['ff_with_glia']
Ke_with_glia = data['Ke_with_glia']
Vn_with_glia = data['Vn_with_glia']
ff_without_glia = data['ff_without_glia']
Ke_without_glia = data['Ke_without_glia']
Vn_without_glia = data['Vn_without_glia']

axy.plot(ff_with_glia, Ke_with_glia, 'o-', color='k', label = 'with glia', markersize=6, linewidth=2, zorder=10)
axy.plot(ff_without_glia, Ke_without_glia, '^-', color='#d62728', label = 'no glia', markersize=6, linewidth=2, zorder=10)
axy.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper left', labelspacing=0.01)
axy.set_xlabel('stimulus frequency [Hz]')
axy.set_ylabel('mM')
axy.set_title('Maximum $\mathrm{[K^+]_{se}}$')
axy.set_xlim(0,10)
axy.set_ylim(0,25)

axz.plot(ff_with_glia, Vn_with_glia, 'o-', color='k', label = 'with glia', markersize=6, linewidth=2)
axz.plot(ff_without_glia, Vn_without_glia, '^-', color='#d62728', label = 'no glia', markersize=6, linewidth=2)
axz.set_xlabel('stimulus frequency [Hz]')
axz.set_ylabel('$\%$')
axz.set_title('Neuronal swelling')
axz.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper left', labelspacing=0.01)
axz.set_xlim(0,10)
axz.set_ylim(0,23)

panel = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
k = 0
for i in range(0,4):
    for j in range(0,2):
        axarr[i,j].text(-0.15, 1.1, panel[k], transform=axarr[i,j].transAxes, fontsize=19, fontweight='bold', va='top', ha='right')
        k += 1
axy.text(-0.06, 1, 'I', transform=axy.transAxes, fontsize=19, fontweight='bold', va='top', ha='right')
axz.text(-0.05, 1, 'J', transform=axz.transAxes, fontsize=19, fontweight='bold', va='top', ha='right')

plt.tight_layout()
plt.savefig('figure6.pdf', dpi=600)
