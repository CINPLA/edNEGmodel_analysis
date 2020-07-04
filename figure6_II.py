import numpy as np

data = np.load('data/figure6_with_glia_1.npz')
ff_with_glia = [0]
Ke_with_glia = [data['cK_se'][0]]
Vn_with_glia = [0]

data = np.load('data/figure6_no_glia_1.npz')
ff_without_glia = [0]
Ke_without_glia = [data['cK_se'][0]]
Vn_without_glia = [0]

for  i in range(1,20):
    data = np.load('data/figure6_with_glia_' + str(i) + '.npz')
    t = data['t']
    ff = data['stimulus_frequency']
    phi_msn = data['phi_msn']*1000
    ff_with_glia.append(ff)
    cK_se = data['cK_se']
    Ke_with_glia.append(max(cK_se))
    V_sn = data['V_sn']
    V_dn = data['V_dn']
    V_n = V_sn + V_dn
    dV_n = 100*(V_n-V_n[0])/V_n[0]
    Vn_with_glia.append(dV_n[-1])
   
    data = np.load('data/figure6_no_glia_' + str(i) + '.npz')
    t = data['t']
    ff = data['stimulus_frequency']
    phi_msn = data['phi_msn']*1000
    ff_without_glia.append(ff)
    cK_se = data['cK_se']
    Ke_without_glia.append(max(cK_se))
    V_sn = data['V_sn']
    V_dn = data['V_dn']
    V_n = V_sn + V_dn
    dV_n = 100*(V_n-V_n[0])/V_n[0]
    Vn_without_glia.append(dV_n[-1])

np.savez('data/figure6.npz', \
ff_with_glia = ff_with_glia, \
Ke_with_glia = Ke_with_glia, \
Vn_with_glia = Vn_with_glia, \
ff_without_glia = ff_without_glia, \
Ke_without_glia = Ke_without_glia, \
Vn_without_glia=Vn_without_glia)
