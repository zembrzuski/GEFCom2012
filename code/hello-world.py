import csv
import cool_functions
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

load_history = csv.reader(open('../datasets/Load_history.csv'))
header = next(load_history)

predicate = cool_functions.year_month_day_predicate(2005, 1, 1)

my_data = list(map(lambda row: cool_functions.raw_row_to_dict(row), load_history))
only_available_data = filter(lambda x: cool_functions.remove_non_available_data(x), my_data)
my_data_normalized = list(map(lambda x: cool_functions.normalize(x), only_available_data))
filtered = list(filter(lambda x: predicate(x), my_data_normalized))


"""
Plotting line charts
"""
fig, ax = plt.subplots()

for i in range(20):
    ax.plot(filtered[i]['normalized'], label=filtered[i]['zone_id'])

fontP = FontProperties()
fontP.set_size('small')

legend = ax.legend(bbox_to_anchor=(1.1, 1.05))

frame = legend.get_frame()

for label in legend.get_texts():
    label.set_fontsize('small')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

plt.show()
