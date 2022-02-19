import numpy as np
from scipy.stats import norm
def compute_slope(T,S,K,r,sigma,t,print_output):

 T=float(T)
 S=float(S)
 K=float(K)
 sigma=float(sigma)
 t=float(t)
 r=float(r)
 if t!=T:
    d1=(1/(sigma*np.sqrt(T-t)))*(np.log(S/K)+((r+(sigma*sigma/2))*(T-t)))
    nd1_call=norm.cdf(d1)
    neg_nd1_put=(-1)*norm.cdf(-1*d1)
    if print_output==True:
        print('t = '+str(t))
        print('d1      :'+str(d1))
        print('N(d1)   :'+str(nd1_call))
        print('-N(-d1) :'+str(neg_nd1_put))

 if t==T:
    d1=np.Inf
    nd1_call=norm.cdf(d1)
    neg_nd1_put=(-1)*norm.cdf(-1*d1)
    if print_output==True:
        print('t = 1')
        print('d1      :'+str(d1))
        print('N(d1)   :'+str(nd1_call))
        print('-N(-d1) :'+str(neg_nd1_put))
 return nd1_call,neg_nd1_put
 
if __name__ == "__main__":
 # Q4
 #  compute_slope(T,S,K,r,sigma,t,print_output)
  compute_slope(1,125,50,0.12,0.3,0,True)
  compute_slope(1,125,50,0.12,0.3,0.5,True)
  compute_slope(1,125,50,0.12,0.3,1,True)
 
