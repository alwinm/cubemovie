# First (parallel) preprocess slices into 3-D array
# Then use this to turn 3-D array into movie

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
vmax0 = [n.max(datalist)]
if boolog:
    vmin0 = [n.min(datalist[datalist > 0])]
else:
    vmin0 = [n.min(datalist)]
ds = datalist.shape
y = n.arange(ds[1])
x = n.arange(ds[2])
# END HANDLE DATA

# ANIMATE SETUP
nw = 1
nh = 1
ni = 0
ns = 5
numplots = 1
fig,axs,divs = tools.makead(nw,nh,ns,numplots)
tp = time.time()
def animate(i):
    totali = ds[0]
    timeelapsed = time.time() - tp
    estimatedtime = (timeelapsed * float(totali - i)) / float(i+1)
    print('frame',i,estimatedtime,'seconds left')#,28.0-estimatedtime,error)
    cbbool = (i == 0)
    output = tools.plotframe(x,y,datalist[i],axs,divs,ni,vmin0,vmax0,cbbool)
    axs[0].set_title('Frame ' + str(i))
    return output

maxframes = 400
numframes = min(maxframes,ds[0])
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
