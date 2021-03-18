import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from set_style import set_style

set_style('default', w=1, h=3.3)

fig = plt.figure()
gs = gridspec.GridSpec(8,6)
ax00 = plt.subplot(gs[0:2,0:2])
ax0 = plt.subplot(gs[0:2,2:4])
ax1 = plt.subplot(gs[2:4,0:2])
ax2 = plt.subplot(gs[2:4,2:4], sharey=ax1)
ax3 = plt.subplot(gs[2:4,4:], sharey=ax1)
ax4 = plt.subplot(gs[4:6,0:2])
ax5 = plt.subplot(gs[4:6,2:4], sharey=ax4)
ax6 = plt.subplot(gs[4:6,4:], sharey=ax4)
ax7 = plt.subplot(gs[6:,0:2])
ax8 = plt.subplot(gs[6:,2:4], sharey=ax7)
ax9 = plt.subplot(gs[6:,4:], sharey=ax7)

### Panel A ###
data = np.load('../data/figure6_K_soma_ss_1.npz')
t = data['t']
phi_e_sum = data['phi_e_n']+data['phi_e_g']+data['phi_e_diff'][:-1]
ax00.plot(t[:-1], phi_e_sum*1000, 'k')[0]
ax00.set_xlim(0,60)
ax00.set_title('Physiological')

### Panel B ###
data = np.load('../data/figure6_K_soma_db_1.npz')
t = data['t']
phi_e_sum = data['phi_e_n']+data['phi_e_g']+data['phi_e_diff'][:-1]
ax0.plot(t[:-1], phi_e_sum*1000, 'k')[0]
ax0.set_xlim(0,600)
ax0.set_title('Pathological')

data = np.load('../data/figure6.npz')

I_stim_K_soma_ss = data['I_stim_K_soma_ss']
n_K_soma_ss = data['n_K_soma_ss']
g_K_soma_ss = data['g_K_soma_ss']
diff_K_soma_ss = data['diff_K_soma_ss']
I_stim_K_soma_db = data['I_stim_K_soma_db']
n_K_soma_db = data['n_K_soma_db']
g_K_soma_db = data['g_K_soma_db']
diff_K_soma_db = data['diff_K_soma_db']

I_stim_K_dendrite_ss = data['I_stim_K_dendrite_ss']
n_K_dendrite_ss = data['n_K_dendrite_ss']
g_K_dendrite_ss = data['g_K_dendrite_ss']
diff_K_dendrite_ss = data['diff_K_dendrite_ss']
I_stim_K_dendrite_db = data['I_stim_K_dendrite_db']
n_K_dendrite_db = data['n_K_dendrite_db']
g_K_dendrite_db = data['g_K_dendrite_db']
diff_K_dendrite_db = data['diff_K_dendrite_db']

I_stim_K_both_ss = data['I_stim_K_both_ss']
n_K_both_ss = data['n_K_both_ss']
g_K_both_ss = data['g_K_both_ss']
diff_K_both_ss = data['diff_K_both_ss']
I_stim_K_both_db = data['I_stim_K_both_db']
n_K_both_db = data['n_K_both_db']
g_K_both_db = data['g_K_both_db']
diff_K_both_db = data['diff_K_both_db']

I_stim_Na_soma_ss = data['I_stim_Na_soma_ss']
n_Na_soma_ss = data['n_Na_soma_ss']
g_Na_soma_ss = data['g_Na_soma_ss']
diff_Na_soma_ss = data['diff_Na_soma_ss']
I_stim_Na_soma_db = data['I_stim_Na_soma_db']
n_Na_soma_db = data['n_Na_soma_db']
g_Na_soma_db = data['g_Na_soma_db']
diff_Na_soma_db = data['diff_Na_soma_db']

