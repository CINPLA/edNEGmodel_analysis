import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
from set_style import set_style

set_style('default', w=1, h=2)

fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2,2)

data = np.load('../data/figureS1.npz')

t = data['t_fig3']

av_I_cap_sn_fig3 = data['av_I_cap_sn_fig3'] 
av_I_leak_sn_fig3 = data['av_I_leak_sn_fig3']
av_I_pump_sn_fig3 = data['av_I_pump_sn_fig3']
av_I_Na_sn_fig3 = data['av_I_Na_sn_fig3']
av_I_DR_sn_fig3 = data['av_I_DR_sn_fig3']
av_I_stim_sn_fig3 = data['av_I_stim_sn_fig3']

av_I_cap_dn_fig3 = data['av_I_cap_dn_fig3']
av_I_leak_dn_fig3 = data['av_I_leak_dn_fig3']
av_I_pump_dn_fig3 = data['av_I_pump_dn_fig3']
av_I_AHP_dn_fig3 = data['av_I_AHP_dn_fig3']
av_I_Ca_dn_fig3 = data['av_I_Ca_dn_fig3']
av_I_KC_dn_fig3 = data['av_I_KC_dn_fig3']

av_I_cap_sg_fig3 = data['av_I_cap_sg_fig3']
av_I_leak_sg_fig3 = data['av_I_leak_sg_fig3']
av_I_pump_sg_fig3 = data['av_I_pump_sg_fig3']
av_I_Kir_sg_fig3 = data['av_I_Kir_sg_fig3']

av_I_cap_dg_fig3 = data['av_I_cap_dg_fig3']
av_I_leak_dg_fig3 = data['av_I_leak_dg_fig3']
av_I_pump_dg_fig3 = data['av_I_pump_dg_fig3']
av_I_Kir_dg_fig3 = data['av_I_Kir_dg_fig3']

ax1.plot(t[:-1], av_I_cap_sn_fig3*1e12, zorder=10, label='$I\mathrm{_{cap}}$')
ax1.plot(t, av_I_leak_sn_fig3*1e12, zorder=10, label='$I\mathrm{_{leak}}$')
ax1.plot(t, av_I_pump_sn_fig3*1e12, zorder=10, label='$I\mathrm{_{pump}}$')
ax1.plot(t, av_I_Na_sn_fig3*1e12, zorder=10, label='$I\mathrm{_{Na}}$')
ax1.plot(t, av_I_DR_sn_fig3*1e12, zorder=10, label='$I\mathrm{_{DR}}$')
ax1.plot(t, av_I_stim_sn_fig3*1e12, zorder=10, label='$I\mathrm{_{stim}}$') 
ax1.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper right')
ax1.set_ylabel('[pA]')
ax1.set_title('neuron, soma-layer')

ax2.plot(t[:-1], av_I_cap_dn_fig3*1e12, zorder=10, label='$I\mathrm{_{cap}}$')
ax2.plot(t, av_I_leak_dn_fig3*1e12, zorder=10, label='$I\mathrm{_{leak}}$')
ax2.plot(t, av_I_pump_dn_fig3*1e12, zorder=10, label='$I\mathrm{_{pump}}$')
ax2.plot(t, av_I_AHP_dn_fig3*1e12, zorder=10, label='$I\mathrm{_{AHP}}$')
ax2.plot(t, av_I_Ca_dn_fig3*1e12, zorder=10, label='$I\mathrm{_{Ca}}$')
ax2.plot(t, av_I_KC_dn_fig3*1e12, zorder=10, label='$I\mathrm{_{KC}}$')
ax2.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper right')
ax2.set_title('neuron, dendrite-layer')

ax3.plot(t[:-1], av_I_cap_sg_fig3*1e12, zorder=10, label='$I\mathrm{_{cap}}$')
ax3.plot(t, av_I_leak_sg_fig3*1e12, zorder=10, label='$I\mathrm{_{leak}}$')
ax3.plot(t, av_I_pump_sg_fig3*1e12, zorder=10, label='$I\mathrm{_{pump}}$')
ax3.plot(t, av_I_Kir_sg_fig3*1e12, zorder=10, label='$I\mathrm{_{Kir}}$')
ax3.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper right')
ax3.set_title('glia, soma-layer')
ax3.set_ylabel('[pA]')

ax4.plot(t[:-1], av_I_cap_dg_fig3*1e12, zorder=10, label='$I\mathrm{_{cap}}$')
ax4.plot(t, av_I_leak_dg_fig3*1e12, zorder=10, label='$I\mathrm{_{leak}}$')
ax4.plot(t, av_I_pump_dg_fig3*1e12, zorder=10, label='$I\mathrm{_{pump}}$')
ax4.plot(t, av_I_Kir_dg_fig3*1e12, zorder=10, label='$I\mathrm{_{Kir}}$')
ax4.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper right')
ax4.set_title('glia, dendrite-layer')

ax3.set_xlabel('time [s]')
ax4.set_xlabel('time [s]')

for ax in [ax1, ax2]:
    ax.set_ylim([-25, 25])
    ax.set_yticks([-20, -10, 0, 10, 20])
for ax in [ax3, ax4]:
    ax.set_ylim([-100, 80])
    ax.set_yticks([-90, -60, -30, 0, 30, 60])

for ax in [ax1, ax2, ax3, ax4]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim([0, 1400])
    ax.set_xticks([0, 300, 600, 900, 1200])

panel = np.array(['A', 'B', 'C', 'D'])
i = 0
for ax in [ax1, ax2, ax3, ax4]:
    ax.text(-0.05, 1.2, panel[i], transform=ax.transAxes, fontsize=12, fontweight='bold', va='top', ha='right')
    i += 1

plt.tight_layout()
plt.savefig('figureS1.eps', dpi=600)
