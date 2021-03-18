from numpy import diff
from functions.synapse import I_synapse

def split_phi_e(my_cell, t,  spikes, dendritic_stimuli=False):
    """
    Split the extracellular potential of the edNEG model into a neuronal, glial, and diffusive component.

    Arguments: 
        my_cell (edNEG model object): tissue model
        t (array): time
        spikes (array): synaptic spike train
        dendritic_stimulie (boolean): True if the neuron was stimulated in the dendrite

    Returns: 
        phi_e_n (array): neuronal component of the extracellular potential
        phi_e_g (array): glial component of the extracellular potential
        phi_e_diff (array): diffusive component of the extracellular potential
    """


    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()

    # calculate capacitive currents
    dt = diff(t)
    I_cap_dn = my_cell.C_mdn*my_cell.A_m * diff(phi_mdn)/dt
    I_cap_dg = my_cell.C_mdg*my_cell.A_m * diff(phi_mdg)/dt

    # calculate membrane currents through ion channels (neuron)
    j_K_dn = my_cell.g_K_leak_n*(phi_mdn - E_K_dn) / (my_cell.F*my_cell.Z_K) \
            - 2*my_cell.j_pump_n(my_cell.cNa_dn, my_cell.cK_de) \
            + my_cell.j_kcc2(my_cell.cK_dn, my_cell.cK_de, my_cell.cCl_dn, my_cell.cCl_de) \
            + my_cell.j_nkcc1(my_cell.cNa_dn, my_cell.cNa_de, my_cell.cK_dn, my_cell.cK_de, my_cell.cCl_dn, my_cell.cCl_de) \
            + my_cell.g_AHP * my_cell.q * (phi_mdn - E_K_dn) / (my_cell.F*my_cell.Z_K)
            
    for i in range(len(t)):
        j_K_dn[i] += my_cell.g_C * my_cell.c[i] * min((my_cell.free_cCa_dn[i]-99.8e-6)/2.5e-4, 1) * (phi_mdn[i] - E_K_dn[i]) / (my_cell.F*my_cell.Z_K)

    I_dn = my_cell.A_m*my_cell.F*(my_cell.j_Na_dn(phi_mdn, E_Na_dn)[:-1]*my_cell.Z_Na + \
                                  j_K_dn[:-1]*my_cell.Z_K + \
                                  my_cell.j_Cl_dn(phi_mdn, E_Cl_dn)[:-1]*my_cell.Z_Cl + \
                                  my_cell.j_Ca_dn(phi_mdn, E_Ca_dn)[:-1]*my_cell.Z_Ca) + \
                                  I_cap_dn
    
    # calculate synaptic current 
    if dendritic_stimuli == True:
        for i in range(len(t)-1):
            I_dn[i] += I_synapse(my_cell, t[i], spikes, phi_mdn[i], E_Na_dn[i], E_K_dn[i], E_Ca_dn[i])

    # calculate membrane currents through ion channels (glia)
    I_dg = my_cell.A_m*my_cell.F*(my_cell.j_Na_dg(phi_mdg, E_Na_dg)[:-1]*my_cell.Z_Na + \
           my_cell.j_K_dg(phi_mdg, E_K_dg)[:-1]*my_cell.Z_K + \
           my_cell.j_Cl_dg(phi_mdg, E_Cl_dg)[:-1]*my_cell.Z_Cl) + \
           I_cap_dg
    
    # calculate conductivities   
    sigma_e = my_cell.conductivity_k(my_cell.D_Na, my_cell.Z_Na, my_cell.lamda_e, my_cell.cNa_se, my_cell.cNa_de) \
        + my_cell.conductivity_k(my_cell.D_K, my_cell.Z_K, my_cell.lamda_e, my_cell.cK_se, my_cell.cK_de) \
        + my_cell.conductivity_k(my_cell.D_Cl, my_cell.Z_Cl, my_cell.lamda_e, my_cell.cCl_se, my_cell.cCl_de) \
        + my_cell.conductivity_k(my_cell.D_Ca, my_cell.Z_Ca, my_cell.lamda_e, my_cell.cCa_se, my_cell.cCa_de)

    I_e_diff = my_cell.A_e*my_cell.F * (my_cell.Z_Na*my_cell.j_k_diff(my_cell.D_Na, my_cell.lamda_e, my_cell.cNa_se, my_cell.cNa_de) \
        + my_cell.Z_K*my_cell.j_k_diff(my_cell.D_K, my_cell.lamda_e, my_cell.cK_se, my_cell.cK_de) \
        + my_cell.Z_Cl*my_cell.j_k_diff(my_cell.D_Cl, my_cell.lamda_e, my_cell.cCl_se, my_cell.cCl_de) \
        + my_cell.Z_Ca*my_cell.j_k_diff(my_cell.D_Ca, my_cell.lamda_e, my_cell.cCa_se, my_cell.cCa_de))
    
    # calculate extracellar potential components   
    phi_e_n = -I_dn*my_cell.dx/(sigma_e[:-1]*my_cell.A_e)
    phi_e_g = -I_dg*my_cell.dx/(sigma_e[:-1]*my_cell.A_e)
    phi_e_diff = -I_e_diff*my_cell.dx/(sigma_e*my_cell.A_e)
    
    return phi_e_n, phi_e_g, phi_e_diff
