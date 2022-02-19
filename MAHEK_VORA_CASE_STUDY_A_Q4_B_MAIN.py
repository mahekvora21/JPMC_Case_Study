import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
#increasing the x axis dimensions, to calculate slope at S=125
S= np.linspace(1,1,140)
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
T=1
S=0
K=50
sigma=0.3
r=0.12
def plot_graphs(t):
  X=[]
  Y1=[]
  Y2=[]
  for i in range(140):
    #store coordinates for these points, S=124 and 126
      if((i+1)==124):
           call_124=C
           put_124=P
      if((i+1)==126):
           call_126=C
           put_126=P
      C,P=calculate(T,i+1,K,sigma,t,r)
      Y1.append(C)
      Y2.append(P)
      X.append(i+1)
  plt.figure()
  plt.plot(X,Y1,linestyle='dashed',color='magenta')
  x = [124,126]
  y = [call_124,call_126]
  plt.text(124-25, call_124+2.5, '({}, {})'.format(124, call_124))
  plt.text(126-25, call_126-2.5, '({}, {})'.format(126, call_126))
  plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
 
  plt.grid('on')
  plt.xlabel('Stock price at time t')
  plt.ylabel('Call option price')
  plt.title('For call option at t = '+str(t))
  plt.show()
  plt.figure()
  plt.plot(X,Y2,linestyle='dashed',color='magenta')
  x2 = [124,126]
  y2 = [put_124,put_126]
  #plot points and coordinates 
  plt.text(124-35, put_124+4.5, '({}, {})'.format(124, put_124))
  plt.text(126-35, put_126+2.5, '({}, {})'.format(126, put_126))
  print(put_124,put_126,(put_124-put_126)/2)
  plt.plot(x2, y2, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
 
  plt.grid('on')
  plt.xlabel('Stock price at time t')
  plt.ylabel('Put option price')
  plt.title('For put option at t = '+str(t))
  plt.show()
if __name__=='__main__':
  plot_graphs(0)
  plot_graphs(0.5)
  plot_graphs(1)

