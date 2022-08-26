## Figure settings file
## CID: 01831640

import os 
os.environ["PATH"] += os.pathsep + '/Library/TeX/texbin'
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
rc('font',**{'family':'serif','serif':['Computer Modern']})
rc('text', usetex=True)
plt.rc('axes', labelsize=20)   # fontsize of the x and y labels
plt.rc('axes', titlesize=20)
plt.rc('xtick', labelsize=15)    # fontsize of the tick labels
plt.rc('ytick', labelsize=15)
plt.rc('legend', fontsize=15)    # legend fontsize
plt.rc('figure', titlesize=20)   # fontsize of the figure title
plt.rc('lines', markersize=5)
plt.rc('lines', linewidth=1.5)
plt.rc('lines',markeredgewidth=1.0)