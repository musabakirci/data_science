import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#box plot
# median, quartile (25%, 50%, 75%) ve min-max 1.5 * IQR, outlier

data = np.array([5, 7, 9, 15, 20, 22, 25, 32, 35, 37, 40, 50, 55, 60, 100])

plt.figure(figsize=(7,5))
sns.boxplot(y=data)
plt.ylabel("Data Values")
plt.title("Box Plot")
plt.grid(True) # Arka plandaki çizgileri gosterir
plt.show()
"""
Boxplotta veriler anlamli bir sirada yer almalidir. Veriler arasinda uçuk ve yüksek farklar olmamalidir.
Bir veri grubunun ortalama, medyani, minimum ve maksimum degerlerini gosterir. 
"""
