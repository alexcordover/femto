import numpy as np
import math
import colorsys
from scipy import ndimage
from scipy import misc
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
import json

'''
Constants
'''

num_vecs = 256
n_a=4
n_b=2
n_c=5

'''
Helper Functions
'''
def svd_recon_components(arr,n_vec,n1,n2,n3):
    u, s, v = np.linalg.svd(arr)
    return [np.round(u[:, :n_vec],decimals=n1),np.round(s[:n_vec],decimals=n2),np.round(v[:n_vec, :],decimals=n3)]

'''
CODE STARTS HERE
'''

images =['image5.jpg']
for img_name in images:
    img = misc.imread('images/'+img_name,flatten=True)
    #misc.imsave('images_out/'+'grayscale_'+img_name,np.asarray(img))
    (u,s,v) = svd_recon_components(img,num_vecs,n_a,n_b,n_c)
    
    print((u,s,v))
