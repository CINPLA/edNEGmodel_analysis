import matplotlib.pyplot as plt

def set_style(style='default', w=1, h=1):
   sdict = {
       'default': {
           'figure.figsize' : (4.98 * w, 2 * h),
           'lines.linewidth': 1,
           'lines.markersize': 1.5,
           'font.size'      : 11,
           'legend.frameon' : False,
           'font.family'    : 'serif',
           'text.usetex'    : True,
           'xtick.direction': 'in',
           'ytick.direction': 'in'
       },
       'figure6': {
           'figure.figsize' : (4.98 * w, 2 * h),
           'lines.linewidth': 1,
           'lines.markersize': 1.5,
           'font.size'      : 14,
           'legend.frameon' : False,
           'font.family'    : 'serif',
           'text.usetex'    : True,
           'xtick.direction': 'in',
           'ytick.direction': 'in'
       }}
   rc = sdict[style]
   plt.rcParams.update(rc)
