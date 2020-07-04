import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from set_style import set_style

set_style('default', w=1, h=3)

fig = plt.figure()
gs = gridspec.GridSpec(3,4)
ax1 = plt.subplot(gs[0,0:2])
ax2 = plt.subplot(gs[0,2:])
ax3 = plt.subplot(gs[1,0:2])
ax4 = plt.subplot(gs[1,2:])
ax5 = plt.subplot(gs[2,:])

data_edNEG_weak = np.load('../data/figure2_edNEG_weak.npz')
data_PR_weak = np.load('../data/figure2_PR_weak.npz')
data_edNEG_strong = np.load('../data/figure2_edNEG_strong.npz')
data_PR_strong = np.load('../data/figure2_PR_strong.npz')

edNEG_weak_t = data_edNEG_weak['t']
edNEG_weak_msn = data_edNEG_weak['phi_msn']
edNEG_weak_mdn = data_edNEG_weak['phi_mdn']

PR_weak_t = data_PR_weak['t']
PR_weak_msn = data_PR_weak['Vs']
PR_weak_mdn = data_PR_weak['Vd']

edNEG_strong_t = data_edNEG_strong['t']
edNEG_strong_msn = data_edNEG_strong['phi_msn']
edNEG_strong_mdn = data_edNEG_strong['phi_mdn']
edNEG_strong_msg = data_edNEG_strong['phi_msg']

PR_strong_t = data_PR_strong['t']
PR_strong_msn = data_PR_strong['Vs']
PR_strong_mdn = data_PR_strong['Vd']

### Panel A ###
ax1.plot(PR_weak_t/1000, PR_weak_msn, 'k', label='soma')
ax1.plot(PR_weak_t/1000, PR_weak_mdn, 'k:', label='dendrite')
ax1.set_xlim([16.52,16.56])
ax1.set_ylabel('mV')
ax1.set_title('PR (weak)')
ax1.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper right')

### Panel B ###
ax2.plot(PR_strong_t/1000, PR_strong_msn, 'k')
ax2.plot(PR_strong_t/1000, PR_strong_mdn, 'k:')
ax2.set_xlim([10.06,10.10])
ax2.set_xticks([10.06, 10.08, 10.10])
ax2.set_title('PR (strong)')

### Panel C ###
ax3.plot(edNEG_weak_t, edNEG_weak_msn*1000, 'k')
ax3.plot(edNEG_weak_t, edNEG_weak_mdn*1000, 'k:')
ax3.set_xlim([16.58,16.62])
ax3.set_ylabel('mV')
ax3.set_xticks([16.58, 16.60, 16.62])
ax3.set_title('edNEG (weak)')
ax3.set_xlabel('time [s]')

### Panel D ###
ax4.plot(edNEG_strong_t, edNEG_strong_msn*1000, 'k')
ax4.plot(edNEG_strong_t, edNEG_strong_mdn*1000, 'k:')
ax4.set_xlim([10.0,10.04])
ax4.set_xticks([10.0, 10.02, 10.04])
ax4.set_title('edNEG (strong)')
ax4.set_xlabel('time [s]')

### Panel E ###
ax5.plot(edNEG_strong_t, edNEG_strong_msn*1000, 'k', label='neuron')
ax5.plot(edNEG_strong_t, edNEG_strong_msg*1000, '#9467bd', label='glia')
ax5.set_xlim([0,30])
ax5.set_xlabel('time [s]')
ax5.set_ylabel('mV')
ax5.legend(fontsize='small', handlelength=0.8, handletextpad=0.4, loc='upper right')
ax5.set_title('$\phi\mathrm{_{ms}}$')

for ax in [ax1, ax2, ax3, ax4]:
    ax.set_yticks([-70, 0, 20])
    ax.set_ylim(-75,25)

ax5.set_ylim(-90,25)
ax5.set_yticks([-70, 0, 20])

for ax in [ax1, ax2, ax3, ax4, ax5]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

panel = np.array(['A', 'B', 'C', 'D', 'E'])
ax5.text(-0.06, 1.1, panel[4], transform=ax5.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
i = 0
for ax in [ax1, ax2, ax3, ax4]:
            ax.text(-0.15, 1.1, panel[i], transform=ax.transAxes, fontsize=16, fontweight='bold', va='top', ha='right')
            i += 1

fig.align_ylabels([ax1, ax3, ax5])
plt.tight_layout()
plt.savefig('figure2.pdf', dpi=600)
