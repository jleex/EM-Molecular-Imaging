import numpy as np
import mrcfile as mf
from scipy.interpolate import interpn as ip
from scipy.interpolate import RegularGridInterpolator as RGI
from scipy.interpolate import griddata as gd
import glob
import os
from itertools import product

def estimate_orientations(tol):
    
    for image0 in glob.glob(os.path.join('/Users/joellee/Desktop/Images', '*_image.txt')):
        for image1 in glob.glob(os.path.join('/Users/joellee/Desktop/Images', '*_image.txt')):
            for image2 in glob.glob(os.path.join('/Users/joellee/Desktop/Images', '*_image.txt')):
                if image0[30:31] < image1[30:31] < image2[30:31]:
                    

                    print(image0[30:31], image1[30:31], image2[30:31])
                    image_0 = np.loadtxt(image0)
                    image_1 = np.loadtxt(image1)
                    image_2 = np.loadtxt(image2)
                    print(image_0[76,76], image_1[76,76],image_2[76,76])

                    #figure out the lines

                    



tol = input('Tolerance')
estimate_orientations(tol)                    
            
        
