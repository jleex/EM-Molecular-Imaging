import numpy as np
import mrcfile as mf
import scipy as sp
import glob
import os

def back_proj():
    m = 0
    b = np.zeros((153,153,153), np.float32)

    abini = np.zeros((3,3))
    for filename in glob.glob(os.path.join('/Users/joellee/Desktop/Images', '*_image.txt')):
        for aibi in glob.glob(os.path.join('/Users/joellee/Desktop/Images', '*_orientation.txt')):
            if filename[30:31] == aibi[30:31]:
                image = np.loadtxt(filename)
                ab = np.loadtxt(aibi)
                image_hat = np.fft.fftshift(np.fft.fftn(image))
                
                N = 153

                omegaz = np.arange((-N-1)/2,(1+N)/2)        
                l = np.zeros(N)
                l_hat = np.zeros(N)
                
                for j in range(0,N-1):
                    l[j] = omegaz[j]*np.sinc(omegaz[j]) 
                    l_hat[j] = np.fft.fftshift(np.fft.fftn(l[j]))

                
                l_hat3 = np.tile(l_hat, (153,153,1))
                image_hat3 = np.tile(image_hat, (153,1,1))      #now both are 153x153x153
                print(l_hat3.shape)
                print(image_hat3.shape)
                b_hat = np.multiply(image_hat3, l_hat3)            #pointwise multiply
                print(b_hat.shape)
                
                if m == 0:
                    abini = ab
                
                b = b + np.fft.ifftn(np.fft.ifftshift(b_hat)) #figure this rotating the grid thingy
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
