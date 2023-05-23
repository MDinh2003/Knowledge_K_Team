import numpy as np
#create
A=[[1,2,3],[4,5,6],[7,8,9]]
#savetxt
np.savetxt("savetxt.txt",A,fmt="%.2f",delimiter=' ')