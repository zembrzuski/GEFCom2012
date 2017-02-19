import numpy as np
import copy

def from_string_to_int(string):
    return int(string.replace(',', '')) if string != '' else None

def raw_row_to_dict(row):
    return {
        'zone_id': int(row[0]),
        'year': int(row[1]),
        'month': int(row[2]),
        'day': int(row[3]),
        'hours': list(map(lambda x: from_string_to_int(x), row[4:]))
    }

def year_month_day_predicate(year, month, day):
    return lambda dict_inp: dict_inp['year'] == year and dict_inp['month'] == month and dict_inp['day'] == day


def normalize(x):
    my_copy = copy.deepcopy(x)
    hours = my_copy['hours']

    normalized = hours / np.linalg.norm(hours)
    my_copy['normalized'] = normalized
    return my_copy


def remove_non_available_data(x):
    return x['hours'][23] != None