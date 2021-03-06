import sys
import getopt 
import argparse
def parse():
    booshow = False
    boogif = False
    boompg = False
    boolog = False
    opts,args = getopt.getopt(sys.argv[1:],'sgmlh')
    for opt,arg in opts:
        if opt == '-s':
            print('Show = True')
            booshow = True
        elif opt == '-g':
            print('Gif = True')
            boogif = True
        elif opt == '-m':
            print('Mpeg = True')
            boompg = True
        elif opt == '-l':
            print('Log = True')
            boolog = True
        elif opt == '-h':
            print('-h for help')
            print('-s for Show')
            print('-g for gif')
            print('-m for mpeg extra options')
            print('-l for log')
        else:
            pass
    return booshow,boogif,boompg,boolog

def parse2():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s',help=('show'),action='store_true')
    parser.add_argument('-g',help=('make gif'),action='store_true')
    parser.add_argument('-m',help=('more compatible mpeg'),action='store_true')
    parser.add_argument('-l',help=('log'),action='store_true')
    parser.add_argument('-fps',help=('fps'),type=int,default=10)
    parser.add_argument('-size',help=('matplotlib figsize'),type=float,default=5)
    parser.add_argument('files',nargs="*",help=('filenames'))
    args = parser.parse_args()
    booshow = args.s
    boogif = args.g
    boompg = args.m
    boolog = args.l
    gfps = args.fps
    files = [fn for fn in args.files if '.npy' in fn]
    if len(files) > 0:
        filename = files[0]
    else:
        filename = 'cube.npy'
    if booshow:
        print('Show = True')
    if boogif:
        print('Gif = True')
    if boompg:
        print('Mpeg = True')
    if boolog:
        print('Log = True')
    print('fps =',gfps)
    return booshow,boogif,boompg,boolog,gfps,filename,args
