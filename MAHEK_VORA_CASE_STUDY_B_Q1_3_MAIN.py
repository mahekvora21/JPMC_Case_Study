import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# 1st part- which is the same as a generalized version of the code for n=3
def find_area_ratio(n, generate_plots, show_answer,show_roundoff_answer):
  def f(x):
    return x/n
  def g(x):
    return ((-1)*(np.sqrt(1-(x-1)**2))+1)
  def h(x):
    return np.minimum(g(x),f(x))
  
  # can be passed as true if we want to see the figure as n varies
  if generate_plots:
    x = np.linspace(0,1,1000)

    plt.plot(x,f(x))
    plt.plot(x,g(x))

    plt.fill_between(x, f(x), color = "cyan",alpha = 0.3, hatch = '|')
    plt.fill_between(x, g(x), color = "pink", alpha = 0.2, hatch = '-')
    plt.show()

    plt.plot(x,h(x))
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.fill_between(x, h(x), color = "magenta",alpha = 0.3, hatch = '|')
    plt.show()
  
  # area B and area Total are computed by integration
  B=quad(h,0,1)
  Total=quad(g,0,1)
  area_ratio=(Total[0]-B[0])/Total[0]
  if show_answer:
    print(area_ratio)
  if show_roundoff_answer:
    print(round(area_ratio))
  return area_ratio

# generating data for n=1 to n=23020, 
# this data will be used to find the lowest n required for getting a particular ratio.
# here(stored values from 1 to 23020) the values used are accurate, not rounded off to 5 places
def generate_area_ratio_vs_n(): 
 print('Started Execution, Please Wait...')
 X=[]
 Y=[]
 for i in range(23020):
   Y.append(find_area_ratio(1+i,False,False,False))
   X.append(i+1)
 plt.plot(X,Y)
 return X,Y
X,Y=generate_area_ratio_vs_n()
def find_lower_bounds(val,generate_plots,show_answer):
  ans=np.Inf
  for i in range(len(Y)):
    if Y[i]>=val:
      ans=(i+1)
      break
  if generate_plots:
    plt.figure()
    plt.grid(True)
    plt.xlim(1,max(23020,ans*2))
    plt.plot(X,Y)
    plt.show()
  if show_answer:
    print('The minimum n required to get the area ratio ' +str(val)+ ' is : '+str(ans))
  return ans

if __name__ == "__main__":
   find_lower_bounds(0.5,False,True)
   find_lower_bounds(0.7,False,True)
   find_lower_bounds(0.9,False,True)
   find_lower_bounds(0.999,False,True)
   find_lower_bounds(0.9999,False,True)
   find_lower_bounds(1.0,False,True)
   print('Done.')
