import numpy as np
from edNEGmodel.edNEGmodel import *
from scipy.ndimage import uniform_filter1d
from scipy.interpolate import interp1d

def membrane_potentials(filename):
    """ Read membrane potentials from file. """
    
    data = np.load(filename)

    phi_sn = data['phi_sn']
    phi_se = data['phi_se']
    phi_sg = data['phi_sg']
    phi_dn = data['phi_dn']
    phi_de = data['phi_de']
    phi_dg = data['phi_dg']
    phi_msn = data['phi_msn']
    phi_mdn = data['phi_mdn']
    phi_msg = data['phi_msg']
    phi_mdg = data['phi_mdg']

    return phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg

def reversal_potentials(filename):
    """ Read reversal potentials from file. """

    data = np.load(filename)

    E_Na_sn = data['E_Na_sn']
    E_Na_sg = data['E_Na_sg']
    E_Na_dn = data['E_Na_dn']
    E_Na_dg = data['E_Na_dg']
    E_K_sn = data['E_K_sn']
    E_K_sg = data['E_K_sg']
    E_K_dn = data['E_K_dn']
    E_K_dg = data['E_K_dg']
    E_Cl_sn = data['E_Cl_sn']
    E_Cl_sg = data['E_Cl_sg']
    E_Cl_dn = data['E_Cl_dn']
    E_Cl_dg = data['E_Cl_dg']
    E_Ca_sn = data['E_Ca_sn']
    E_Ca_dn = data['E_Ca_dn']

    return E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn

def ion_concentrations(filename):
    """ Read ion concentrations from file. """

    data = np.load(filename)

    cNa_sn = data['cNa_sn']
    cNa_se = data['cNa_se']
    cNa_sg = data['cNa_sg']
    cNa_dn = data['cNa_dn']
    cNa_de = data['cNa_de']
    cNa_dg = data['cNa_dg']
    cK_sn = data['cK_sn']
    cK_se = data['cK_se']
    cK_sg = data['cK_sg']
    cK_dn = data['cK_dn']
    cK_de = data['cK_de']
    cK_dg = data['cK_dg']
    cCl_sn = data['cCl_sn']
    cCl_se = data['cCl_se']
    cCl_sg = data['cCl_sg']
    cCl_dn = data['cCl_dn']
    cCl_de = data['cCl_de']
    cCl_dg = data['cCl_dg']
    cCa_sn = data['cCa_sn']
    cCa_se = data['cCa_se']
    cCa_dn = data['cCa_dn']
    cCa_de = data['cCa_de']

    return cNa_sn, cNa_se, cNa_sg, cNa_dn, cNa_de, cNa_dg, cK_sn, cK_se, cK_sg, cK_dn, cK_de, cK_dg, cCl_sn, cCl_se, cCl_sg, cCl_dn, cCl_de, cCl_dg, cCa_sn, cCa_se, cCa_dn, cCa_de  

def state_variables(filename):
    """ Read state variables from file. """

    data = np.load(filename)

    n = data['n']
    h = data['h']
    s = data['s']
    c = data['c']
    q = data['q']
    z = data['z']

    return n, h, s, c, q, z

