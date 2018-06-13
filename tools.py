import sys
import getopt
import matplotlib.pyplot as plt
import matplotlib.colors as mco
from mpl_toolkits.axes_grid1 import make_axes_locatable
gnorm = mco.LogNorm()
def makead(nw,nh,ns,numplots):
    fig = plt.figure(figsize=(nw*ns,nh*ns))
    axs = range(numplots)
    divs = range(numplots)
    for i in range(numplots):
        axs[i] = fig.add_subplot(nh,nw,i+1)
        divs[i] = make_axes_locatable(axs[i]).append_axes('right',size='5%',pad=0.0)
    return fig,axs,divs

def plotframe(x,y,data,axs,divs,ni,vmin0,vmax0,cbbool):
    axs[ni].cla()
    im = axs[ni].pcolormesh(y,x,data,cmap=plt.get_cmap('viridis'),vmin=vmin0,vmax=vmax0,norm=gnorm,zorder=0)
    if cbbool:
        plt.colorbar(im,cax=divs[ni])
        plt.tight_layout()

def init():
    return

