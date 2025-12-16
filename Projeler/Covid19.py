from turtle import title
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Direkten githubeden veri okuma
data = pd.read_csv(r"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/refs/heads/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
print(data)
print("---------------------")

data = data.drop(columns=["Province/State", "Lat", "Long"])
print(data)
print("---------------------")

data = data.groupby("Country/Region").aggregate(np.sum)
print(data)
print("---------------------")

#Satır ve sütunların yerlerini değiştirme
data = data.transpose()
print(data)
print("---------------------")

data.index.name = "Date"
print(data)
print("---------------------")

data = data.reset_index()
print(data)
print("---------------------")

melt_data = data.melt(id_vars=["Date"], var_name="Country", value_name="Cornfirmed")
print(melt_data)
print("---------------------")

max_date = melt_data["Date"].max()
print(max_date)
print("---------------------")

print(type(max_date))
print("---------------------")

melt_data["Date"] = pd.to_datetime(melt_data["Date"], dayfirst=True)
print(melt_data)
print("---------------------")

max_date = melt_data["Date"].max()
print("Max Date:", max_date)
print("---------------------")

print(type(max_date))
print("---------------------")

melt_data["Date"] = melt_data["Date"].dt.strftime("%Y/%m/%d")
print(melt_data)
print("---------------------")

max_date = melt_data["Date"].max()
print(max_date)
print("---------------------")

enson = melt_data[melt_data["Date"] == max_date]
print(enson)
print("---------------------")

toplam = enson["Cornfirmed"].sum()
print(toplam)
print("---------------------")

figure = px.bar(enson, x="Country", y="Cornfirmed")
figure.show()
print("---------------------")

figure = px.bar(enson.sort_values("Cornfirmed", ascending=False), x="Country", y="Cornfirmed")
figure.show()
print("---------------------")

figure = px.bar(enson.sort_values("Cornfirmed", ascending=False).head(20), x="Country", y="Cornfirmed", text="Cornfirmed")
figure.show()
print("---------------------")

figure = px.line(melt_data[melt_data["Country"] == "Turkey"], x="Date", y="Cornfirmed")
figure.show()
print("---------------------")

figure = px.scatter(melt_data, x = "Date", y = "Cornfirmed", color = "Country")
figure.show()
print("---------------------")

fig = go.Figure()
fig.add_trace(go.Indicator(mode = "number", value =toplam,number={"valueformat": "0.f"},
              title = {"text": "Toplam Vaka Sayısı"}, domain={"row":0, "column":0}))
fig.show()
print("---------------------")

pd.set_option("mode.chained_assignment", None)
fig = px.choropleth(enson, 
                   locations="Country", 
                   locationmode="country names", 
                   color_continuous_scale="dense",
                   color="Cornfirmed",  # Sadece sütun adı, liste değil
                   range_color=(0,9))
fig.show()
print("---------------------")

k = melt_data.groupby("Date").aggregate(np.sum)
k = k.reset_index()
k["Gunluk Vaka Sayısı"] = k["Cornfirmed"].diff()
print(k)
print("---------------------")
