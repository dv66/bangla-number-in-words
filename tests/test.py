import sys
sys.path.append('../')

from src.banglanum2words import num_convert


print(num_convert.number_to_bangla_words("৪০০০০০০০৪০০০০০০০৪৪৪৪৪৪৪"))
print(num_convert.year_in_number_to_bangla_words("১৪৯৪"))
print(num_convert.year_in_number_to_bangla_words("১৯৯৪"))
print(num_convert.year_in_number_to_bangla_words("৯৯৪"))
print(num_convert.year_in_number_to_bangla_words("৯১০৪"))
print(num_convert.year_in_number_to_bangla_words("৯৪"))