I_stim_Na_dendrite_ss = data['I_stim_Na_dendrite_ss']
n_Na_dendrite_ss = data['n_Na_dendrite_ss']
g_Na_dendrite_ss = data['g_Na_dendrite_ss']
diff_Na_dendrite_ss = data['diff_Na_dendrite_ss']
I_stim_Na_dendrite_db = data['I_stim_Na_dendrite_db']
n_Na_dendrite_db = data['n_Na_dendrite_db']
g_Na_dendrite_db = data['g_Na_dendrite_db']
diff_Na_dendrite_db = data['diff_Na_dendrite_db']

I_stim_Na_both_ss = data['I_stim_Na_both_ss']
n_Na_both_ss = data['n_Na_both_ss']
g_Na_both_ss = data['g_Na_both_ss']
diff_Na_both_ss = data['diff_Na_both_ss']
I_stim_Na_both_db = data['I_stim_Na_both_db']
n_Na_both_db = data['n_Na_both_db']
g_Na_both_db = data['g_Na_both_db']
diff_Na_both_db = data['diff_Na_both_db']

I_stim_Cl_soma_ss = data['I_stim_Cl_soma_ss']
n_Cl_soma_ss = data['n_Cl_soma_ss']
g_Cl_soma_ss = data['g_Cl_soma_ss']
diff_Cl_soma_ss = data['diff_Cl_soma_ss']
I_stim_Cl_soma_db = data['I_stim_Cl_soma_db']
n_Cl_soma_db = data['n_Cl_soma_db']
g_Cl_soma_db = data['g_Cl_soma_db']
diff_Cl_soma_db = data['diff_Cl_soma_db']

I_stim_Cl_dendrite_ss = data['I_stim_Cl_dendrite_ss']
n_Cl_dendrite_ss = data['n_Cl_dendrite_ss']
g_Cl_dendrite_ss = data['g_Cl_dendrite_ss']
diff_Cl_dendrite_ss = data['diff_Cl_dendrite_ss']
I_stim_Cl_dendrite_db = data['I_stim_Cl_dendrite_db']
n_Cl_dendrite_db = data['n_Cl_dendrite_db']
g_Cl_dendrite_db = data['g_Cl_dendrite_db']
diff_Cl_dendrite_db = data['diff_Cl_dendrite_db']

I_stim_Cl_both_ss = data['I_stim_Cl_both_ss']
n_Cl_both_ss = data['n_Cl_both_ss']
g_Cl_both_ss = data['g_Cl_both_ss']
diff_Cl_both_ss = data['diff_Cl_both_ss']
I_stim_Cl_both_db = data['I_stim_Cl_both_db']
n_Cl_both_db = data['n_Cl_both_db']
g_Cl_both_db = data['g_Cl_both_db']
diff_Cl_both_db = data['diff_Cl_both_db']

###### Panel C ###
l1 = ax1.plot(I_stim_K_soma_ss, n_K_soma_ss, 'o-', color='k', markersize=3)[0]
l2 = ax1.plot(I_stim_K_soma_ss, g_K_soma_ss, 'v-', color='tab:purple', markersize=3)[0]
l3 = ax1.plot(I_stim_K_soma_ss, diff_K_soma_ss, '*-', color='tab:red', markersize=3)[0]
l4 = ax1.plot(I_stim_K_soma_ss, n_K_soma_ss+g_K_soma_ss+diff_K_soma_ss, 'k--', markersize=3)[0]
ax1.plot(I_stim_K_soma_db, n_K_soma_db, 'o-', color='k', markersize=3)[0]
ax1.plot(I_stim_K_soma_db, g_K_soma_db, 'v-', color='tab:purple', markersize=3)[0]
ax1.plot(I_stim_K_soma_db, diff_K_soma_db, '*-', color='tab:red', markersize=3)[0]
ax1.plot(I_stim_K_soma_db, n_K_soma_db+g_K_soma_db+diff_K_soma_db, 'k--', markersize=3)[0]
ax1.set_title('K$^+$, soma')
fig.legend([l1, l2, l3, l4], [r'$\bar{\phi}\mathrm{_{se,n}}$', r'$\bar{\phi}\mathrm{_{se,g}}$', r'$\bar{\phi}\mathrm{_{se,diff}}$', r'$\bar{\phi}\mathrm{_{se,sum}}$'], \
    loc=(0.75,0.77), ncol=1, fontsize='large', handlelength=0.9, handletextpad=0.4)

