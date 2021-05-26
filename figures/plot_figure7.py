import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from set_style import set_style

set_style('default', w=1, h=3.5)

fig = plt.figure()
gs = gridspec.GridSpec(6,6)
ax1 = plt.subplot(gs[0:2,:])
ax2 = plt.subplot(gs[2:4,0:3])
ax3 = plt.subplot(gs[2:4,3:], sharey=ax2)
ax4 = plt.subplot(gs[4:,0:2])
ax5 = plt.subplot(gs[4:,2:4], sharey=ax4)
ax6 = plt.subplot(gs[4:,4:], sharey=ax4)

### Panel A ###
data = np.load('../data/figure7_syn_soma_ss_1.npz')
t = data['t']
phi_m = data['phi_msn']
ax1.plot(t, phi_m*1000, 'k')[0]
ax1.set_yticks([-70, 0])
ax1.set_xlim(0,10)

### Panel B ###
phi_e_sum = data['phi_e_n']+data['phi_e_g']+data['phi_e_diff'][:-1]
ax2.plot(t[:-1], phi_e_sum*1000, 'k')[0]
ax2.set_xlim(0,60)
ax2.set_title('Physiological')

### Panel C ###
data = np.load('../data/figure7_syn_soma_db_1.npz')
t = data['t']
phi_e_sum = data['phi_e_n']+data['phi_e_g']+data['phi_e_diff'][:-1]
ax3.plot(t[:-1], phi_e_sum*1000, 'k')[0]
ax3.set_xlim(0,600)
ax3.set_title('Pathological')

data = np.load('../data/figure7.npz')

syn_rate_soma_ss = data['syn_rate_soma_ss']
n_soma_ss = data['n_soma_ss']
g_soma_ss = data['g_soma_ss']
diff_soma_ss = data['diff_soma_ss']
syn_rate_soma_db = data['syn_rate_soma_db']
n_soma_db = data['n_soma_db']
g_soma_db = data['g_soma_db']
diff_soma_db = data['diff_soma_db']

syn_rate_dendrite_ss = data['syn_rate_dendrite_ss']
n_dendrite_ss = data['n_dendrite_ss']
g_dendrite_ss = data['g_dendrite_ss']
diff_dendrite_ss = data['diff_dendrite_ss']
syn_rate_dendrite_db = data['syn_rate_dendrite_db']
n_dendrite_db = data['n_dendrite_db']
g_dendrite_db = data['g_dendrite_db']
diff_dendrite_db = data['diff_dendrite_db']

syn_rate_both_ss = data['syn_rate_both_ss']
n_both_ss = data['n_both_ss']
g_both_ss = data['g_both_ss']
diff_both_ss = data['diff_both_ss']
syn_rate_both_db = data['syn_rate_both_db']
n_both_db = data['n_both_db']
g_both_db = data['g_both_db']
diff_both_db = data['diff_both_db']

### Panel D ###
l1 = ax4.plot(syn_rate_soma_ss, n_soma_ss, 'o-', color='k', markersize=3)[0]
l2 = ax4.plot(syn_rate_soma_ss, g_soma_ss, 'v-', color='tab:purple', markersize=3)[0]
l3 = ax4.plot(syn_rate_soma_ss, diff_soma_ss, '*-', color='tab:red', markersize=3)[0]
l4 = ax4.plot(syn_rate_soma_ss, n_soma_ss+g_soma_ss+diff_soma_ss, 'k--', markersize=3)[0]
ax4.plot(syn_rate_soma_db, n_soma_db, 'o-', color='k', markersize=3)[0]
ax4.plot(syn_rate_soma_db, g_soma_db, 'v-', color='tab:purple', markersize=3)[0]
ax4.plot(syn_rate_soma_db, diff_soma_db, '*-', color='tab:red', markersize=3)[0]
ax4.plot(syn_rate_soma_db, n_soma_db+g_soma_db+diff_soma_db, 'k--', markersize=3)[0]
ax4.set_title('soma')
fig.legend([l1, l2, l3, l4], [r'$\bar{\phi}\mathrm{_{se,n}}$', r'$\bar{\phi}\mathrm{_{se,g}}$', r'$\bar{\phi}\mathrm{_{se,diff}}$', r'$\bar{\phi}\mathrm{_{se,sum}}$'], \
    loc=(0.2,0.3), ncol=4, fontsize='large', handlelength=0.9, handletextpad=0.4, columnspacing=0.4)

