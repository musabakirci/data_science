from xmlrpc.client import boolean
import pandas as pd
import numpy as np

data = np.random.randn(4, 3)
print(data)

data_frame = pd.DataFrame(data)
print(data_frame)
print(type(data_frame))

new_df = pd.DataFrame(data, index= ["Musa", "Pinar", "Miran", "Nazar"], columns=["Salary", "Age", "Department"])
print(new_df)
print(new_df["Salary"])
print(new_df["Age"])
print(new_df["Department"])
print(new_df.loc["Musa"]) # Musa'nın bilgilerini getirir.
print(new_df.iloc[0]) # İndex numarasına göre getirir.
print("************************")
print(new_df.iloc[:,2]) # Tüm herkesin departman bilgilerini getirir.
print("************************")
print(new_df.iloc[1:3, 0:2]) # 1. ve 2. indexteki kişilerin salary ve age bilgilerini getirir.

new_df["Extra"] = 10
print(new_df)
print("-------------------------")

print(new_df.drop("Extra", axis=1)) # Extra sütununu siler. Buradaki axis=1, sütun silineceğini belirtir.
print("-------------------------")

print(new_df) # Orijinal dataframe değişmedi. Sadece drop ile geçici olarak silindi.
print("-------------------------")

print(new_df.drop("Nazar", axis=0)) # Nazar isimli satırı siler. Buradaki axis=0, satır silineceğini belirtir.
print("-------------------------")

print(new_df.loc["Miran", "Salary"]) # Miran'ın maaşını getirir.
print("-------------------------")

print(new_df.iloc[2, 0]) # İndex numarasına göre Miran'ın maaşını getirir.
print("-------------------------")

boolean_frame = new_df > 0
print(boolean_frame) # Boolean değerler döner.
print("-------------------------")

boolean_frame2 = new_df[new_df["Salary"] > 0]
print(boolean_frame2) # İnteger değerler döner.
print("-------------------------")

print(new_df[new_df["Age"] > 0]) # Age bilgisi pozitif olanları getirir.
print("-------------------------")

print(new_df.reset_index()) # İndexi resetler ve default index atar.
print("-------------------------")

reset_frame = new_df.reset_index()
print(reset_frame.loc[0, "index"]) # Resetlenmiş indexin 0. satırındaki index bilgisini getirir.
print("-------------------------")

new_indices = ["Ati", "Zey", "Mir", "Naz"] # Yeni indexler
new_df["New_Indices"] = new_indices
print(new_df)
print("-------------------------")

print(new_df[new_df["New_Indices"] == "Ati"])
print("-------------------------")

# multi index
first_index = ["Simpson", "Simpson", "Simpson", "South Park", "South Park", "South Park"]
inner_index = ["Homer", "Marge", "Bart", "Stan", "Kyle", "Cartman"]
zipped_index = list(zip(first_index, inner_index))
print(zipped_index)
print("-------------------------")

zipped_index = pd.MultiIndex.from_tuples(zipped_index)
print(zipped_index)
print("-------------------------")

sample_values = np.ones((6,2)) # Örnek değerler
big_df = pd.DataFrame(sample_values, index=zipped_index, columns=["Age", "Salary"]) # MultiIndex ile oluşturulmuş DataFrame 
print(big_df)
print("-------------------------")

print(big_df[big_df["Age"] > 0]) # Yaşı 0'dan büyük olanları getirir.
print("-------------------------")

print(big_df.loc["Simpson"]) # Simpson ailesinin tüm bireylerini getirir.
print("-------------------------")
print(big_df.loc["Simpson"].loc["Homer"]) # Simpson ailesinden Homer'ı getirir.
