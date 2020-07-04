import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from set_style import set_style

set_style('default', w=1, h=3)

fig, axarr = plt.subplots(4,2)

data = np.load('../data/figure4_figure5.npz')

t = data['t']
phi_msn = data['phi_msn']
phi_msg = data['phi_msg']

E_Na_sn = data['E_Na_sn']
E_Na_sg = data['E_Na_sg']
E_K_sn = data['E_K_sn']
E_K_sg = data['E_K_sg']
E_Cl_sn = data['E_Cl_sn']
E_Cl_sg = data['E_Cl_sg']
E_Ca_sn = data['E_Ca_sn']

V_sn = data['V_sn']
V_se = data['V_se']
V_sg = data['V_sg']
V_dn = data['V_dn']
V_de = data['V_de']
V_dg = data['V_dg']

### Panel A1 ###
axarr[0,0].plot(t, phi_msn*1000, 'k', label='neuron')
axarr[0,0].plot(t, phi_msg*1000, '#9467bd', label='glia')
axarr[0,0].set_ylabel('$\phi\mathrm{_{ms}}$ [mV]')
axarr[0,0].set_yticks([-70, -30, 0])
axarr[0,0].legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper right', labelspacing=0.01)

### Panel A2 ###
axarr[0,1].plot(t, phi_msn*1000, 'k', label='neuron')
axarr[0,1].plot(t, phi_msg*1000, '#9467bd', label='glia')
axarr[0,1].set_yticks([-70, -30, 0])

#### Panel B1 ###
l1 = axarr[1,0].plot(t, (E_Na_sn-E_Na_sn[0])*1000, zorder=10)[0]
l2 = axarr[1,0].plot(t, (E_K_sn-E_K_sn[0])*1000, zorder=10)[0]
l3 = axarr[1,0].plot(t, (E_Cl_sn-E_Cl_sn[0])*1000, zorder=10)[0]
l4 = axarr[1,0].plot(t, (E_Ca_sn-E_Ca_sn[0])*1000, zorder=10)[0]
axarr[1,0].set_ylabel('$\Delta E\mathrm{_{k,sn}}$ [mV]')
axarr[1,0].set_ylim(-20, 45)
axarr[1,0].set_yticks([-10, 0, 20, 40])
fig.legend([l1, l2, l3, l4], ['$E\mathrm{_{Na}}$', '$E\mathrm{_K}$', '$E\mathrm{_{Cl}}$', '$E\mathrm{_{Ca}}$'], \
    loc=(0.19,0.45), ncol=2, fontsize='small', handlelength=1, handletextpad=0.4, columnspacing=0.4)

#### Panel B2 ###
l1 = axarr[1,1].plot(t, (E_Na_sn-E_Na_sn[0])*1000, zorder=10)[0]
l2 = axarr[1,1].plot(t, (E_K_sn-E_K_sn[0])*1000, zorder=10)[0]
l3 = axarr[1,1].plot(t, (E_Cl_sn-E_Cl_sn[0])*1000, zorder=10)[0]
l4 = axarr[1,1].plot(t, (E_Ca_sn-E_Ca_sn[0])*1000, zorder=10)[0]
axarr[1,1].set_ylim(-50, 70)
axarr[1,1].set_yticks([-35, 0, 35])

#### Panel C1 ###
axarr[2,0].plot(t, (E_Na_sg-E_Na_sg[0])*1000, zorder=9)[0]
axarr[2,0].plot(t, (E_K_sg-E_K_sg[0])*1000, zorder=10)[0]
axarr[2,0].plot(t, (E_Cl_sg-E_Cl_sg[0])*1000, zorder=10)[0]
axarr[2,0].set_ylabel('$\Delta E\mathrm{_{k,sg}}$ [mV]')
axarr[2,0].set_yticks([0, 20, 40])

#### Panel C2 ###
axarr[2,1].plot(t, (E_Na_sg-E_Na_sg[0])*1000, zorder=9)[0]
axarr[2,1].plot(t, (E_K_sg-E_K_sg[0])*1000, zorder=10)[0]
axarr[2,1].plot(t, (E_Cl_sg-E_Cl_sg[0])*1000, zorder=10)[0]

### Panel D1 ###
axarr[3,0].plot(t, ((V_sn+V_dn)-(V_sn[0]+V_dn[0]))/(V_sn[0]+V_dn[0])*100, 'k', label='neuron')
axarr[3,0].plot(t, ((V_se+V_de)-(V_se[0]+V_de[0]))/(V_se[0]+V_de[0])*100, 'k:', label='ecs')
axarr[3,0].plot(t, ((V_sg+V_dg)-(V_sg[0]+V_dg[0]))/(V_sg[0]+V_dg[0])*100, 'k--', label='glia')
axarr[3,0].set_ylabel('$\Delta V$ [\%]')
axarr[3,0].legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='lower left', labelspacing=0.01)
axarr[3,0].set_ylim(-0.3, 0.1)
axarr[3,0].set_yticks([-0.2, 0])
axarr[3,0].set_xlabel('time [s]')

### Panel D2 ###
axarr[3,1].plot(t, ((V_sn+V_dn)-(V_sn[0]+V_dn[0]))/(V_sn[0]+V_dn[0])*100, 'k', label='neuron')
axarr[3,1].plot(t, ((V_se+V_de)-(V_se[0]+V_de[0]))/(V_se[0]+V_de[0])*100, 'k:', label='ecs')
axarr[3,1].plot(t, ((V_sg+V_dg)-(V_sg[0]+V_dg[0]))/(V_sg[0]+V_dg[0])*100, 'k--', label='glia')
axarr[3,1].set_ylim(-100, 50)
axarr[3,1].set_yticks([-100, -50, 0, 25])
axarr[3,1].set_xlabel('time [s]')

for i in range(0,4):
    axarr[i,0].set_xlim(0,4)
    axarr[i,0].set_xticks([0,1,2,3,4])

for i in range(0,4):
    axarr[i,1].set_xlim(0,800)
    axarr[i,1].set_xticks([0,200,400,600,800])

for axa in axarr:
    for ax in axa:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

# ABC
panel = np.array([['A1', 'A2'], ['B1', 'B2'], ['C1', 'C2'], ['D1', 'D2']])
for i in range(0,4):
    for j in range(0,2):
        axarr[i,j].text(-0.1, 1.1, panel[i,j], transform=axarr[i,j].transAxes, fontsize=12, fontweight='bold', va='top', ha='right')

fig.align_ylabels(axarr)
plt.tight_layout()
plt.savefig('figure4.pdf', dpi=600)