### Panel E ###
ax5.plot(syn_rate_dendrite_ss, n_dendrite_ss, 'o-', color='k', markersize=3)[0]
ax5.plot(syn_rate_dendrite_ss, g_dendrite_ss, 'v-', color='tab:purple', markersize=3)[0]
ax5.plot(syn_rate_dendrite_ss, diff_dendrite_ss, '*-', color='tab:red', markersize=3)[0]
ax5.plot(syn_rate_dendrite_ss, n_dendrite_ss+g_dendrite_ss+diff_dendrite_ss, 'k--', markersize=3)[0]
ax5.plot(syn_rate_dendrite_db, n_dendrite_db, 'o-', color='k', markersize=3)[0]
ax5.plot(syn_rate_dendrite_db, g_dendrite_db, 'v-', color='tab:purple', markersize=3)[0]
ax5.plot(syn_rate_dendrite_db, diff_dendrite_db, '*-', color='tab:red', markersize=3)[0]
ax5.plot(syn_rate_dendrite_db, n_dendrite_db+g_dendrite_db+diff_dendrite_db, 'k--', markersize=3)[0]
ax5.set_title('dendrite')

### Panel E ###
ax6.plot(syn_rate_both_ss, n_both_ss, 'o-', color='k', markersize=3)[0]
ax6.plot(syn_rate_both_ss, g_both_ss, 'v-', color='tab:purple', markersize=3)[0]
ax6.plot(syn_rate_both_ss, diff_both_ss, '*-', color='tab:red', markersize=3)[0]
ax6.plot(syn_rate_both_ss, n_both_ss+g_both_ss+diff_both_ss, 'k--', markersize=3)[0]
ax6.plot(syn_rate_both_db, n_both_db, 'o-', color='k', markersize=3)[0]
ax6.plot(syn_rate_both_db, g_both_db, 'v-', color='tab:purple', markersize=3)[0]
ax6.plot(syn_rate_both_db, diff_both_db, '*-', color='tab:red', markersize=3)[0]
ax6.plot(syn_rate_both_db, n_both_db+g_both_db+diff_both_db, 'k--', markersize=3)[0]
ax6.set_title('both')

for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

ax4.set_xlim(300,1000)
ax5.set_xlim(400,1100)
ax6.set_xlim(150,500)
t4 = [300,500,700,900]
ax4.set_xticks(t4)
ax4.set_xticklabels(t4, rotation=30)
t5 = [400,600,800,1000]
ax5.set_xticks(t5)
ax5.set_xticklabels(t5, rotation=30)
t6 = [200, 300, 400, 500]
ax6.set_xticks(t6)
ax6.set_xticklabels(t6, rotation=30)

ax1.set_ylabel(r'$\phi\mathrm{_{msn}}$ [mV]')
ax2.set_ylabel(r'$\phi\mathrm{_{se,sum}}$ [mV]')
ax4.set_ylabel(r'$\bar{\phi}\mathrm{_{se}}$ [mV]')
for ax in [ax1, ax2, ax3]:
    ax.set_xlabel('time [s]')
for ax in [ax4, ax5, ax6]:
    ax.set_xlabel('input rate [Hz]')

## ABC
panel = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
i = 0
for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    ax.text(-0.1, 1.2, panel[i], transform=ax.transAxes, fontsize=12, fontweight='bold', va='top', ha='right')
    i += 1

plt.tight_layout()
plt.savefig('figure7.pdf', dpi=600)