### Panel D ###
ax2.plot(I_stim_K_dendrite_ss, n_K_dendrite_ss, 'o-', color='k', markersize=3)[0]
ax2.plot(I_stim_K_dendrite_ss, g_K_dendrite_ss, 'v-', color='tab:purple', markersize=3)[0]
ax2.plot(I_stim_K_dendrite_ss, diff_K_dendrite_ss, '*-', color='tab:red', markersize=3)[0]
ax2.plot(I_stim_K_dendrite_ss, n_K_dendrite_ss+g_K_dendrite_ss+diff_K_dendrite_ss, 'k--', markersize=3)[0]
ax2.plot(I_stim_K_dendrite_db, n_K_dendrite_db, 'o-', color='k', markersize=3)[0]
ax2.plot(I_stim_K_dendrite_db, g_K_dendrite_db, 'v-', color='tab:purple', markersize=3)[0]
ax2.plot(I_stim_K_dendrite_db, diff_K_dendrite_db, '*-', color='tab:red', markersize=3)[0]
ax2.plot(I_stim_K_dendrite_db, n_K_dendrite_db+g_K_dendrite_db+diff_K_dendrite_db, 'k--', markersize=3)[0]
ax2.set_title('K$^+$, dendrite')

### Panel E ###
ax3.plot(I_stim_K_both_ss, n_K_both_ss, 'o-', color='k', markersize=3)[0]
ax3.plot(I_stim_K_both_ss, g_K_both_ss, 'v-', color='tab:purple', markersize=3)[0]
ax3.plot(I_stim_K_both_ss, diff_K_both_ss, '*-', color='tab:red', markersize=3)[0]
ax3.plot(I_stim_K_both_ss, n_K_both_ss+g_K_both_ss+diff_K_both_ss, 'k--', markersize=3)[0]
ax3.plot(I_stim_K_both_db, n_K_both_db, 'o-', color='k', markersize=3)[0]
ax3.plot(I_stim_K_both_db, g_K_both_db, 'v-', color='tab:purple', markersize=3)[0]
ax3.plot(I_stim_K_both_db, diff_K_both_db, '*-', color='tab:red', markersize=3)[0]
ax3.plot(I_stim_K_both_db, n_K_both_db+g_K_both_db+diff_K_both_db, 'k--', markersize=3)[0]
ax3.set_title('K$^+$, both')

### Panel F ###
ax4.plot(I_stim_Na_soma_ss, n_Na_soma_ss, 'o-', color='k', markersize=3)[0]
ax4.plot(I_stim_Na_soma_ss, g_Na_soma_ss, 'v-', color='tab:purple', markersize=3)[0]
ax4.plot(I_stim_Na_soma_ss, diff_Na_soma_ss, '*-', color='tab:red', markersize=3)[0]
ax4.plot(I_stim_Na_soma_ss, n_Na_soma_ss+g_Na_soma_ss+diff_Na_soma_ss, 'k--', markersize=3)[0]
ax4.plot(I_stim_Na_soma_db, n_Na_soma_db, 'o-', color='k', markersize=3)[0]
ax4.plot(I_stim_Na_soma_db, g_Na_soma_db, 'v-', color='tab:purple', markersize=3)[0]
ax4.plot(I_stim_Na_soma_db, diff_Na_soma_db, '*-', color='tab:red', markersize=3)[0]
ax4.plot(I_stim_Na_soma_db, n_Na_soma_db+g_Na_soma_db+diff_Na_soma_db, 'k--', markersize=3)[0]
ax4.set_title('Na$^+$, soma')

