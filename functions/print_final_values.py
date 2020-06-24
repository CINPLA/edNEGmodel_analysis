import numpy as np

def print_final_values(my_cell):
    
    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    q_sn = my_cell.total_charge(np.array([my_cell.Na_sn[-1], my_cell.K_sn[-1], my_cell.Cl_sn[-1], my_cell.Ca_sn[-1], my_cell.X_sn]))
    q_se = my_cell.total_charge(np.array([my_cell.Na_se[-1], my_cell.K_se[-1], my_cell.Cl_se[-1], my_cell.Ca_se[-1], my_cell.X_se]))        
    q_sg = my_cell.total_charge(np.array([my_cell.Na_sg[-1], my_cell.K_sg[-1], my_cell.Cl_sg[-1], 0, my_cell.X_sg]))        
    q_dn = my_cell.total_charge(np.array([my_cell.Na_dn[-1], my_cell.K_dn[-1], my_cell.Cl_dn[-1], my_cell.Ca_dn[-1], my_cell.X_dn]))
    q_de = my_cell.total_charge(np.array([my_cell.Na_de[-1], my_cell.K_de[-1], my_cell.Cl_de[-1], my_cell.Ca_de[-1], my_cell.X_de]))
    q_dg = my_cell.total_charge(np.array([my_cell.Na_dg[-1], my_cell.K_dg[-1], my_cell.Cl_dg[-1], 0, my_cell.X_dg]))
    print("----------------------------")
    print("Final values")
    print("----------------------------")
    print("Final total charge(C):", q_sn + q_se + q_sg + q_dn + q_de + q_dg)
    print("Q_sn + Q_sg (C):", q_sn+q_sg)
    print("Q_se (C):", q_se)
    print("Q_dn + Q_sg (C):", q_dn+q_dg)
    print("Q_de (C):", q_de)
    print("----------------------------")
    print('final total volume (m^3):', my_cell.V_sn[-1] + my_cell.V_se[-1] + my_cell.V_sg[-1] + my_cell.V_dn[-1] + my_cell.V_de[-1] + my_cell.V_dg[-1])
    print("----------------------------")
