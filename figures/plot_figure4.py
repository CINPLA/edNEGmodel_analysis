import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from set_style import set_style

set_style('default', w=1, h=3.5)

fig, [ax1, ax2, ax3, ax4, ax5] = plt.subplots(5,1)

data = np.load('../data/figure4.npz')

t = data['t']
phi_msn = data['phi_msn']
phi_mdn = data['phi_mdn']
phi_msg = data['phi_msg']
phi_mdg = data['phi_mdg']

Na_se = data['cNa_se']
K_se = data['cK_se']
Cl_se = data['cCl_se']
Ca_se = data['cCa_se']
Na_de = data['cNa_de']
K_de = data['cK_de']
Cl_de = data['cCl_de']
Ca_de = data['cCa_de']

V_sn = data['V_sn']
V_se = data['V_se']
V_sg = data['V_sg']
V_dn = data['V_dn']
V_de = data['V_de']
V_dg = data['V_dg']

### Panel A ###
l001 = ax1.plot(t, phi_msn*1000, 'k')[0]
l003 = ax1.plot(t, phi_msg*1000, '#9467bd')[0]
ax1.set_ylabel('$\phi\mathrm{_{ms}}$ [mV]')
ax1.set_yticks([-70, 0])
ax1.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax1.set_xlim(0,10)

### Panel B ###
l01 = ax2.plot(t, phi_msn*1000, 'k', label='neuron')[0]
l02 = ax2.plot(t, phi_msg*1000, '#9467bd', label='glia')[0]
ax2.set_ylabel('$\phi\mathrm{_{ms}}$ [mV]')
ax2.set_yticks([-70, 0])

##### Panel C ###
l1 = ax3.plot(t, Na_se-Na_se[0], zorder=10)[0]
l2 = ax3.plot(t, K_se-K_se[0], zorder=10)[0]
l3 = ax3.plot(t, Cl_se-Cl_se[0], zorder=10)[0]
l4 = ax3.plot(t, Ca_se-Ca_se[0], zorder=10)[0]
ax3.set_ylabel('$\Delta \mathrm{[k]_{se}}$ [mM]')
fig.legend([l01, l02, l1, l2, l3, l4], ['neuron', 'glia', '$\mathrm{Na^+}$', '$\mathrm{K^+}$', '$\mathrm{Cl^-}$', '$\mathrm{Ca^{2+}}$'], \
    loc=(0.60,0.73), ncol=3, fontsize='small', handlelength=0.8, handletextpad=0.4, columnspacing=0.4)
ax3.set_ylim(-60,60)

#### Panel D ###
ax4.plot(t, Na_de-Na_de[0], zorder=10)
ax4.plot(t, K_de-K_de[0], zorder=10)
ax4.plot(t, Cl_de-Cl_de[0], zorder=10)
ax4.plot(t, Ca_de-Ca_de[0], zorder=10)
ax4.set_ylabel('$\Delta \mathrm{[k]_{de}}$ [mM]')
ax4.set_ylim(-60,60)

### Panel E ###
ax5.plot(t, ((V_sn+V_dn)-(V_sn[0]+V_dn[0]))/(V_sn[0]+V_dn[0])*100, 'k', label='neuron')
ax5.plot(t, ((V_se+V_de)-(V_se[0]+V_de[0]))/(V_se[0]+V_de[0])*100, 'k:', label='ECS')
ax5.plot(t, ((V_sg+V_dg)-(V_sg[0]+V_dg[0]))/(V_sg[0]+V_dg[0])*100, 'k--', label='glia')
ax5.set_ylabel('$\Delta V$ [\%]')
ax5.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='lower right', labelspacing=0.01)
ax5.set_yticks([-100, -50, 0, 50])

for ax in [ax2, ax3, ax4, ax5]:
    ax.set_xlim(0,800)
for ax in [ax1, ax2, ax3, ax4, ax5]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

ax5.set_xlabel('time [s]')

# ABC
panel = np.array(['A', 'B', 'C', 'D', 'E'])
i = 0
for ax in [ax1, ax2, ax3, ax4, ax5]:
    ax.text(-0.05, 1.2, panel[i], transform=ax.transAxes, fontsize=12, fontweight='bold', va='top', ha='right')
    i += 1

plt.tight_layout()
plt.savefig('figure4.pdf', dpi=600)
