import numpy as np
import mrcfile as mf
from scipy.interpolate import interpn as ip
from scipy.interpolate import RegularGridInterpolator as RGI
from scipy.interpolate import griddata as gd
import glob
import os

def back_proj():
    m = 0
    b = np.zeros((153,153,153), np.float32)             #watch out for this and makes sure to change the dimension to the image resolutions
    abini = np.zeros((3,3))

    for filename in glob.glob(os.path.join('/Users/joellee/Desktop/Images', '*_image.txt')):
        for aibici in glob.glob(os.path.join('/Users/joellee/Desktop/Images', '*_orientation.txt')):
            if filename[30:31] == aibici[30:31]:
                image = np.loadtxt(filename)
                abc = np.loadtxt(aibici)
                image_hat = np.fft.fftshift(np.fft.fft2(image))

                N = image.shape[0]
                L = N*2
                
                omegaz = np.arange((-N-1)/2,(1+N)/2)        
                l = np.zeros(N)
                l_hat = np.zeros(N)
                
                for j in np.arange(N-1):
                    l[j] = L*L*np.sinc(L*omegaz[j]) 
                
                l_hat = np.fft.fftshift(np.fft.fftn(l))
                l_hat3 = np.tile(l_hat, (N,N,1))
                l_hat3 = np.transpose(l_hat3)
                
                image_hat3 = np.tile(image_hat, (N,1,1))

                b_hat = np.multiply(image_hat3, l_hat3)
                
                b_hatR = np.zeros((N,N,N))
                b_hat_Rot = np.zeros((N,N,N))
                b_space = np.linspace(0,N,N)
                
                b_hatR = RGI((b_space,b_space,b_space), b_hat, method='linear', bounds_error=False)
                
                if m == 0:
                    abcini = abc
                else:
                    for i in np.arange(N-1):
                        for j in np.arange(N-1):
                            for k in np.arange(N-1):
                                sample_point = np.array([i, j, k])
                                conv_sam_pt = np.matmul(sample_point, abc)
                                print(conv_sam_pt)
                                print(conv_sam_pt[0])
                                b_hat_Rot[i,j,k] = b_hatR[conv_sam_pt[0], conv_sam_pt[1], conv_sam_pt[2]]

                
                b = b + np.fft.ifftn(np.fft.ifftshift(b_hat_Rot)) #figure this rotating the grid thingy
                m = m + 1

    b = np.real(b)
    b = np.float32(b)
    output = mf.new('/Users/joellee/Desktop/images/back_proj.mrc')
    output.set_data(b)
    output.close()

##    b_hat = np.real(b_hat)
##    b_hat = np.float32(b_hat)
##    output = mf.new('/Users/joellee/Desktop/images/b_hat.mrc')
##    output.set_data(b_hat)
##    output.close()
##
##    image3 = np.tile(image, (N,1,1))
##    image3 = np.float32(image3)
##    output = mf.new('/Users/joellee/Desktop/images/image3.mrc')
##    output.set_data(image3)
##    output.close()
##
##    l3 = np.tile(l, (N,N,1))
##    l3 = np.float32(l3)
##    output = mf.new('/Users/joellee/Desktop/images/l3.mrc')
##    output.set_data(l3)
##    output.close()
##    
##    image_hat3 = np.real(image_hat3)
##    image_hat3 = np.float32(image_hat3)    
##    output = mf.new('/Users/joellee/Desktop/images/image_hat3.mrc')
##    output.set_data(image_hat3)
##    output.close()
##
##    l_hat3 = np.real(l_hat3)
##    l_hat3 = np.float32(l_hat3)    
##    output = mf.new('/Users/joellee/Desktop/images/l_hat3.mrc')
##    output.set_data(l_hat3)
##    output.close()


back_proj()
