import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from set_style import set_style

set_style('default', w=1, h=3)

fig = plt.figure()
gs = gridspec.GridSpec(4,4)
ax0 = plt.subplot(gs[0,:])
ax1 = plt.subplot(gs[1,0])
ax2 = plt.subplot(gs[1,1], sharey=ax1)
ax3 = plt.subplot(gs[1,2], sharey=ax1)
ax4 = plt.subplot(gs[1,3], sharey=ax1)
ax5 = plt.subplot(gs[2,0])
ax6 = plt.subplot(gs[2,1], sharey=ax5)
ax7 = plt.subplot(gs[2,2], sharey=ax5)
ax8 = plt.subplot(gs[2,3], sharey=ax5)
ax9 = plt.subplot(gs[3,0])
ax10 = plt.subplot(gs[3,1], sharey=ax9)
ax11 = plt.subplot(gs[3,2], sharey=ax9)
ax12 = plt.subplot(gs[3,3], sharey=ax9)

data = np.load('../data/figure3.npz')

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

### Panel A ###
l01 = ax0.plot(t, phi_msn*1000, 'k', label='neuron')[0]
l02 = ax0.plot(t, phi_msg*1000, '#9467bd', label='glia')[0]
ax0.set_ylabel('$\phi\mathrm{_{ms}}$ [mV]')
ax0.set_yticks([-70, 0])
ax0.set_xlim(0,1400)

##### Panel B1 ###
l1 = ax1.plot(t, (E_Na_sn-E_Na_sn[0])*1000, zorder=10)[0]
l2 = ax1.plot(t, (E_K_sn-E_K_sn[0])*1000, zorder=10)[0]
l3 = ax1.plot(t, (E_Cl_sn-E_Cl_sn[0])*1000, zorder=10)[0]
l4 = ax1.plot(t, (E_Ca_sn-E_Ca_sn[0])*1000, zorder=10)[0]
ax1.set_title('Initial phase')
ax1.set_ylabel('$\Delta E\mathrm{_{k,sn}}$ [mV]')
ax1.set_xlim(0,10)
fig.legend([l01, l02, l1, l2, l3, l4], ['neuron', 'glia', '$\mathrm{Na^+}$', '$\mathrm{K^+}$', '$\mathrm{Cl^-}$', '$\mathrm{Ca^{2+}}$'], \
    loc=(0.60,0.85), ncol=3, fontsize='small', handlelength=0.8, handletextpad=0.4, columnspacing=0.4)

##### Panel B2 ###
ax2.plot(t, (E_Na_sn-E_Na_sn[0])*1000, zorder=10)
ax2.plot(t, (E_K_sn-E_K_sn[0])*1000, zorder=10)
ax2.plot(t, (E_Cl_sn-E_Cl_sn[0])*1000, zorder=10)
ax2.plot(t, (E_Ca_sn-E_Ca_sn[0])*1000, zorder=10)
ax2.set_xlim(590,600)
ax2.set_title('Steady state')

##### Panel B3 ###
ax3.plot(t, (E_Na_sn-E_Na_sn[0])*1000, zorder=10)
ax3.plot(t, (E_K_sn-E_K_sn[0])*1000, zorder=10)
ax3.plot(t, (E_Cl_sn-E_Cl_sn[0])*1000, zorder=10)
ax3.plot(t, (E_Ca_sn-E_Ca_sn[0])*1000, zorder=10)
ax3.set_xlim(600,610)
ax3.set_title('Recovery')

##### Panel B4 ###
ax4.plot(t, (E_Na_sn-E_Na_sn[0])*1000, zorder=10)
ax4.plot(t, (E_K_sn-E_K_sn[0])*1000, zorder=10)
ax4.plot(t, (E_Cl_sn-E_Cl_sn[0])*1000, zorder=10)
ax4.plot(t, (E_Ca_sn-E_Ca_sn[0])*1000, zorder=10)
ax4.set_xlim(1390,1400)
ax4.set_title('Recovered')

#### Panel C1 ###
ax5.plot(t, (E_Na_sg-E_Na_sg[0])*1000, zorder=10)
ax5.plot(t, (E_K_sg-E_K_sg[0])*1000, zorder=9)
ax5.plot(t, (E_Cl_sg-E_Cl_sg[0])*1000, zorder=10)
ax5.set_ylabel('$\Delta E\mathrm{_{k,sg}}$ [mV]')
ax5.set_xlim(0,10)

