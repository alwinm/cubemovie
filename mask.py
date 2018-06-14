#First use python -m script_ppp to parallel preprocess slices
#Then use this to load those slices and just plot them real simple

# Parse args, Handle data, Animate, Output

# builtins
import os
import time
# package module 
import parse 
verbose = False
booshow,boogif,boompg,boolog,filename = parse.parse2()
# matplotlib
import matplotlib
if booshow:
    matplotlib.use('tkagg')
else:
    matplotlib.use('Agg')
from matplotlib import animation
# numpy
import numpy as n
# package module
import tools

# BEGIN SETUP

gfps = 10

if booshow:
    pass
else:
    if boolog:
        logn = 'log'
    else:
        logn = 'lin'
    matplotlib.rcParams['animation.ffmpeg_path'] = 'ffmpeg'
    moviefile = 'movie'+logn+str(int(time.time()))+'.mp4'
    if boompg:
        # for web compatibility
        FFwriter = animation.FFMpegWriter(bitrate=1000,codec='libx264',extra_args=['-pix_fmt','yuv420p','-preset','slow','-profile:v','baseline','-level','3.0'],fps=gfps)
    else:
        # default 
        FFwriter = animation.FFMpegWriter(bitrate=1000,fps=gfps,codec='libx264',extra_args=['-crf','5','-preset','veryslow','-pix_fmt','yuv420p'])


#the options are there to enforce compatibility with the Chrome web browser

#        FFwriter = animation.FFMpegWriter(fps=gfps, codec='libvpx-vp9')
#        moviefile = 'movie'+logn+str(int(time.time()))+'.webm'


if boolog:
    pass
else:
    tools.gnorm = None
#default norm is LogNorm

# END SETUP
# BEGIN HANDLE DATA
t0 = time.time()
datalist = n.load(filename)
# if datalist is 4-d it is multiple datasets
if len(datalist.shape) == 4:
    pass
else:
    datalist = [datalist]
ds = datalist.shape
vmin0 = n.zeros(ds[0])
vmax0 = n.zeros(ds[0])
for i in range(ds[0]):
    vmax0[i] = n.max(datalist[i])
    if boolog:
        vmin0[i] = n.min(datalist[i][datalist[i] > 0])
    else:
        vmin0[i] = n.min(datalist[i])
y = n.arange(ds[2])
x = n.arange(ds[3])
# END HANDLE DATA

# ANIMATE SETUP
nw = ds[0]
nh = 1
ns = 5
numplots = ds[0]
fig,axs,divs = tools.makead(nw,nh,ns,numplots)
tp = time.time()

def animate(i):
    if (i%5 == 0):
        totali = ds[1]
        timeelapsed = time.time() - tp
        estimatedtime = (timeelapsed * float(totali - i)) / float(i+1)
        print('frame',i,estimatedtime,'seconds left')

    cbbool = (i == 0)
    ni = 0
    output = tools.plotframe(x,y,datalist[ni][i],axs,divs,ni,vmin0,vmax0,cbbool)
    if (numframes > 1):
        axs[ni].contour(datalist[1][i],origin='lower',levels=[0])
        ni = 1
        output = tools.plotframe(x,y,datalist[ni][i],axs,divs,ni,vmin0,vmax0,cbbool)

    axs[0].set_title('Frame ' + str(i))
    return output

maxframes = 400
numframes = min(maxframes,ds[1])
if numframes == maxframes:
    print('Warning: Maxframes = ',maxframes)
print('Frames:',numframes)
# ANIMATE LOOP
anim = animation.FuncAnimation(fig,animate,init_func=tools.init,frames=numframes,interval=40)
# END ANIMATE

# BEGIN OUTPUT

if booshow:
    pass
else:
    anim.save(moviefile,
              writer=FFwriter)

## palette makes the gif much nicer
## the quotes around palettegen and paletteuse are not necessary
if boogif:
    os.system('ffmepg -i '+moviefile+' -vf "palettegen" -y palette.png')
    os.system('ffmpeg -i '+moviefile+' -i palette.png -lavfi "paletteuse" -y movie.gif')
if booshow:
    tools.plt.show()
##

t1 = time.time()
print('Seconds to complete task:',t1-t0)
# END OUTPUT
