import csv
from cool_functions import *
import matplotlib.pyplot as plt

load_history = csv.reader(open('../datasets/Load_history.csv'))
header = next(load_history)

predicate = year_month_day_predicate(2004, 1, 30)

my_data = list(map(lambda row: raw_row_to_dict(row), load_history))
filtered = list(filter(lambda x: predicate(x), my_data))

for i in range(20):
    plt.plot(filtered[i]['hours'])

plt.show()

print(len(filtered))
