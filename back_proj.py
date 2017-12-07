import numpy as np
import mrcfile as mf
import scipy as sp
import glob
import os

def back_proj():
    m = 0
    b = np.zeros((153,153,153), np.float32)

    abini = np.zeros((3,3))
    N = 153
    L = N*2
    for filename in glob.glob(os.path.join('/Users/joellee/Desktop/Images', '*_image.txt')):
        for aibi in glob.glob(os.path.join('/Users/joellee/Desktop/Images', '*_orientation.txt')):
            if filename[30:31] == aibi[30:31]:
                image = np.loadtxt(filename)
                ab = np.loadtxt(aibi)
                image_hat = np.fft.fftshift(np.fft.fft2(image))
                

                omegaz = np.arange((-N-1)/2,(1+N)/2)        
                l = np.zeros(N)
                l_hat = np.zeros(N)
                
                for j in np.arange(N-1):
                    l[j] = L*L*np.sinc(L*omegaz[j]) 
                
                l_hat = np.fft.fftshift(np.fft.fftn(l))
                l_hat3 = np.tile(l_hat, (153,153,1))
                l_hat3 = np.transpose(l_hat3)
                
                image_hat3 = np.tile(image_hat, (153,1,1))      #now both are 153x153x153

                b_hat = np.multiply(image_hat3, l_hat3)            #pointwise multiply
                
                if m == 0:
                    abini = ab
                
                b = b + np.fft.ifftn(np.fft.ifftshift(b_hat)) #figure this rotating the grid thingy
                m = m + 1

    #somehow sum them up
    #straight sum the matrices pointwise is normals
    b = np.real(b)
    b = np.float32(b)
##    b_hat = np.real(b_hat)
##    b_hat = np.float32(b_hat)

    output = mf.new('/Users/joellee/Desktop/images/back_proj.mrc')
    output.set_data(b)
    output.close()
##    output = mf.new('/Users/joellee/Desktop/images/b_hat.mrc')
##    output.set_data(b_hat)
##    output.close()

##    image3 = np.tile(image, (153,1,1))
##    image3 = np.float32(image3)
##    output = mf.new('/Users/joellee/Desktop/images/image3.mrc')
##    output.set_data(image3)
##    output.close()

##    l3 = np.tile(l, (153,153,1))
##    l3 = np.float32(l3)
##    output = mf.new('/Users/joellee/Desktop/images/l3.mrc')
##    output.set_data(l3)
##    output.close()
##    
####    image_hat3 = np.real(image_hat3)
####    image_hat3 = np.float32(image_hat3)    
####    output = mf.new('/Users/joellee/Desktop/images/image_hat3.mrc')
####    output.set_data(image_hat3)
####    output.close()
##
##    l_hat3 = np.real(l_hat3)
##    l_hat3 = np.float32(l_hat3)    
##    output = mf.new('/Users/joellee/Desktop/images/l_hat3.mrc')
##    output.set_data(l_hat3)
##    output.close()


back_proj()
