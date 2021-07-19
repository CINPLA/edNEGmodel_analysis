import numpy as np

def g(t, t_s):
    """
    Calculate synaptic conductance.
    
    Arguments:
        t (float): time
        t_s (array): spike train

    Returns: 
        G (float): synaptic conductance
    """

    tau_1 = 3.0e-3       # [s]
    tau_2 = 1.0e-3       # [s]

    condition = t_s <= t
    t_s = np.extract(condition, t_s)

    G = np.exp(-(t-t_s)/tau_1) - np.exp(-(t-t_s)/tau_2)
    G = sum(G)

    return G
    
def activate_synapse(my_cell, t, t_s, phi, E_Na, E_K, E_Ca, dNadt_n, dNadt_e, dKdt_n, dKdt_e, dCadt_n, dCadt_e):
    """
    Add synaptic currents to the edNEG model.
    """

    g_bar = g(t, t_s)
    g_nmda_Na = 1.0e-9
    g_nmda_K = 1.9e-9
    g_nmda_Ca = 6.5e-12

    j_nmda_Na = g_nmda_Na * g_bar * (phi - E_Na) / (my_cell.F*my_cell.Z_Na)
    j_nmda_K = g_nmda_K * g_bar * (phi - E_K) / (my_cell.F*my_cell.Z_K)
    j_nmda_Ca = g_nmda_Ca * g_bar * (phi - E_Ca) / (my_cell.F*my_cell.Z_Ca)
    
    dNadt_n += -j_nmda_Na
    dNadt_e += j_nmda_Na
    dKdt_n += -j_nmda_K
    dKdt_e += j_nmda_K
    dCadt_n += -j_nmda_Ca
    dCadt_e += j_nmda_Ca

    return dNadt_n, dNadt_e, dKdt_n, dKdt_e, dCadt_n, dCadt_e

def I_synapse(my_cell, t, t_s, phi, E_Na, E_K, E_Ca):
    """
    Calculate the total synaptic current across the membrane.
    """

    g_bar = g(t, t_s)
    g_nmda_Na = 1.0e-9
    g_nmda_K = 1.9e-9
    g_nmda_Ca = 6.5e-12

    j_nmda_Na = g_nmda_Na * g_bar * (phi - E_Na) / (my_cell.F*my_cell.Z_Na)
    j_nmda_K = g_nmda_K * g_bar * (phi- E_K) / (my_cell.F*my_cell.Z_K)
    j_nmda_Ca = g_nmda_Ca * g_bar * (phi- E_Ca) / (my_cell.F*my_cell.Z_Ca)

    I = (j_nmda_Na*my_cell.Z_Na + j_nmda_K*my_cell.Z_K + j_nmda_Ca*my_cell.Z_Ca)*my_cell.F
    return I

