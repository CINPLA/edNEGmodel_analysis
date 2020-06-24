import numpy as np

def print_initial_values(init_cell):
    
    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = init_cell.membrane_potentials()
    
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = init_cell.reversal_potentials()

    q_sn = init_cell.total_charge(np.array([init_cell.Na_sn, init_cell.K_sn, init_cell.Cl_sn, init_cell.Ca_sn, init_cell.X_sn]))
    q_se = init_cell.total_charge(np.array([init_cell.Na_se, init_cell.K_se, init_cell.Cl_se, init_cell.Ca_se, init_cell.X_se]))        
    q_sg = init_cell.total_charge(np.array([init_cell.Na_sg, init_cell.K_sg, init_cell.Cl_sg, 0, init_cell.X_sg]))        
    q_dn = init_cell.total_charge(np.array([init_cell.Na_dn, init_cell.K_dn, init_cell.Cl_dn, init_cell.Ca_dn, init_cell.X_dn]))
    q_de = init_cell.total_charge(np.array([init_cell.Na_de, init_cell.K_de, init_cell.Cl_de, init_cell.Ca_de, init_cell.X_de]))
    q_dg = init_cell.total_charge(np.array([init_cell.Na_dg, init_cell.K_dg, init_cell.Cl_dg, 0, init_cell.X_dg]))
    print("----------------------------")
    print("Initial values")
    print("----------------------------")
    print("initial total charge(C):", q_sn + q_se + q_sg + q_dn + q_de + q_dg)
    print("Q_sn + Q_sg (C):", q_sn+q_sg)
    print("Q_se (C):", q_se)
    print("Q_dn + Q_sg (C):", q_dn+q_dg)
    print("Q_de (C):", q_de)
    print("----------------------------")
    print('phi_sn: ', round(phi_sn*1000, 1))
    print('phi_se: ', round(phi_se*1000, 1))
    print('phi_sg: ', round(phi_sg*1000, 1))
    print('phi_dn: ', round(phi_dn*1000, 1))
    print('phi_de: ', round(phi_de*1000, 1))
    print('phi_dg: ', round(phi_dg*1000, 1))
    print('phi_msn: ', round(phi_msn*1000, 1))
    print('phi_mdn: ', round(phi_mdn*1000, 1))
    print('phi_msg: ', round(phi_msg*1000, 1))
    print('phi_mdg: ', round(phi_mdg*1000, 1))
    print('E_Na_sn: ', round(E_Na_sn*1000))
    print('E_Na_sg: ', round(E_Na_sg*1000))
    print('E_K_sn: ', round(E_K_sn*1000))
    print('E_K_sg: ', round(E_K_sg*1000))
    print('E_Cl_sn: ', round(E_Cl_sn*1000))
    print('E_Cl_sg: ', round(E_Cl_sg*1000))
    print('E_Ca_sn: ', round(E_Ca_sn*1000))
    print("----------------------------")
    print('psi_se-psi_sn', init_cell.psi_se-init_cell.psi_sn) 
    print('psi_se-psi_sg', init_cell.psi_se-init_cell.psi_sg) 
    print('psi_de-psi_dn', init_cell.psi_de-init_cell.psi_dn) 
    print('psi_de-psi_dg', init_cell.psi_de-init_cell.psi_dg) 
    print("----------------------------")
    print('initial total volume (m^3):', init_cell.V_sn + init_cell.V_se + init_cell.V_sg + init_cell.V_dn + init_cell.V_de + init_cell.V_dg)
    print("----------------------------")
