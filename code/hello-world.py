import csv
from cool_functions import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

load_history = csv.reader(open('../datasets/Load_history.csv'))
header = next(load_history)

predicate = year_month_day_predicate(2004, 1, 1)

my_data = list(map(lambda row: raw_row_to_dict(row), load_history))
filtered = list(filter(lambda x: predicate(x), my_data))


"""
Plotting line charts
"""
fig, ax = plt.subplots()

for i in range(20):
    ax.plot(filtered[i]['hours'], label=filtered[i]['zone_id'])

fontP = FontProperties()
fontP.set_size('small')

legend = ax.legend(bbox_to_anchor=(1.1, 1.05))

frame = legend.get_frame()

for label in legend.get_texts():
    label.set_fontsize('small')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

plt.show()
