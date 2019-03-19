# cubemovie

Python code for transmuting numpy arrays into reasonable mp4 movies using matplotlib and ffmpeg. 

## Basic usage

Hold numpy array in a .npy file. 

Generate a .npy file from numpy.save(filename.npy,array).

A preprocessing script can produce all the frames and save them to a 3-D array of shape:

    [N_frames,N_vertical,N_horizontal] 

Then, run:

    python -m cubemovie.basic filename.npy

## Flags

    -l # uses lognorm to scale colors instead of linear
    -s # show movie instead of saving
    -m # alternate mpeg option for wider compatibility but worse quality
    -g # make a gif from the mp4 output
    -h # show help
    -fps N # set fps 
## Advanced usage example:

    python -m cubemovie.basic filename1.npy -l
    python -m cubemovie.mask  filename1.npy ignored_filename2.npy -l -s
    python -m cubemovie.basic filename1.npy -fps 5

## Files

parse.py parses the command line arguments: flags and filenames

tools.py contains some useful functions

basic.py is the main script

mask.py  is a specific application 

dict.py  is a specific application

## Mask

Given an array of shape 
    [2,N_frames,N_vertical,N_horizontal]
split into two arrays of shape 
    [N_frames,N_vertical,N_horizontal]
The first array is some original field, and the second array is like a mask: non-zero values in some areas, and 0 everywhere else. Both arrays are plotted side-by-side, and contours of the Mask (second array) are drawn over the Original (first array). 

## Dict

Given a python dictionary, plots the following according to the dictionary key:
contour-1: takes a mask of 0 and 1 and makes 2-D contour plot to delineate the boundaries in black
contour-2: takes a mask of 0 and 1 and makes 2-D contour plot to delineate the boundaries in red
scatter-x, scatter-y: given these, draw scatter points on top 
data: 