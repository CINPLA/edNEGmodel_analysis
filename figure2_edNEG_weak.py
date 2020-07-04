import numpy as np
import time
import matplotlib.pyplot as plt
from edNEGmodel.edNEGmodel import *
from functions.solve_edNEGmodel import *
from functions.print_final_values import *

start_time = time.time()

t_dur = 30      # [s]
alpha = 0.51
I_stim = 44e-12 # [A]
stim_start = 10 # [s]
stim_end = 20   # [s]

sol, my_cell = solve_edNEGmodel(t_dur, alpha, I_stim, stim_start, stim_end)

t = sol.t

phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

print_final_values(my_cell)
print("----------------------------")
print('elapsed time: ', round(time.time() - start_time, 1), 'seconds')

f1 = plt.figure(1)
plt.plot(t, phi_msn*1000, '-', label='soma')
plt.plot(t, phi_mdn*1000, '-', label='dendrite')
plt.title('Neuronal membrane potentials')
plt.xlabel('time [s]')
plt.ylabel('[mV]')
plt.legend(loc='upper right')

# save to file
np.savez('data/figure2_edNEG_weak', t=t, phi_sn=phi_sn, phi_se=phi_se, phi_dn=phi_dn, phi_de=phi_de, phi_sg=phi_sg, phi_dg=phi_dg, \
    phi_msn=phi_msn, phi_mdn=phi_mdn, phi_msg=phi_msg, phi_mdg=phi_mdg, \
    E_Na_sn=E_Na_sn, E_Na_dn=E_Na_dn, E_Na_sg=E_Na_sg, E_Na_dg=E_Na_dg, \
    E_K_sn=E_K_sn, E_K_dn=E_K_dn, E_K_sg=E_K_sg, E_K_dg=E_K_dg, \
    E_Cl_sn=E_Cl_sn, E_Cl_dn=E_Cl_dn, E_Cl_sg=E_Cl_sg, E_Cl_dg=E_Cl_dg, \
    E_Ca_sn=E_Ca_sn, E_Ca_dn=E_Ca_dn, \
    cNa_sn=my_cell.cNa_sn, cNa_se=my_cell.cNa_se, cNa_sg=my_cell.cNa_sg, cNa_dn=my_cell.cNa_dn, cNa_de=my_cell.cNa_de, cNa_dg=my_cell.cNa_dg, \
    cK_sn=my_cell.cK_sn, cK_se=my_cell.cK_se, cK_sg=my_cell.cK_sg, cK_dn=my_cell.cK_dn, cK_de=my_cell.cK_de, cK_dg=my_cell.cK_dg, \
    cCl_sn=my_cell.cCl_sn, cCl_se=my_cell.cCl_se, cCl_sg=my_cell.cCl_sg, cCl_dn=my_cell.cCl_dn, cCl_de=my_cell.cCl_de, cCl_dg=my_cell.cCl_dg, \
    cCa_sn=my_cell.cCa_sn, cCa_se=my_cell.cCa_se, cCa_dn=my_cell.cCa_dn, cCa_de=my_cell.cCa_de, \
    free_cCa_dn=my_cell.free_cCa_dn, \
    V_sn = my_cell.V_sn, V_se = my_cell.V_se, V_sg = my_cell.V_sg, \
    V_dn = my_cell.V_dn, V_de = my_cell.V_de, V_dg = my_cell.V_dg)

plt.show()