#### Panel C2 ###
ax6.plot(t, (E_Na_sg-E_Na_sg[0])*1000, zorder=10)
ax6.plot(t, (E_K_sg-E_K_sg[0])*1000, zorder=9)
ax6.plot(t, (E_Cl_sg-E_Cl_sg[0])*1000, zorder=10)
#ax6.set_xlim(200,210)
ax6.set_xlim(590,600)

#### Panel C3 ###
ax7.plot(t, (E_Na_sg-E_Na_sg[0])*1000, zorder=10)
ax7.plot(t, (E_K_sg-E_K_sg[0])*1000, zorder=9)
ax7.plot(t, (E_Cl_sg-E_Cl_sg[0])*1000, zorder=10)
ax7.set_xlim(600,610)

#### Panel C4 ###
ax8.plot(t, (E_Na_sg-E_Na_sg[0])*1000, zorder=10)
ax8.plot(t, (E_K_sg-E_K_sg[0])*1000, zorder=9)
ax8.plot(t, (E_Cl_sg-E_Cl_sg[0])*1000, zorder=10)
ax8.set_xlim(1390,1400)

### Panel D1 ###
ax9.plot(t, ((V_sn+V_dn)-(V_sn[0]+V_dn[0]))/(V_sn[0]+V_dn[0])*100, 'k', label='neuron')
ax9.plot(t, ((V_se+V_de)-(V_se[0]+V_de[0]))/(V_se[0]+V_de[0])*100, 'k:', label='ECS')
ax9.plot(t, ((V_sg+V_dg)-(V_sg[0]+V_dg[0]))/(V_sg[0]+V_dg[0])*100, 'k--', label='glia')
ax9.set_ylabel('$\Delta V$ [\%]')
ax9.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='lower left', labelspacing=0.01)
ax9.set_xlim(0, 10)

### Panel D2 ###
ax10.plot(t, ((V_sn+V_dn)-(V_sn[0]+V_dn[0]))/(V_sn[0]+V_dn[0])*100, 'k')
ax10.plot(t, ((V_se+V_de)-(V_se[0]+V_de[0]))/(V_se[0]+V_de[0])*100, 'k:')
ax10.plot(t, ((V_sg+V_dg)-(V_sg[0]+V_dg[0]))/(V_sg[0]+V_dg[0])*100, 'k--')
ax10.set_xlim(590, 600)

### Panel D3 ###
ax11.plot(t, ((V_sn+V_dn)-(V_sn[0]+V_dn[0]))/(V_sn[0]+V_dn[0])*100, 'k')
ax11.plot(t, ((V_se+V_de)-(V_se[0]+V_de[0]))/(V_se[0]+V_de[0])*100, 'k:')
ax11.plot(t, ((V_sg+V_dg)-(V_sg[0]+V_dg[0]))/(V_sg[0]+V_dg[0])*100, 'k--')
ax11.set_xlim(600, 610)

### Panel D4 ###
ax12.plot(t, ((V_sn+V_dn)-(V_sn[0]+V_dn[0]))/(V_sn[0]+V_dn[0])*100, 'k')
ax12.plot(t, ((V_se+V_de)-(V_se[0]+V_de[0]))/(V_se[0]+V_de[0])*100, 'k:')
ax12.plot(t, ((V_sg+V_dg)-(V_sg[0]+V_dg[0]))/(V_sg[0]+V_dg[0])*100, 'k--')
ax12.set_xlim(1390, 1400)

for ax in [ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

for ax in [ax2, ax3, ax4, ax6, ax7, ax8, ax10, ax11, ax12]:
    plt.setp(ax.get_yticklabels(), visible=False)

for ax in [ax9, ax10, ax11, ax12]:
    ax.set_xlabel('time [s]')

# ABC
ax0.text(-0.02, 1.2, 'A', transform=ax0.transAxes, fontsize=12, fontweight='bold', va='top', ha='right')
panel = np.array(['B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4'])
i = 0
for ax in [ax1, ax2, ax3, ax4]:
    ax.text(-0.1, 1, panel[i], transform=ax.transAxes, fontsize=12, fontweight='bold', va='top', ha='right')
    i += 1
for ax in [ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12]:
    ax.text(-0.1, 1.2, panel[i], transform=ax.transAxes, fontsize=12, fontweight='bold', va='top', ha='right')
    i += 1

fig.align_ylabels([ax0, ax1,ax5,ax9])
plt.tight_layout()
plt.savefig('figure3.pdf', dpi=600)
