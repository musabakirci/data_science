from hmac import new
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

data1 = np.linspace(0,10,20) # 0 ile 10 arasında 20 eşit parçaya ayır
print(data1)
data2 = data1**2

my_fig, my_axes = plt.subplots()
my_axes.plot(data1, data2, "r")
my_axes.plot(data2, data1, "g")
my_axes.set_xlabel("X Axis")
my_axes.set_ylabel("Y Axis")
my_axes.set_title("X ve Y İlişkisi")
plt.show()

(new_fig, new_axes)=plt.subplots()
new_axes.plot(data1, data1+2, color = "blue", linewidth = 1.2)
new_axes.plot(data1, data1+3, color = "red", linewidth = 3, linestyle = "dashed", marker = "o", markersize = 10, markerfacecolor = "green")
new_axes.plot(data1, data1+6, color = "yellow", linewidth = 2, linestyle = "solid", marker = "v", markersize = 12, markerfacecolor = "blue")
new_axes.plot(data1, data1+4, color = "green", linewidth = 2, linestyle = "dotted")
plt.show()