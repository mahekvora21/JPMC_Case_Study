import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# defining a function as the line(diagonal) and circle.
# area between minimum of these 2 functions and x axis is B

def find_area_ratio(generate_plots, show_roundoff_answer):
  def f(x):
    return x/3
  def g(x):
    return ((-1)*(np.sqrt(1-(x-1)**2))+1)
  def h(x):
    return np.minimum(g(x),f(x))
  
  # if we wish to generate plots this can be passed as true, the generated plot was used in Figure 10 by me
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
  
  # Calculate B by integration
  B=quad(h,0,1)
  # Total is the area between circle and X axis from x=0 to x=r, here r=1
  Total=quad(g,0,1)

  # A/Total=(Total-B)/Total
  area_ratio=(Total[0]-B[0])/Total[0]
  if show_roundoff_answer:
    print(round(area_ratio,5))
  return area_ratio

if __name__ == "__main__":
  find_area_ratio(False,True)
