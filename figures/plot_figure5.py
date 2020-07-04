import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from set_style import set_style

set_style('default', w=1, h=2)

fig, axarr = plt.subplots(2,2)

data = np.load('../data/figure4_figure5.npz')

t = data['t']
K_sn = data['cK_sn']
K_se = data['cK_se']
K_sg = data['cK_sg']
K_dn = data['cK_dn']
K_de = data['cK_de']
K_dg = data['cK_dg']

V_sn = data['V_sn']
V_se = data['V_se']
V_sg = data['V_sg']
V_dn = data['V_dn']
V_de = data['V_de']
V_dg = data['V_dg']

### Panel A1 ###
axarr[0,0].plot(t, K_se, 'k', label='soma')
axarr[0,0].plot(t, K_de, 'k:', label='dendrite')
axarr[0,0].set_ylabel('$\mathrm{[K]_{e}}$ [mM]')
axarr[0,0].legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper left', labelspacing=0.01)

### Panel A2 ###
axarr[0,1].plot(t, K_se, 'k', label='soma')
axarr[0,1].plot(t, K_de, 'k:', label='dendrite')

### Panel B1 ###
axarr[1,0].plot(t, (V_sn-V_sn[0])/V_sn[0]*100, 'k', label='soma')
axarr[1,0].plot(t, (V_dn-V_dn[0])/V_dn[0]*100, 'k:', label='dendrite')
axarr[1,0].set_ylabel('$\Delta V$ [\%]')
axarr[1,0].legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper left', labelspacing=0.01)
axarr[1,0].set_xlabel('time [s]')

### Panel B2 ###
axarr[1,1].plot(t, (V_sn-V_sn[0])/V_sn[0]*100, 'k', label='soma')
axarr[1,1].plot(t, (V_dn-V_dn[0])/V_dn[0]*100, 'k:', label='dendrite')
axarr[1,1].set_xlabel('time [s]')

axarr[0,0].set_ylim(0,18)
axarr[0,1].set_ylim(0,23)
axarr[1,0].set_ylim(0,0.06)
axarr[1,1].set_ylim(0,45)

for i in range(2):
    axarr[i,0].set_xlim(0,4)
    axarr[i,0].set_xticks([0,1,2,3,4])
    axarr[i,1].set_xlim(0,800)
    axarr[i,1].set_xticks([0,200,400,600,800])

for axi in axarr:
    for ax in axi:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

# ABC
axarr[0,0].text(-0.1, 1.1, 'A1', transform=axarr[0,0].transAxes, fontsize=12, fontweight='bold', va='top', ha='right')
axarr[0,1].text(-0.1, 1.1, 'A2', transform=axarr[0,1].transAxes, fontsize=12, fontweight='bold', va='top', ha='right')
axarr[1,0].text(-0.1, 1.15, 'B1', transform=axarr[1,0].transAxes, fontsize=12, fontweight='bold', va='top', ha='right')
axarr[1,1].text(-0.1, 1.15, 'B2', transform=axarr[1,1].transAxes, fontsize=12, fontweight='bold', va='top', ha='right')

fig.align_ylabels(axarr)
plt.tight_layout()
plt.savefig('figure5.pdf', dpi=600)
