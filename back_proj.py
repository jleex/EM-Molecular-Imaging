import numpy as np
import mrcfile as mf
import scipy as sp
import glob
import os

def back_proj():
    m = 0
    b = np.zeros((153,153,153), np.float32)
    for filename in glob.glob(os.path.join('/Users/joellee/Desktop/Images', '*.txt')):
        image = np.loadtxt(filename)
        image_hat = np.fft.fftshift(np.fft.fftn(image))
   
        N = 153                   #image dimension

        omegaz = np.arange((-N-1)/2,(1+N)/2)        #figure out the omegaz
        l = np.zeros(N)
        l_hat = np.zeros((N,N))
        #F{bj} = F{Ij}F{lj} 
        for j in range(0,N-1):                     #this gives you the lj function
            l[j] = omegaz[j]*np.sinc(omegaz[j])     #figure out omegaz check the sinc
            l_hat[j] = np.fft.fftshift(np.fft.fftn(l[j]))            #check if you have to shift
            
        
        l_hat3 = np.tile(l_hat, (2,1))               #figure out the axes tiling is because you want it constant in the other dimensions 
        image_hat3 = np.tile(image_hat, (2,1))        
        
        b_hat = np.multiply(image_hat, l_hat)            #pointwise multiply
        
        if m == 0:
            b = b + np.fft.ifftn(np.fft.ifftshift(b_hat))      #shiftback then transform figure out the rotation
        else:
            b = b + 'rotation'*np.fft.ifftn(np.fft.ifftshift(b_hat))
        m = m + 1

    #somehow sum them up
    #straight sum the matrices pointwise is normals
    b = np.real(b)
    b = np.float32(b)
    overwrite=True
    output = mf.new('/Users/joellee/Desktop/images/back_proj.mrc')
    output.set_data(b)
    overwrite=True
    output.close()

    return b


back_proj()

