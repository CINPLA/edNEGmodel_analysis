import numpy as np
from scipy.ndimage import uniform_filter1d
from scipy.interpolate import interp1d
from functions.currents import *

filename = 'data/figure3.npz'
data = np.load(filename)
t = data['t']

t_fig3, av_I_cap_sn_fig3, av_I_leak_sn_fig3, av_I_pump_sn_fig3, av_I_Na_sn_fig3, av_I_DR_sn_fig3, av_I_stim_sn_fig3 = membrane_currents_sn(filename, t, stim_i=22e-12, stim_start=1, stim_end=600)
t_fig3, av_I_cap_dn_fig3, av_I_leak_dn_fig3, av_I_pump_dn_fig3, av_I_AHP_dn_fig3, av_I_Ca_dn_fig3, av_I_KC_dn_fig3 = membrane_currents_dn(filename, t)
t_fig3, av_I_cap_sg_fig3, av_I_leak_sg_fig3, av_I_pump_sg_fig3, av_I_Kir_sg_fig3 = membrane_currents_sg(filename, t)
t_fig3, av_I_cap_dg_fig3, av_I_leak_dg_fig3, av_I_pump_dg_fig3, av_I_Kir_dg_fig3 = membrane_currents_dg(filename, t)

np.savez('data/figureS1', t_fig3=t_fig3, av_I_cap_sn_fig3=av_I_cap_sn_fig3, av_I_leak_sn_fig3=av_I_leak_sn_fig3, \
    av_I_pump_sn_fig3=av_I_pump_sn_fig3, av_I_Na_sn_fig3=av_I_Na_sn_fig3, av_I_DR_sn_fig3=av_I_DR_sn_fig3, \
    av_I_stim_sn_fig3=av_I_stim_sn_fig3, \
    av_I_cap_dn_fig3=av_I_cap_dn_fig3, av_I_leak_dn_fig3=av_I_leak_dn_fig3, av_I_pump_dn_fig3=av_I_pump_dn_fig3, \
    av_I_AHP_dn_fig3=av_I_AHP_dn_fig3, av_I_Ca_dn_fig3=av_I_Ca_dn_fig3, av_I_KC_dn_fig3=av_I_KC_dn_fig3, \
    av_I_cap_sg_fig3=av_I_cap_sg_fig3, av_I_leak_sg_fig3=av_I_leak_sg_fig3, \
    av_I_pump_sg_fig3=av_I_pump_sg_fig3, av_I_Kir_sg_fig3=av_I_Kir_sg_fig3, \
    av_I_cap_dg_fig3=av_I_cap_dg_fig3, av_I_leak_dg_fig3=av_I_leak_dg_fig3, \
    av_I_pump_dg_fig3=av_I_pump_dg_fig3, av_I_Kir_dg_fig3=av_I_Kir_dg_fig3)
