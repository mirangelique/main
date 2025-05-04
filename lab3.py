import matplotlib.pyplot as plt  # импорт библиотек
import pandas as pd
import statsmodels.api as sm
import seaborn as sns

# Задание 1
data = sm.datasets.cancer.load_pandas()
df = data.data
population_bins = [
    df['population'].min() - 1,
    df['population'].quantile(0.33),
    df['population'].quantile(0.66),
    df['population'].max() + 1,
]
population_labels = ['малые', 'средние', 'большие']

df['категория популяций'] = pd.cut(
    df['population'],
    bins=population_bins,
    labels=population_labels,
    include_lowest=True,
)


sns.scatterplot(
    x='cancer', y='population', hue='категория популяций', data=df
)
plt.title('Диаграмма рассеяния')
plt.xlabel('cancer')
plt.ylabel('population')
plt.show()


# Задание 2
dn = 'co2'
start = 1958
end = 1980

#загрузка набора данных
data = sm.datasets.co2.load_pandas()
df = data.data

#преобразование DatetimeIndex в столбец 'date'
df['date'] = df.index.to_series()  # преобразование в series
df = df.set_index('date')

#ограничение временного промежутка
df['year'] = df.index.year  # создание столбца 'year'
df = df[(df['year'] >= start) & (df['year'] <= end)]

#построение графика
plt.figure(figsize=(12, 6))
plt.plot(df['co2'], label='CO2 уровень')

plt.xlabel('Дата')
plt.ylabel('Уровень CO2')
plt.title(f'Уровень CO2 ({start}-{end})')
plt.legend()
plt.grid(True)
plt.show()