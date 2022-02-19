import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
def solve(S):
    sigma=0.3
    r=0.12
    T=1
    t=0
    T=float(T)
    S=float(S)
    sigma=float(sigma)
    t=float(t)
    r=float(r)
    def f(x):
        return norm.cdf((0.165+np.log(S/x))/0.3)
    return quad(f,0,50)[0]-quad(f,50,100)[0]
    
if __name__=="__main__":
    D1=solve(10)
    print(D1)
    D2=solve(30)
    print(D2)
    D3=solve(50)
    print(D3)
    D4=solve(70)
    print(D4)
    D5=solve(90)
    print(D5)