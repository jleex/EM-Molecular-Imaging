import numpy as np
import mrcfile as mf
import scipy as sp

zika_file = mf.open('zika_153.mrc')


def project_fast(rho, a, b)
  rho_hat = np.fft.fftn(np.fft.fftshift(rho))
  
  N = length of rho 
  #get this^ later
  
  for i in range(N):
    for j in range(N):
      eta_x[i,j] = -N/2 + 1 + j*1
      eta_y[i,j] = 1 - N/2 + i
  
  eta_x, eta_y = [...,np.newaxis]  #check this
  
  grid = eta_x*a + eta_y*b        #sampling grid
  
  
  
  #sample rho_hat
  from sp import RegularGridInterpolator as RGI
  rho_hat_f = RGI(rho_hat) + 1*j*RGI(rho_hat)         #check this j
  
  imageab = rho_hat_f(grid)
  
  finalimage = np.fft.ifftn(np.fft.ifftshift(imageab))
  realfinalimage = np.real(finalimage)
  
  from matplotlib import pyplot as plt
  
  %matplotlib
  plt.imshow(realfinalimage)


try:
  rho = zika_file.data
  print(rho)
  a = [1,0,0]
  b = [0,1,0]
