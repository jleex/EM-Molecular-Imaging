import numpy as np
import mrcfile as mf
import scipy as sp
import glob
import os
#mrcfiles are volumes

#this is your orientation data                    

#L = length(image in images)   #is from proj_fst     need this?

##def delta(x):
##    #FIGURE THIS OUT
##    return
##
##def rect(x):
##    return 1 if abs(x) <= L/2 else 0 

##def abwrite():
##    a = input('a')
##    b = input('b')
##    output = mf.new('/Users/joellee/Desktop/Images/[1aibi.mrc')
##    output.close()
##    overwrite = True
b = 0

def back_proj():
    #check up for proj_fst to have the orientations built in
    
    #implement if no aibi

    
    m = 0
    
    for filename in glob.glob(os.path.join('/Users/joellee/Desktop/Images', '*.mrc')):  #check this later and update path
        image = mf.open(filename)
        image_hat[image] = np.fft.fftshift(np.fft.fftn(image))               #shift after transform
        ab = aibi[n]
   
        m = m+1

        N = length(image_hat)                   #image dimension
        l = np.zeroes[length(images)]           #sets up the l matrix
        omegaz = np.meshgrid(np.arange((-N-1)/2,(1+N)/2))         #figure out the omegaz
        
        
        #F{bj} = F{Ij}F{lj} 
        for j in length(image):                     #this gives you the lj function
            l[j] = omegaz(j)*np.sinc(omegaz(j))     #figure out omegaz check the sinc
            l_hat[j] = np.fft.fftshift(np.fft.fftn(l[j]))            #check if you have to shift
            
        
        l_hat3 = np.tile(l_hat, (2,1))               #figure out the axes tiling is because you want it constant in the other dimensions 
        image_hat3 = np.tile(image_hat, (2,1))        
        
        b_hat = np.multiply(image_hat, l_hat)            #pointwise multiply

        if n == 1:
            b = b + np.fft.ifftn(np.fft.ifftshift(b_hat))      #shiftback then transform figure out the rotation
        else:
            b = b + 'rotation'*np.fft.ifftn(np.fft.ifftshift(b_hat))
    

    #somehow sum them up
    #straight sum the matrices pointwise is normals

    output = mf.new('/Users/joellee/Desktop/images/back_proj.mrc')
    output.set_data(b.ascontiguoustype(np.float32))
    output.close()
    overwrite=True
    
    print(b)
    
    return b


##abwrite()
back_proj()