def dummy_cell():
    """ Create "dummy" cell to fetch functions and paramters. """
    
    T = 309.14
    alpha = 2

    cbK_se = 3.082
    cbK_sg = 99.959
    cbK_de = 3.082
    cbK_dg = 99.959
    cbCa_sn = 0.01
    cbCa_dn = 0.01

    cell = edNEGmodel(T, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, alpha, \
        cbK_se, cbK_sg, cbK_de, cbK_dg, cbCa_sn, cbCa_dn, 1, 1, 1, 1, 1, 1, \
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    return cell

def membrane_currents_sn(filename, t, stim_i, stim_start, stim_end):
    
    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = membrane_potentials(filename)
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = reversal_potentials(filename)
    cNa_sn, cNa_se, cNa_sg, cNa_dn, cNa_de, cNa_dg, cK_sn, cK_se, cK_sg, cK_dn, cK_de, cK_dg, cCl_sn, cCl_se, cCl_sg, cCl_dn, cCl_de, cCl_dg, cCa_sn, cCa_se, cCa_dn, cCa_de = ion_concentrations(filename)
    n, h, s, c, q, z = state_variables(filename)
    my_cell = dummy_cell()
    
    # capacitive current
    dt = np.diff(t)
    I_cap = my_cell.C_msn*my_cell.A_m * np.diff(phi_msn)/dt

    # membrane currents through ion channels
    I_leak = my_cell.A_m * (my_cell.g_K_leak_n*(phi_msn - E_K_sn) + my_cell.g_Na_leak_n*(phi_msn - E_Na_sn) + my_cell.g_Cl_leak_n*(phi_msn - E_Cl_sn))
    I_pump = my_cell.A_m * my_cell.F * my_cell.j_pump_n(cNa_sn, cK_se)
    I_Na = my_cell.A_m * my_cell.g_Na * my_cell.m_inf(phi_msn)**2 * h * (phi_msn - E_Na_sn) 
    I_DR = my_cell.A_m * my_cell.g_DR * n * (phi_msn - E_K_sn)

    # stimulus current
    I_stim = np.zeros(len(t))
    for i in range(len(t)):
        if t[i] > stim_start and t[i] < stim_end:
            I_stim[i] = -stim_i
    
    # interpolate 
    f_I_cap = interp1d(t[:-1], I_cap, 'cubic')
    f_I_leak = interp1d(t, I_leak, 'cubic')
    f_I_pump = interp1d(t, I_pump, 'cubic')
    f_I_Na = interp1d(t, I_Na, 'cubic')
    f_I_DR = interp1d(t, I_DR, 'cubic')
    f_I_stim = interp1d(t, I_stim, 'cubic')

    tt = np.linspace(int(t[0]), int(t[-1]), len(t))
    I_cap = f_I_cap(tt[:-1])
    I_leak = f_I_leak(tt)
    I_pump = f_I_pump(tt)
    I_Na = f_I_Na(tt)
    I_DR = f_I_DR(tt)
    I_stim = f_I_stim(tt)

    # calculate moving averages
    dt = np.diff(tt)[0]
    size = int(10/dt)
    av_I_cap = uniform_filter1d(I_cap, size)
    av_I_leak = uniform_filter1d(I_leak, size)
    av_I_pump = uniform_filter1d(I_pump, size)
    av_I_Na = uniform_filter1d(I_Na, size)
    av_I_DR = uniform_filter1d(I_DR, size)
    av_I_stim = uniform_filter1d(I_stim, size)
    
    return tt, av_I_cap, av_I_leak, av_I_pump, av_I_Na, av_I_DR, av_I_stim

def membrane_currents_dn(filename, t):

    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = membrane_potentials(filename)
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = reversal_potentials(filename)
    cNa_sn, cNa_se, cNa_sg, cNa_dn, cNa_de, cNa_dg, cK_sn, cK_se, cK_sg, cK_dn, cK_de, cK_dg, cCl_sn, cCl_se, cCl_sg, cCl_dn, cCl_de, cCl_dg, cCa_sn, cCa_se, cCa_dn, cCa_de = ion_concentrations(filename)
    n, h, s, c, q, z = state_variables(filename)
    my_cell = dummy_cell()
    
    # capacitive current
    dt = np.diff(t)
    I_cap = my_cell.C_mdn*my_cell.A_m * np.diff(phi_mdn)/dt

    # membrane currents through ion channels
    I_leak = my_cell.A_m * (my_cell.g_K_leak_n*(phi_mdn - E_K_dn) + my_cell.g_Na_leak_n*(phi_mdn - E_Na_dn) + my_cell.g_Cl_leak_n*(phi_mdn - E_Cl_dn))
    I_pump = my_cell.A_m * my_cell.F * my_cell.j_pump_n(cNa_dn, cK_de)
    I_AHP = my_cell.A_m * my_cell.g_AHP * q * (phi_mdn - E_K_dn)
    I_Ca = my_cell.A_m * my_cell.g_Ca * s**2 * z * (phi_mdn - E_Ca_dn)
    I_KC = np.zeros(len(t))
    for i in range(len(t)):
        I_KC[i] += my_cell.A_m * my_cell.g_C * c[i] * min((0.01*cCa_dn[i]-99.8e-6)/2.5e-4, 1) * (phi_mdn[i] - E_K_dn[i]) 

    # interpolate
    f_I_cap = interp1d(t[:-1], I_cap, 'cubic')
    f_I_leak = interp1d(t, I_leak, 'cubic')
    f_I_pump = interp1d(t, I_pump, 'cubic')
    f_I_AHP = interp1d(t, I_AHP, 'cubic')
    f_I_Ca = interp1d(t, I_Ca, 'cubic')
    f_I_KC = interp1d(t, I_KC, 'cubic')
    
    tt = np.linspace(int(t[0]), int(t[-1]), len(t))
    I_cap = f_I_cap(tt[:-1])
    I_leak = f_I_leak(tt)
    I_pump = f_I_pump(tt)
    I_AHP = f_I_AHP(tt)
    I_Ca = f_I_Ca(tt)
    I_KC = f_I_KC(tt)

    # calculate moving averages
    dt = np.diff(tt)[0]
    size = int(10/dt)
    av_I_cap = uniform_filter1d(I_cap, size)
    av_I_leak = uniform_filter1d(I_leak, size)
    av_I_pump = uniform_filter1d(I_pump, size)
    av_I_AHP = uniform_filter1d(I_AHP, size)
    av_I_Ca = uniform_filter1d(I_Ca, size)
    av_I_KC = uniform_filter1d(I_KC, size)

    return tt, av_I_cap, av_I_leak, av_I_pump, av_I_AHP, av_I_Ca, av_I_KC

def membrane_currents_sg(filename, t):
    
    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = membrane_potentials(filename)
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = reversal_potentials(filename)
    cNa_sn, cNa_se, cNa_sg, cNa_dn, cNa_de, cNa_dg, cK_sn, cK_se, cK_sg, cK_dn, cK_de, cK_dg, cCl_sn, cCl_se, cCl_sg, cCl_dn, cCl_de, cCl_dg, cCa_sn, cCa_se, cCa_dn, cCa_de = ion_concentrations(filename)
    n, h, s, c, q, z = state_variables(filename)
    my_cell = dummy_cell()
    
    # capacitive current
    dt = np.diff(t)
    I_cap = my_cell.C_msg*my_cell.A_m * np.diff(phi_msg)/dt
    
    # membrane currents through ion channels
    I_leak = my_cell.A_m * (my_cell.g_Na_leak_g*(phi_msg - E_Na_sg) + my_cell.g_Cl_leak_g*(phi_msg - E_Cl_sg))
    I_pump = my_cell.A_m * my_cell.F *my_cell.j_pump_g(cNa_sg, cK_se)
    dphi = (phi_msg - E_K_sg)*1000
    phi_m_mil = phi_msg*1000
    bE_K_mil = my_cell.bE_K_sg*1000
    fact1 = (1 + np.exp(18.4/42.4))/(1 + np.exp((dphi + 18.5)/42.5))
    fact2 = (1 + np.exp(-(118.6+bE_K_mil)/44.1))/(1+np.exp(-(118.6+phi_m_mil)/44.1))
    f = np.sqrt(cK_se/my_cell.cbK_se) * fact1 * fact2 
    I_Kir = my_cell.A_m * my_cell.g_K_IR * f * (phi_msg - E_K_sg)

    # interpolate
    f_I_cap = interp1d(t[:-1], I_cap, 'cubic')
    f_I_leak = interp1d(t, I_leak, 'cubic')
    f_I_pump = interp1d(t, I_pump, 'cubic')
    f_I_Kir = interp1d(t, I_Kir, 'cubic')

    tt = np.linspace(int(t[0]), int(t[-1]), len(t))
    I_cap = f_I_cap(tt[:-1])
    I_leak = f_I_leak(tt)
    I_pump = f_I_pump(tt)
    I_Kir = f_I_Kir(tt)
    
    # calculate moving averages
    dt = np.diff(tt)[0]
    size = int(10/dt)
    av_I_cap = uniform_filter1d(I_cap, size)
    av_I_leak = uniform_filter1d(I_leak, size)
    av_I_pump = uniform_filter1d(I_pump, size)
    av_I_Kir = uniform_filter1d(I_Kir, size)
    
    return tt, av_I_cap, av_I_leak, av_I_pump, av_I_Kir

def membrane_currents_dg(filename, t):
    
    phi_sn, phi_se, phi_sg, phi_dn, phi_de, phi_dg, phi_msn, phi_mdn, phi_msg, phi_mdg = membrane_potentials(filename)
    E_Na_sn, E_Na_sg, E_Na_dn, E_Na_dg, E_K_sn, E_K_sg, E_K_dn, E_K_dg, E_Cl_sn, E_Cl_sg, E_Cl_dn, E_Cl_dg, E_Ca_sn, E_Ca_dn = reversal_potentials(filename)
    cNa_sn, cNa_se, cNa_sg, cNa_dn, cNa_de, cNa_dg, cK_sn, cK_se, cK_sg, cK_dn, cK_de, cK_dg, cCl_sn, cCl_se, cCl_sg, cCl_dn, cCl_de, cCl_dg, cCa_sn, cCa_se, cCa_dn, cCa_de = ion_concentrations(filename)
    n, h, s, c, q, z = state_variables(filename)
    my_cell = dummy_cell()
    
    # capacitive current
    dt = np.diff(t)
    I_cap = my_cell.C_mdg*my_cell.A_m * np.diff(phi_mdg)/dt
    
    # membrane currents through ion channels
    I_leak = my_cell.A_m * (my_cell.g_Na_leak_g*(phi_mdg - E_Na_dg) + my_cell.g_Cl_leak_g*(phi_mdg - E_Cl_dg))
    I_pump = my_cell.A_m * my_cell.F *my_cell.j_pump_g(cNa_dg, cK_de)
    dphi = (phi_mdg - E_K_dg)*1000
    phi_m_mil = phi_mdg*1000
    bE_K_mil = my_cell.bE_K_dg*1000
    fact1 = (1 + np.exp(18.4/42.4))/(1 + np.exp((dphi + 18.5)/42.5))
    fact2 = (1 + np.exp(-(118.6+bE_K_mil)/44.1))/(1+np.exp(-(118.6+phi_m_mil)/44.1))
    f = np.sqrt(cK_de/my_cell.cbK_de) * fact1 * fact2 
    I_Kir = my_cell.A_m * my_cell.g_K_IR * f * (phi_mdg - E_K_dg)
    
    # interpolate
    f_I_cap = interp1d(t[:-1], I_cap, 'cubic')
    f_I_leak = interp1d(t, I_leak, 'cubic')
    f_I_pump = interp1d(t, I_pump, 'cubic')
    f_I_Kir = interp1d(t, I_Kir, 'cubic')

    tt = np.linspace(int(t[0]), int(t[-1]), len(t))
    I_cap = f_I_cap(tt[:-1])
    I_leak = f_I_leak(tt)
    I_pump = f_I_pump(tt)
    I_Kir = f_I_Kir(tt)
    
    # calculate moving averages
    dt = np.diff(tt)[0]
    size = int(10/dt)
    av_I_cap = uniform_filter1d(I_cap, size)
    av_I_leak = uniform_filter1d(I_leak, size)
    av_I_pump = uniform_filter1d(I_pump, size)
    av_I_Kir = uniform_filter1d(I_Kir, size)

    return tt, av_I_cap, av_I_leak, av_I_pump, av_I_Kir
