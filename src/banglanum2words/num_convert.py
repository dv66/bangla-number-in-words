from unicodedata import category
from num2words import num2words

digits = set(['১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '০'])
english_digits = {
    '১':'1', 
    '২':'2', 
    '৩':'3', 
    '৪':'4', 
    '৫':'5', 
    '৬':'6', 
    '৭':'7', 
    '৮':'8', 
    '৯':'9', 
    '০':'0'
}

bangla_numeric_words = {
    'zero':'শূন্য',
    'one':'এক',
    'two':'দুই',
    'three':'তিন',
    'four':'চার',
    'five':'পাঁচ',
    'six':'ছয়',
    'seven':'সাত',
    'eight':'আট',
    'nine':'নয়',
    "hundred" : "শত", 
    "thousand" : "হাজার", 
    "lakh" : "লক্ষ", 
    "crore" : "কোটি" ,
    "ten" : "দশ",
    "eleven" : "এগারো",
    "twelve" : "বারো",
    "thirteen" : "তেরো",
    "fourteen" : "চৌদ্দ",
    "fifteen" : "পনেরো",
    "sixteen" : "ষোল",
    "seventeen" : "সতেরো",
    "eighteen" : "আঠারো",
    "nineteen" : "উনিশ",
    "twenty" : "বিশ",
    "twenty-one" : "একুশ",
    "twenty-two" : "বাইশ",
    "twenty-three" : "তেইশ",
    "twenty-four" : "চব্বিশ",
    "twenty-five" : "পঁচিশ",
    "twenty-six" : "ছাব্বিশ",
    "twenty-seven" : "সাতাশ",
    "twenty-eight" : "আঠাশ",
    "twenty-nine" : "ঊনত্রিশ",
    "thirty" : "ত্রিশ",
    "thirty-one" : "একত্রিশ",
    "thirty-two" : "বত্রিশ",
    "thirty-three" : "তেত্রিশ",
    "thirty-four" : "চৌত্রিশ",
    "thirty-five" : "পঁয়ত্রিশ",
    "thirty-six" : "ছত্রিশ",
    "thirty-seven" : "সাইত্রিশ",
    "thirty-eight" : "আটত্রিশ",
    "thirty-nine" : "ঊনচল্লিশ",
    "forty" : "চল্লিশ",
    "forty-one" : "একচল্লিশ",
    "forty-two" : "বেয়াল্লিশ",
    "forty-three" : "তেতাল্লিশ",
    "forty-four" : "চুয়াল্লিশ",
    "forty-five" : "পঁয়তাল্লিশ",
    "forty-six" : "ছেচল্লিশ",
    "forty-seven" : "সাতচল্লিশ",
    "forty-eight" : "আটচল্লিশ",
    "forty-nine" : "ঊনপঞ্চাশ",
    "fifty" : "পঞ্চাশ",
    "fifty-one" : "একান্ন",
    "fifty-two" : "বায়ান্ন",
    "fifty-three" : "তেপ্পান্ন",
    "fifty-four" : "চুয়ান্ন",
    "fifty-five" : "পঞ্চান্ন",
    "fifty-six" : "ছাপ্পান্ন",
    "fifty-seven" : "সাতান্ন",
    "fifty-eight" : "আটান্ন",
    "fifty-nine" : "ঊনষাট",
    "sixty" : "ষাট",
    "sixty-one" : "একষট্টি",
    "sixty-two" : "বাষট্টি",
    "sixty-three" : "তেষট্টি",
    "sixty-four" : "চৌষট্টি",
    "sixty-five" : "পঁয়ষট্টি",
    "sixty-six" : "ছেষট্টি",
    "sixty-seven" : "সাতষট্টি",
    "sixty-eight" : "আটষট্টি",
    "sixty-nine" : "ঊনসত্তর",
    "seventy" : "সত্তর",
    "seventy-one" : "একাত্তর",
    "seventy-two" : "বাহাত্তর",
    "seventy-three" : "তেয়াত্তর",
    "seventy-four" : "চুয়াত্তর",
    "seventy-five" : "পঁচাত্তর",
    "seventy-six" : "ছিয়াত্তর",
    "seventy-seven" : "সাতাত্তর",
    "seventy-eight" : "আটাত্তর",
    "seventy-nine" : "ঊনআশি",
    "eighty" : "আশি",
    "eighty-one" : "একাশি",
    "eighty-two" : "বিরাশি",
    "eighty-three" : "তিরাশি",
    "eighty-four" : "চুরাশি",
    "eighty-five" : "পঁচাশি",
    "eighty-six" : "ছিয়াশি",
    "eighty-seven" : "সাতাশি",
    "eighty-eight" : "আটাশি",
    "eighty-nine" : "ঊননব্বই",
    "ninety" : "নব্বই",
    "ninety-one" : "একানব্বই",
    "ninety-two" : "বিরানব্বই",
    "ninety-three" : "তিরানব্বই",
    "ninety-four" : "চুরানব্বই",
    "ninety-five" : "পঁচানব্বই",
    "ninety-six" : "ছিয়ানব্বই",
    "ninety-seven" : "সাতানব্বই",
    "ninety-eight" : "আটানব্বই",
    "ninety-nine" : "নিরানব্বই"
}



def number_to_bangla_words_upto_millions(number_string:str):
    number_string = number_string.strip()
    num = int("".join([english_digits[bangla_digit] for bangla_digit in number_string]))

    try:
        eng_in_num_to_words = num2words(num, lang='en_IN')
        bangla_num_to_words_list = [bangla_numeric_words[word] for word in eng_in_num_to_words.replace(',', ' ').replace(' and ', ' ').split()]
        return ' '.join(bangla_num_to_words_list)
    
    except Exception as e:
        print(e)


def number_to_bangla_words(bangla_number:str):
    """ Converts a Bangla numeric string to literal words.

    Args:
        number_string: Bangla number as string. Example: "১২৩৪"

    Returns:
        Bangla number in words. Example: "এক হাজার দুই শত চৌত্রিশ"

    """
    chunk_upto_millions = 7
    rev_string = bangla_number[::-1]
    parts = [rev_string[i:i+chunk_upto_millions] for i in range(0, len(rev_string), chunk_upto_millions)]
    parts = [p[::-1] for p in parts]
    parts = parts[::-1]
    main_number = " কোটি ".join([number_to_bangla_words_upto_millions(part) for part in parts])
    main_number = main_number.replace("শূন্য", "")

    return " ".join(main_number.split())


def year_in_number_to_bangla_words(year_in_number:str):
    """ Converts a Bangla year in numeric form to literal words.

    Args:
        number_string: Bangla year in numbers as string. Example: "১৯৯৪"

    Returns:
        Bangla year in words. Example: "উনিশশো চুরানব্বই"

    """
    if (len(year_in_number) == 4 and year_in_number[1] != '০') or len(year_in_number) == 3:
        return number_to_bangla_words(year_in_number[:-2]) + "শো " + number_to_bangla_words(year_in_number[-2:])
    else:
        return number_to_bangla_words(year_in_number)
    






