### Panel G ###
ax5.plot(I_stim_Na_dendrite_ss, n_Na_dendrite_ss, 'o-', color='k', markersize=3)[0]
ax5.plot(I_stim_Na_dendrite_ss, g_Na_dendrite_ss, 'v-', color='tab:purple', markersize=3)[0]
ax5.plot(I_stim_Na_dendrite_ss, diff_Na_dendrite_ss, '*-', color='tab:red', markersize=3)[0]
ax5.plot(I_stim_Na_dendrite_ss, n_Na_dendrite_ss+g_Na_dendrite_ss+diff_Na_dendrite_ss, 'k--', markersize=3)[0]
ax5.plot(I_stim_Na_dendrite_db, n_Na_dendrite_db, 'o-', color='k', markersize=3)[0]
ax5.plot(I_stim_Na_dendrite_db, g_Na_dendrite_db, 'v-', color='tab:purple', markersize=3)[0]
ax5.plot(I_stim_Na_dendrite_db, diff_Na_dendrite_db, '*-', color='tab:red', markersize=3)[0]
ax5.plot(I_stim_Na_dendrite_db, n_Na_dendrite_db+g_Na_dendrite_db+diff_Na_dendrite_db, 'k--', markersize=3)[0]
ax5.set_title('Na$^+$, dendrite')

### Panel H ###
ax6.plot(I_stim_Na_both_ss, n_Na_both_ss, 'o-', color='k', markersize=3)[0]
ax6.plot(I_stim_Na_both_ss, g_Na_both_ss, 'v-', color='tab:purple', markersize=3)[0]
ax6.plot(I_stim_Na_both_ss, diff_Na_both_ss, '*-', color='tab:red', markersize=3)[0]
ax6.plot(I_stim_Na_both_ss, n_Na_both_ss+g_Na_both_ss+diff_Na_both_ss, 'k--', markersize=3)[0]
ax6.plot(I_stim_Na_both_db, n_Na_both_db, 'o-', color='k', markersize=3)[0]
ax6.plot(I_stim_Na_both_db, g_Na_both_db, 'v-', color='tab:purple', markersize=3)[0]
ax6.plot(I_stim_Na_both_db, diff_Na_both_db, '*-', color='tab:red', markersize=3)[0]
ax6.plot(I_stim_Na_both_db, n_Na_both_db+g_Na_both_db+diff_Na_both_db, 'k--', markersize=3)[0]
ax6.set_title('Na$^+$, both')

### Panel I ###
ax7.plot(I_stim_Cl_soma_ss, n_Cl_soma_ss, 'o-', color='k', markersize=3)[0]
ax7.plot(I_stim_Cl_soma_ss, g_Cl_soma_ss, 'v-', color='tab:purple', markersize=3)[0]
ax7.plot(I_stim_Cl_soma_ss, diff_Cl_soma_ss, '*-', color='tab:red', markersize=3)[0]
ax7.plot(I_stim_Cl_soma_ss, n_Cl_soma_ss+g_Cl_soma_ss+diff_Cl_soma_ss, 'k--', markersize=3)[0]
ax7.plot(I_stim_Cl_soma_db, n_Cl_soma_db, 'o-', color='k', markersize=3)[0]
ax7.plot(I_stim_Cl_soma_db, g_Cl_soma_db, 'v-', color='tab:purple', markersize=3)[0]
ax7.plot(I_stim_Cl_soma_db, diff_Cl_soma_db, '*-', color='tab:red', markersize=3)[0]
ax7.plot(I_stim_Cl_soma_db, n_Cl_soma_db+g_Cl_soma_db+diff_Cl_soma_db, 'k--', markersize=3)[0]
ax7.set_title('Cl$^-$, soma')

