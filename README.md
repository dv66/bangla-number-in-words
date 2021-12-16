# Bangla Number in Words
Converts a Bangla numeric string to literal words.
### Install
```bash
$ pip install banglanum2words
```

### Usage

Bangla number to words
```bash
>>> from banglanum2words import num_convert
>>> num_convert.number_to_bangla_words("১২৩৪")
'এক হাজার দুই শত চৌত্রিশ'
>>> num_convert.number_to_bangla_words("৩৪১২৩৪")
'তিন লক্ষ একচল্লিশ হাজার দুই শত চৌত্রিশ'
```

Bangla year in numbers to words
```bash
>>> from banglanum2words import num_convert
>>> num_convert.year_in_number_to_bangla_words("১৯৯৪")
'উনিশশো চুরানব্বই'
>>> num_convert.year_in_number_to_bangla_words("২০০৪")
'দুই হাজার চার'
```
