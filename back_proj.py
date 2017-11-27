import numpy as np
import mrcfile as mf
import scipy as sp

image_file = mf.open('images.mrc') #give the full path or find the images later on
aibi_file = mf.open('orientations.mrc')

images = image_file.data
aibi = aibi_file.data

L = length(image in images)

def delta(x):
    #FIGURE THIS OUT

def rect(x):
    return 1 if abs(x) <= L/2 else 0 
    
def back_proj(images,aibi):
    for image in images:
        fftimages[image] = np.fft.fftn(image)
    for ab in aibi:
        ci = np.cross(ab)
    
    l = np.zeroes[length(images)]
    
    #F{bj} = F{Ij}F{lj}
    for j in length(image):
         l[j] = 1/(pi*(omegaz(j)))*sin(2*pi*L/2*omegaz(j))
         Fl[j] = np.fft.fftn(l[j])
          
    #pointwise multiply
    Fb = np.multiply(fftimages,Fl)
    b = np.fft.ifftn(Fb)
    
    
    #somehow sum them up
    
    return b
