import numpy as np
import mrcfile as mf
import scipy as sp

zika_file = mf.open('zika_153.mrc')  #give the full path to the file here


def project_fast(rho, a, b):
  rho_hat = np.fft.fftn(np.fft.fftshift(rho))
  
  N = length(rho)
  
  for i in range(N):
    for j in range(N):
      eta_x[i,j] = -N/2 + 1 + j*1
      eta_y[i,j] = 1 - N/2 + i
  
  eta_x, eta_y = [...,np.newaxis]  #check this
  
  grid = eta_x*a + eta_y*b        #sampling grid
  
  
  
  #sample rho_hat
  from sp import RegularGridInterpolator as RGI
  rho_hat_f = sp.interpolate.RGI(rho_hat, CHECK THIS )
  
  imageab = rho_hat_f(grid)
  
  finalimage = np.fft.ifftn(np.fft.ifftshift(imageab))
  realfinalimage = np.real(finalimage)
  
  from matplotlib import pyplot as plt

  plt.imshow(realfinalimage)


try:
  rho = zika_file.data
  print(rho)
  a = [1,0,0]
  b = [0,1,0]
