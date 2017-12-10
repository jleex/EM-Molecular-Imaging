import numpy as np
import mrcfile as mf
from scipy.interpolate import interpn as ip
from scipy.interpolate import RegularGridInterpolator as RGI
from scipy.interpolate import griddata as gd
import glob
import os
from itertools import product

def back_proj():
    b_ = np.zeros((153,153,153), np.float32)             #watch out for this and makes sure to change the dimension to the image resolutions
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
                
                b_space = np.linspace((1-N)/2,(N-1)/2,N)

                
                #build a grid to eval RGI on

                xcoor = np.array(b_space)
                ycoor = np.array(b_space)
                zcoor = np.array(b_space)
                xctr, yctr, zctr = xcoor+(N-1)/2, ycoor+(N-1)/2, zcoor+(N-1)/2
                a = abc[:,0]
                b = abc[:,1]
                c = abc[:,2]

                x_rot = (xcoor[:, np.newaxis]*a)+(N-1)/2
                print(x_rot)
                y_rot = (ycoor[:, np.newaxis]*b)+(N-1)/2
                z_rot = (zcoor[:, np.newaxis]*c)+(N-1)/2
                x_rot = x_rot[:,0]
                y_rot = y_rot[:,0]
                z_rot = z_rot[:,0]

                if x_rot[0] >= x_rot[15]:
                    x_rot = x_rot[::-1]
                if y_rot[0] >= y_rot[15]:
                    y_rot = y_rot[::-1]
                if z_rot[0] >= z_rot[15]:
                    z_rot = z_rot[::-1]
                
                b_ini = np.fft.ifftn(np.fft.ifftshift(b_hat))
                b_ini_real = np.real(b_ini)
                
                b_f = RGI((x_rot,y_rot,z_rot), b_ini_real, method='linear', bounds_error=False, fill_value=0)

                b_int = np.zeros((N,N,N))
                for i in np.arange(N-1):
                    for j in np.arange(N-1):
                        for k in np.arange(N-1):
                            b_int[i,j,k] = b_f(np.array([i, j, k]))        #figure this rotating the grid thingy
                                            
                b_ = b_ + b_int
                print(b_.shape)
                print(b_int.shape)
                print(b_)
                print(b_int)
    
    b_ = np.real(b_)
    b_ = np.float32(b_)
    output = mf.new('/Users/joellee/Desktop/images/back_proj.mrc')
    output.set_data(b_)
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