### Panel J ###
ax8.plot(I_stim_Cl_dendrite_ss, n_Cl_dendrite_ss, 'o-', color='k', markersize=3)[0]
ax8.plot(I_stim_Cl_dendrite_ss, g_Cl_dendrite_ss, 'v-', color='tab:purple', markersize=3)[0]
ax8.plot(I_stim_Cl_dendrite_ss, diff_Cl_dendrite_ss, '*-', color='tab:red', markersize=3)[0]
ax8.plot(I_stim_Cl_dendrite_ss, n_Cl_dendrite_ss+g_Cl_dendrite_ss+diff_Cl_dendrite_ss, 'k--', markersize=3)[0]
ax8.plot(I_stim_Cl_dendrite_db, n_Cl_dendrite_db, 'o-', color='k', markersize=3)[0]
ax8.plot(I_stim_Cl_dendrite_db, g_Cl_dendrite_db, 'v-', color='tab:purple', markersize=3)[0]
ax8.plot(I_stim_Cl_dendrite_db, diff_Cl_dendrite_db, '*-', color='tab:red', markersize=3)[0]
ax8.plot(I_stim_Cl_dendrite_db, n_Cl_dendrite_db+g_Cl_dendrite_db+diff_Cl_dendrite_db, 'k--', markersize=3)[0]
ax8.set_title('Cl$^-$, dendrite')

### Panel K ###
ax9.plot(I_stim_Cl_both_ss, n_Cl_both_ss, 'o-', color='k', markersize=3)[0]
ax9.plot(I_stim_Cl_both_ss, g_Cl_both_ss, 'v-', color='tab:purple', markersize=3)[0]
ax9.plot(I_stim_Cl_both_ss, diff_Cl_both_ss, '*-', color='tab:red', markersize=3)[0]
ax9.plot(I_stim_Cl_both_ss, n_Cl_both_ss+g_Cl_both_ss+diff_Cl_both_ss, 'k--', markersize=3)[0]
ax9.plot(I_stim_Cl_both_db, n_Cl_both_db, 'o-', color='k', markersize=3)[0]
ax9.plot(I_stim_Cl_both_db, g_Cl_both_db, 'v-', color='tab:purple', markersize=3)[0]
ax9.plot(I_stim_Cl_both_db, diff_Cl_both_db, '*-', color='tab:red', markersize=3)[0]
ax9.plot(I_stim_Cl_both_db, n_Cl_both_db+g_Cl_both_db+diff_Cl_both_db, 'k--', markersize=3)[0]
ax9.set_title('Cl$^-$, both')

for ax in [ax00, ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

ax00.set_ylabel('$\phi_\mathrm{{se,sum}}$ [mV]')
ax00.set_xticks([0,20,40,60])
ax0.set_xticks([0,200,400,600])
ax1.set_xlim(90,160)
ax1.set_xticks([100,120,140,160])
ax2.set_xlim(90,160)
ax2.set_xticks([100,120,140,160])
ax3.set_xlim(30,100)
ax3.set_xticks([40,60,80,100])
ax4.set_xlim(70,140)
ax4.set_xticks([80,120,100,140])
ax5.set_xlim(70,140)
ax5.set_xticks([80,120,100,140])
ax6.set_xlim(20,90)
ax6.set_xticks([30,50,70,90])
ax7.set_xlim(50,120)
ax7.set_xticks([60,80,100,120])
ax8.set_xlim(50,120)
ax8.set_xticks([60,80,100,120])
ax9.set_xlim(10,80)
ax9.set_xticks([20,40,60,80])

for ax in [ax1, ax4, ax7]:
    ax.set_yticks([-2, -1, 0])

for ax in [ax1, ax4, ax7]:
    ax.set_ylabel(r'$\bar{\phi}\mathrm{_{se}}$ [mV]')
for ax in [ax00, ax0]:
    ax.set_xlabel('time [s]')
for ax in [ax7, ax8, ax9]:
    ax.set_xlabel('$I\mathrm{_{stim}}$ [pA]')

## ABC
panel = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
i = 0
for ax in [ax00, ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]:
    ax.text(-0.1, 1.2, panel[i], transform=ax.transAxes, fontsize=12, fontweight='bold', va='top', ha='right')
    i += 1

plt.tight_layout()
plt.savefig('figure6.pdf', dpi=600)
