import numpy as np
import matplotlib.pyplot as plt
S= np.linspace(1,1,140)
def calculate(T,S,K,sigma,r):
   T=float(T)
   S=float(S)
   K=float(K)
   sigma=float(sigma)
   r=float(r)
   C=max(S-K,0)
   P=max(K-S,0)
   return C,P
T=1
S=0
sigma=0.3
r=0.12
def plot_graphs():
  X=[]
  Y0_1=[]
  Y0_2=[]
  Y0_3=[]
  Y1_1=[]
  Y1_2=[]
  Y1_3=[]
  Y1_4=[]

  Y=[]
  for i in range(140):
      C1,P1=calculate(T,i+1,20,sigma,r)
      C2,P2=calculate(T,i+1,40,sigma,r)
      C3,P3=calculate(T,i+1,60,sigma,r)
      C4,P4=calculate(T,i+1,80,sigma,r)
      Y0_1.append(C2/20)
      Y0_2.append(-1*C3/20)
      Y0_3.append((C2-C3)/20)
      Y1_1.append(C1/20)
      Y1_2.append(-C2/20)
      Y1_3.append(-C3/20)
      Y1_4.append(C4/20)
      Y.append((C1+C4-C2-C3)/20)
      X.append(i+1)
  plt.figure()
  plt.title('')
  plt.plot(X,Y0_1,linestyle='dashed',color='palevioletred')
  plt.plot(X,Y0_2,linestyle='dashed',color='lightseagreen')
  plt.plot(X,Y0_3,linestyle='solid',color='limegreen')
  plt.xlabel('Stock Price at expiry')
  plt.ylabel('Payoff')
  plt.grid('on')
  plt.legend(['Long Call at strike $40','Short Call at strike $60','Net Payoff'])
  plt.show()

  plt.figure()
  plt.title('')
  plt.plot(X,Y1_1,linestyle='dashed',color='mediumslateblue')
  plt.plot(X,Y1_2,linestyle='dashed',color='palevioletred')
  plt.plot(X,Y1_3,linestyle='dashed',color='lightseagreen')
  plt.plot(X,Y1_4,linestyle='dashed',color='plum')
  plt.plot(X,Y,linestyle='solid',color='limegreen')
  plt.xlabel('Stock Price at expiry')
  plt.ylabel('Payoff')
  plt.grid('on')
  plt.legend(['Long Call at strike $20','Short Call at strike $40','Short Call at strike $60','Long Call at strike $80','Net Payoff'],loc=4)
  plt.show()
if __name__=='__main__':
  plot_graphs()


