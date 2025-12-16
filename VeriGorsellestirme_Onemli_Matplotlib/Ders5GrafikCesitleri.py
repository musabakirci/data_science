import numpy as np
import matplotlib.pyplot as plt
data1 = np.linspace(0,10,20) # 0 ile 10 arasında 20 eşit parçaya ayır
print(data1)
data2 = data1**2

# scatter plot
plt.scatter(data1, data2, color = "green", marker = "o", s = 100)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("X ve Y İlişkisi")
plt.show()

#histogram
new_arr = np.random.randint(0,200,50)
plt.hist(new_arr)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("X ve Y İlişkisi")
plt.show()

#box plot
new_arr = np.random.randint(0,200,50)
plt.boxplot(new_arr)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("X ve Y İlişkisi")
plt.show()