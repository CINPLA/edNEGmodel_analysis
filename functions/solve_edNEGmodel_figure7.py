from edNEGmodel.edNEGmodel import *
from functions.print_initial_values import *
from scipy.integrate import solve_ivp
import numpy as np
import pkg_resources
import quantities as qnt
from elephant.spike_train_generation import homogeneous_poisson_process
from functions.synapse import *

def solve_edNEGmodel(t_dur, alpha, syn_rate, syn_start, syn_end, syn_protocol):
    """
    Solves the edNEG model (Sætra et al. 2021) using the solve_ivp function from scipy.

    Arguments:
        t_dur (float): duration of simulation [s]
        alpha (float): coupling strength
        I_stim (float): stimulus current [A]
        stim_start (float): time of stimulus onset [s]
        stim_end (float): time of stimulus offset [s]
        syn_protocol (str): protocol defining synaptic location 
    
    Returns:
        sol: solution from solve_ivp
        my_cell: edNEGmodel object
        spikes: synaptic spike train
    """

    spikes = homogeneous_poisson_process(rate=syn_rate*qnt.Hz, t_start=syn_start*qnt.s, t_stop=syn_end*qnt.s, as_array=True)
    filename = pkg_resources.resource_filename('data', 'initial_values/initial_values.npz')
    data = np.load(filename)

    T = 309.14

    # initial membrane potentials [V]
    phi_msn = data['phi_msn']
    phi_msg = data['phi_msg']
    phi_mdn = data['phi_mdn']
    phi_mdg = data['phi_mdg']

    # initial volumes [m**3]
    V_sn0 = data['V_sn']
    V_se0 = data['V_se']
    V_sg0 = data['V_sg']
    V_dn0 = data['V_dn']
    V_de0 = data['V_de']
    V_dg0 = data['V_dg']

    # initial amounts of ions [mol]
    Na_sn0 = data['Na_sn']
    Na_se0 = data['Na_se']
    Na_sg0 = data['Na_sg']
    K_sn0 = data['K_sn']
    K_se0 = data['K_se']
    K_sg0 = data['K_sg']
    Cl_sn0 = data['Cl_sn']
    Cl_se0 = data['Cl_se']
    Cl_sg0 = data['Cl_sg']
    Ca_sn0 = data['Ca_sn']
    Ca_se0 = data['Ca_se']

    Na_dn0 = data['Na_dn']
    Na_de0 = data['Na_de']
    Na_dg0 = data['Na_dg']
    K_dn0 = data['K_dn'] 
    K_de0 = data['K_de']
    K_dg0 = data['K_dg']
    Cl_dn0 = data['Cl_dn']
    Cl_de0 = data['Cl_de']
    Cl_dg0 = data['Cl_dg']
    Ca_dn0 = data['Ca_dn']
    Ca_de0 = data['Ca_de']

    # intial gating variables
    n0 = data['n']
    h0 = data['h']
    s0 = data['s']
    c0 = data['c']
    q0 = data['q']
    z0 = data['z']

    # baseline ion concentrations [mol/m**3]
    cbK_se = 3.082
    cbK_sg = 99.959
    cbK_de = 3.082
    cbK_dg = 99.959
    cbCa_sn = 0.01
    cbCa_dn = 0.01

    # residual charges [mol]
    res_sn = phi_msn*3e-2*616e-12/9.648e4 
    res_sg = phi_msg*3e-2*616e-12/9.648e4 
    res_se = res_sn+res_sg
    res_dn = phi_mdn*3e-2*616e-12/9.648e4 
    res_dg = phi_mdg*3e-2*616e-12/9.648e4 
    res_de = res_dn+res_dg

    X_sn = Na_sn0 + K_sn0 - Cl_sn0 + 2*Ca_sn0 - res_sn
    X_se = Na_se0 + K_se0 - Cl_se0 + 2*Ca_se0 + res_se
    X_sg = Na_sg0 + K_sg0 - Cl_sg0 - res_sg
    X_dn = Na_dn0 + K_dn0 - Cl_dn0 + 2*Ca_dn0 - res_dn
    X_de = Na_de0 + K_de0 - Cl_de0 + 2*Ca_de0 + res_de
    X_dg = Na_dg0 + K_dg0 - Cl_dg0 - res_dg

    # residual mass [mol/m**3]
    cM_sn = (Na_sn0 + K_sn0 + Cl_sn0 + Ca_sn0)/V_sn0
    cM_se = (Na_se0 + K_se0 + Cl_se0 + Ca_se0)/V_se0 
    cM_sg = (Na_sg0 + K_sg0 + Cl_sg0)/V_sg0
    cM_dn = (Na_dn0 + K_dn0 + Cl_dn0 + Ca_dn0)/V_dn0
    cM_de = (Na_de0 + K_de0 + Cl_de0 + Ca_de0)/V_de0 
    cM_dg = (Na_dg0 + K_dg0 + Cl_dg0)/V_dg0 

    # print initial values
    #init_cell = edNEGmodel(T, Na_sn0, Na_se0, Na_sg0, Na_dn0, Na_de0, Na_dg0, K_sn0, K_se0, K_sg0, K_dn0, K_de0, K_dg0, Cl_sn0, Cl_se0, Cl_sg0, Cl_dn0, Cl_de0, Cl_dg0, Ca_sn0, Ca_se0, Ca_dn0, Ca_de0, X_sn, X_se, X_sg, X_dn, X_de, X_dg, alpha, cbK_se, cbK_sg, cbK_de, cbK_dg, cbCa_sn, cbCa_dn, n0, h0, s0, c0, q0, z0, V_sn0, V_se0, V_sg0, V_dn0, V_de0, V_dg0, cM_sn, cM_se, cM_sg, cM_dn, cM_de, cM_dg)
    #print_initial_values(init_cell)

    # define differential equations for different synaptic protocols
    def dkdt_syn_soma(t,k):

        Na_sn, Na_se, Na_sg, Na_dn, Na_de, Na_dg, K_sn, K_se, K_sg, K_dn, K_de, K_dg, Cl_sn, Cl_se, Cl_sg, Cl_dn, Cl_de, Cl_dg, Ca_sn, Ca_se, Ca_dn, Ca_de, n, h, s, c, q, z, V_sn, V_se, V_sg, V_dn, V_de, V_dg = k

        my_cell = edNEGmodel(T, Na_sn, Na_se, Na_sg, Na_dn, Na_de, Na_dg, K_sn, K_se, K_sg, K_dn, K_de, K_dg, Cl_sn, Cl_se, Cl_sg, Cl_dn, Cl_de, Cl_dg, Ca_sn, Ca_se, Ca_dn, Ca_de, X_sn, X_se, X_sg, X_dn, X_de, X_dg, alpha, cbK_se, cbK_sg, cbK_de, cbK_dg, cbCa_sn, cbCa_dn, n, h, s, c, q, z, V_sn, V_se, V_sg, V_dn, V_de, V_dg, cM_sn, cM_se, cM_sg, cM_dn, cM_de, cM_dg)
        
        phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
        E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()
        dNadt_sn, dNadt_se, dNadt_sg, dNadt_dn, dNadt_de, dNadt_dg, dKdt_sn, dKdt_se, dKdt_sg, dKdt_dn, dKdt_de, dKdt_dg, dCldt_sn, dCldt_se, dCldt_sg, dCldt_dn, dCldt_de, dCldt_dg, dCadt_sn, dCadt_se, dCadt_dn, dCadt_de = my_cell.dkdt()
        dndt, dhdt, dsdt, dcdt, dqdt, dzdt = my_cell.dmdt()
        dVsidt, dVsedt, dVsgdt, dVdidt, dVdedt, dVdgdt = my_cell.dVdt()
       
        if t > syn_start:
            dNadt_sn, dNadt_se, dKdt_sn, dKdt_se, dCadt_sn, dCadt_se = activate_synapse(my_cell, t, spikes, phi_msn, E_Na_sn, E_K_sn, E_Ca_sn, dNadt_sn, dNadt_se, dKdt_sn, dKdt_se, dCadt_sn, dCadt_se)
        
        return dNadt_sn, dNadt_se, dNadt_sg, dNadt_dn, dNadt_de, dNadt_dg, dKdt_sn, dKdt_se, dKdt_sg, dKdt_dn, dKdt_de, dKdt_dg, \
            dCldt_sn, dCldt_se, dCldt_sg, dCldt_dn, dCldt_de, dCldt_dg, dCadt_sn, dCadt_se, dCadt_dn, dCadt_de, \
            dndt, dhdt, dsdt, dcdt, dqdt, dzdt, dVsidt, dVsedt, dVsgdt, dVdidt, dVdedt, dVdgdt

    def dkdt_syn_dendrite(t,k):

        Na_sn, Na_se, Na_sg, Na_dn, Na_de, Na_dg, K_sn, K_se, K_sg, K_dn, K_de, K_dg, Cl_sn, Cl_se, Cl_sg, Cl_dn, Cl_de, Cl_dg, Ca_sn, Ca_se, Ca_dn, Ca_de, n, h, s, c, q, z, V_sn, V_se, V_sg, V_dn, V_de, V_dg = k

        my_cell = edNEGmodel(T, Na_sn, Na_se, Na_sg, Na_dn, Na_de, Na_dg, K_sn, K_se, K_sg, K_dn, K_de, K_dg, Cl_sn, Cl_se, Cl_sg, Cl_dn, Cl_de, Cl_dg, Ca_sn, Ca_se, Ca_dn, Ca_de, X_sn, X_se, X_sg, X_dn, X_de, X_dg, alpha, cbK_se, cbK_sg, cbK_de, cbK_dg, cbCa_sn, cbCa_dn, n, h, s, c, q, z, V_sn, V_se, V_sg, V_dn, V_de, V_dg, cM_sn, cM_se, cM_sg, cM_dn, cM_de, cM_dg)
        
        phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
        E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()
        dNadt_sn, dNadt_se, dNadt_sg, dNadt_dn, dNadt_de, dNadt_dg, dKdt_sn, dKdt_se, dKdt_sg, dKdt_dn, dKdt_de, dKdt_dg, dCldt_sn, dCldt_se, dCldt_sg, dCldt_dn, dCldt_de, dCldt_dg, dCadt_sn, dCadt_se, dCadt_dn, dCadt_de = my_cell.dkdt()
        dndt, dhdt, dsdt, dcdt, dqdt, dzdt = my_cell.dmdt()
        dVsidt, dVsedt, dVsgdt, dVdidt, dVdedt, dVdgdt = my_cell.dVdt()
        
        if t > syn_start:
            dNadt_dn, dNadt_de, dKdt_dn, dKdt_de, dCadt_dn, dCadt_de = activate_synapse(my_cell, t, spikes, phi_mdn, E_Na_dn, E_K_dn, E_Ca_dn, dNadt_dn, dNadt_de, dKdt_dn, dKdt_de, dCadt_dn, dCadt_de)
        
        return dNadt_sn, dNadt_se, dNadt_sg, dNadt_dn, dNadt_de, dNadt_dg, dKdt_sn, dKdt_se, dKdt_sg, dKdt_dn, dKdt_de, dKdt_dg, \
            dCldt_sn, dCldt_se, dCldt_sg, dCldt_dn, dCldt_de, dCldt_dg, dCadt_sn, dCadt_se, dCadt_dn, dCadt_de, \
            dndt, dhdt, dsdt, dcdt, dqdt, dzdt, dVsidt, dVsedt, dVsgdt, dVdidt, dVdedt, dVdgdt
        
    def dkdt_syn_both(t,k):

        Na_sn, Na_se, Na_sg, Na_dn, Na_de, Na_dg, K_sn, K_se, K_sg, K_dn, K_de, K_dg, Cl_sn, Cl_se, Cl_sg, Cl_dn, Cl_de, Cl_dg, Ca_sn, Ca_se, Ca_dn, Ca_de, n, h, s, c, q, z, V_sn, V_se, V_sg, V_dn, V_de, V_dg = k

        my_cell = edNEGmodel(T, Na_sn, Na_se, Na_sg, Na_dn, Na_de, Na_dg, K_sn, K_se, K_sg, K_dn, K_de, K_dg, Cl_sn, Cl_se, Cl_sg, Cl_dn, Cl_de, Cl_dg, Ca_sn, Ca_se, Ca_dn, Ca_de, X_sn, X_se, X_sg, X_dn, X_de, X_dg, alpha, cbK_se, cbK_sg, cbK_de, cbK_dg, cbCa_sn, cbCa_dn, n, h, s, c, q, z, V_sn, V_se, V_sg, V_dn, V_de, V_dg, cM_sn, cM_se, cM_sg, cM_dn, cM_de, cM_dg)
        
        phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = my_cell.membrane_potentials()
        E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = my_cell.reversal_potentials()
        dNadt_sn, dNadt_se, dNadt_sg, dNadt_dn, dNadt_de, dNadt_dg, dKdt_sn, dKdt_se, dKdt_sg, dKdt_dn, dKdt_de, dKdt_dg, dCldt_sn, dCldt_se, dCldt_sg, dCldt_dn, dCldt_de, dCldt_dg, dCadt_sn, dCadt_se, dCadt_dn, dCadt_de = my_cell.dkdt()
        dndt, dhdt, dsdt, dcdt, dqdt, dzdt = my_cell.dmdt()
        dVsidt, dVsedt, dVsgdt, dVdidt, dVdedt, dVdgdt = my_cell.dVdt()
        
        if t > syn_start:
            dNadt_sn, dNadt_se, dKdt_sn, dKdt_se, dCadt_sn, dCadt_se = activate_synapse(my_cell, t, spikes, phi_msn, E_Na_sn, E_K_sn, E_Ca_sn, dNadt_sn, dNadt_se, dKdt_sn, dKdt_se, dCadt_sn, dCadt_se)
            dNadt_dn, dNadt_de, dKdt_dn, dKdt_de, dCadt_dn, dCadt_de = activate_synapse(my_cell, t, spikes, phi_mdn, E_Na_dn, E_K_dn, E_Ca_dn, dNadt_dn, dNadt_de, dKdt_dn, dKdt_de, dCadt_dn, dCadt_de)
        
        return dNadt_sn, dNadt_se, dNadt_sg, dNadt_dn, dNadt_de, dNadt_dg, dKdt_sn, dKdt_se, dKdt_sg, dKdt_dn, dKdt_de, dKdt_dg, \
            dCldt_sn, dCldt_se, dCldt_sg, dCldt_dn, dCldt_de, dCldt_dg, dCadt_sn, dCadt_se, dCadt_dn, dCadt_de, \
            dndt, dhdt, dsdt, dcdt, dqdt, dzdt, dVsidt, dVsedt, dVsgdt, dVdidt, dVdedt, dVdgdt
    
    # solve 
    t_span = (0, t_dur)

    k0 = [Na_sn0, Na_se0, Na_sg0, Na_dn0, Na_de0, Na_dg0, K_sn0, K_se0, K_sg0, K_dn0, K_de0, K_dg0, Cl_sn0, Cl_se0, Cl_sg0, Cl_dn0, Cl_de0, Cl_dg0, Ca_sn0, Ca_se0, Ca_dn0, Ca_de0, n0, h0, s0, c0, q0, z0, V_sn0, V_se0, V_sg0, V_dn0, V_de0, V_dg0]

    if syn_protocol == 'syn_soma':
        sol = solve_ivp(dkdt_syn_soma, t_span, k0, method='RK23', max_step=1e-4)
    elif syn_protocol == 'syn_dendrite':
        sol = solve_ivp(dkdt_syn_dendrite, t_span, k0, method='RK23', max_step=1e-4)
    elif syn_protocol == 'syn_both':
        sol = solve_ivp(dkdt_syn_both, t_span, k0, method='RK23', max_step=1e-4)

    Na_sn, Na_se, Na_sg, Na_dn, Na_de, Na_dg, K_sn, K_se, K_sg, K_dn, K_de, K_dg, Cl_sn, Cl_se, Cl_sg, Cl_dn, Cl_de, Cl_dg, Ca_sn, Ca_se, Ca_dn, Ca_de, n, h, s, c, q, z, V_sn, V_se, V_sg, V_dn, V_de, V_dg = sol.y

    my_cell = edNEGmodel(T, Na_sn, Na_se, Na_sg, Na_dn, Na_de, Na_dg, K_sn, K_se, K_sg, K_dn, K_de, K_dg, Cl_sn, Cl_se, Cl_sg, Cl_dn, Cl_de, Cl_dg, \
        Ca_sn, Ca_se, Ca_dn, Ca_de, X_sn, X_se, X_sg, X_dn, X_de, X_dg, alpha, \
        cbK_se, cbK_sg, cbK_de, cbK_dg, cbCa_sn, cbCa_dn, n, h, s, c, q, z, \
        V_sn, V_se, V_sg, V_dn, V_de, V_dg, cM_sn, cM_se, cM_sg, cM_dn, cM_de, cM_dg)

    return sol, my_cell, spikes
