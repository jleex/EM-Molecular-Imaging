import mrcfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator as RGI
from numpy.fft import fftn, fftshift, ifft2

zika_file = mrcfile.open('/Users/joellee/Desktop/zika_153.mrc', mode='r+')
mol = zika_file.data

def project_fst(rho, R):
    N = rho.shape[0]
    N_range = np.linspace(-1, 1, N)
    rho_hat_f = RGI((N_range, N_range, N_range), rho, bounds_error=False, method='linear', fill_value=0)
   
    grid = np.concatenate((N_range.reshape(N, 1, 1, 1) * np.ones(N * N).reshape(1, N, N, 1),
                          N_range.reshape(1, N, 1, 1) * np.ones(N * N).reshape(N, 1, N, 1),
                          N_range.reshape(1, 1, N, 1) * np.ones(N * N).reshape(N, N, 1, 1)),
                         axis=3)
    
    
    rho_hat = rho_hat_f(np.dot(grid, R))
    
    return np.real(ifft2(fftshift(fftn(rho_hat))[:,:,0]))

def random_rotation_matrix():
    e_1 = 2*np.random.rand(3) - 1
    e_1 /= np.linalg.norm(e_1)

    e_2 = np.cross( e_1, 2*np.random.rand(3) - 1 )
    e_2 /= np.linalg.norm(e_2)

    e_3 = np.cross( e_1, e_2 )
    e_3 /= np.linalg.norm(e_3)

    return np.array([e_1, e_2, e_3]).T

project_fst(mol, random_rotation_matrix())

image = project_fst(mol, random_rotation_matrix())
plt.imshow(image)
plt.show()

###written by joel below
##
##
##num = int(input('number of images you want'))
##N = 0
##
##rotationmatrix = random_rotation_matrix()
##image = project_fst(mol, rotationmatrix)
##np.savetxt('/Users/joellee/Desktop/Images/image.txt', image)
##N = N + 1
