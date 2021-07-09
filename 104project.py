import statistics
import pandas as pd

df=pd.read_csv(r"C:\Users\ADMIN\Dropbox\My PC (DESKTOP-QH1TBQA)\Downloads\New folder (5)\Data-visualization-master\csv files\SOCR-HeightWeight.csv")
Weight=df["Weight(Pounds)"]
x=statistics.mean(Weight)
print(x)
y=statistics.median(Weight)
print(y)
z=statistics.mode(Weight)
print(z)