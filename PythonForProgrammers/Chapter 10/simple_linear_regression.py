import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


c = lambda f: 5 / 9 * (f - 32)
temps = [(f, c(f)) for f in range(0, 101, 10)]

temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])
axes = temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')
y_label = axes.set_ylabel('Celsius')

la = pd.read_csv("ave_hi_la_jan_1895-2018.csv")

la.columns = ['Date', 'Temperature', "Anomaly"]
pd.set_option('precision', 2)
print(la.Temperature.describe())

linear_regression = stats.linregress(x=la.Date,
                                     y=la.Temperature)



