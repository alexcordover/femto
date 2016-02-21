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
decimals_a = 4
decimals_b = 2
decimals_c = 5

'''
Helper Functions
'''
def svd_recon_components(arr,n_vec,n1,n2,n3):
    u, s, v = np.linalg.svd(arr)
    return [np.round(u[:, :n_vec],decimals=n1),np.round(s[:n_vec],decimals=n2),np.round(v[:n_vec, :],decimals=n3)]

'''
CODE STARTS HERE
'''

images =['JPCLN001.tif']
for img_name in images:
    img = misc.imread('images/'+img_name,flatten=True)
    (a,b,c) = svd_recon_components(img,num_vecs,decimals_a,decimals_b,decimals_c)
    re_matrix = np.matrix(a) * np.diag(b) * np.matrix(c)

    json_dict = {}
    json_dict['a'] = a.tolist()
    json_dict['b'] = b.tolist()
    json_dict['c'] = c.tolist()

    with open('new_grayscale_data.txt','w') as outfile:
        json.dump(json_dict,outfile)

    misc.imsave('images_out/'+'grayscale_'+img_name,np.asarray(re_matrix))
