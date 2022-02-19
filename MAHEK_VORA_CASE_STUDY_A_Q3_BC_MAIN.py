import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
#plotting option price vs stock price
S= np.linspace(0,1,100)
#using bsm formulae
def calculate(T,S,K,sigma,t,r):
    T=float(T)
    S=float(S)
    K=float(K)
    sigma=float(sigma)
    t=float(t)
    r=float(r)
    if t!=T:
        d1=(1/(sigma*np.sqrt(T-t)))*(np.log(S/K)+((r+(sigma*sigma/2))*(T-t)))
        d2=d1-sigma*(np.sqrt(T-t))
        C=S*(norm.cdf(d1))-norm.cdf(d2)*K*np.exp(-1*r*(T-t))
        P=norm.cdf(-d2)*K*np.exp(-1*r*(T-t))-S*(norm.cdf(-d1))
    if t==T:
        C=max(S-K,0)
        P=max(K-S,0)
    return C,P
T=1.0
K=50.0
sigma=0.3
r=0.12
def plot_graphs(t):
   X=[]
   Y1=[]
   Y2=[]
  
   for i in range(100):
       C,P=calculate(T,i+1,K,sigma,t,r)
       Y1.append(C)
       Y2.append(P)
       X.append(i+1)
   
   #graphs for call
   plt.figure()
   plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
   plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
   plt.plot(X,Y1,linestyle = 'solid',color='green')
   plt.grid('on')
   plt.xlabel('Stock price')
   plt.ylabel('Call option price')
   plt.title('For call option at t = '+str(t))
   plt.legend(['Call option price'],loc=4)
   plt.show()
 
   #graphs for put
   plt.figure()
   plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
   plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
   plt.plot(X,Y2,linestyle = 'solid',color='green')
   plt.grid('on')
   plt.xlabel('Stock price')
   plt.ylabel('Put option price')
   plt.title('For put option at t = '+str(t))
   plt.legend(['Put option price'])
   plt.show()
 
#plotting all the cases by calling the main function
if __name__=='__main__':
   plot_graphs(0)
   plot_graphs(0.5)
   plot_graphs(1)
