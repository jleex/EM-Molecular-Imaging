import numpy as np
import mrcfile as mf
import scipy as sp

aibi_file = mf.open(/Users/'ME'/Desktop/Images/'aibi.mrc')
aibi = aibi_file.data
#this is your orientation data                    
                    
L = length(image in images)   #figure this out as well

def delta(x):
    #FIGURE THIS OUT

def rect(x):
    return 1 if abs(x) <= L/2 else 0 
    
def back_proj(images,aibi):
    n = 0 
    for filename in glob.glob(os.path.join(/Users/ME/Desktop/Images, '*.mrc')):  #check this later and update path
        image = mf.open(filename)
        image_hat[image] = np.fft.fftn(image)               #check if you have to shift
        ab = aibi[n]
   
        n = n+1
                    
        l = np.zeroes[length(images)]
        omegaz =                                    #figure out the omegaz
        
        
        #F{bj} = F{Ij}F{lj}
        for j in length(image):                     #this gives you the lj function
            l[j] = omegaz(j)*np.sinc(omegaz(j))     #figure out omegaz check the sinc
            l_hat[j] = np.fft.fftn(l[j])            #check if you have to shift
            
        
        l_hat3 = np.append(l_hat, zeroes, zeroes, 0)    #add two dimensions of 0s
        image_hat3 = np.append(l_hat, zeroes, 0)        #add 1 dimension of 0s
        
        b_hat = np.multiply(image_hat,l_hat)            #pointwise multiply
        bi = np.fft.ifftn(Fb)                            #shift?
    
    
    
    #somehow sum them up
    
    return b


print(b)
#figure out how to write to an mrcfile
