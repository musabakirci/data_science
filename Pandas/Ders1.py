import numpy as np
import pandas as pd

grades = {"Musa": 50, "Ali": 60, "Ayşe": 70}
print(pd.Series(grades)) # Not: Series, bir veri çerçevesinin (DataFrame) tek bir sütununu temsil eder.

names = ["Musa", "Ali", "Ayşe"]
grades = [50, 60, 70]

print(pd.Series(names))
print(pd.Series(grades))
print(pd.Series(data=grades, index=names))

# with numpy
numpy_array = np.array([50,40,30,20])
print(pd.Series(numpy_array))

print("***********************")

# arithmetic
contest_result = pd.Series(data=[1, 2, 3, 4], index=["Musa", "Ali", "Ayşe", "Fatma"])
contest_result2 = pd.Series(data=[5, 6, 7, 8], index=["Musa", "Ali", "Ayşe", "Fatma"])

print(contest_result["Musa"])
print(contest_result2["Ali"])

final_result = contest_result + contest_result2
print(final_result)

final_result2 = contest_result / contest_result2
print(final_result2)

print("***********************")

different_series = pd.Series(data=[10, 20, 30, 40], index=["Musa", "Ali", "Ayşe", "Fatma"])
different_series2 = pd.Series(data=[5, 6, 7, 8], index=["Musa", "Pinar", "Ali", "Zeynep"])

different_series_result = different_series + different_series2
print(different_series_result)