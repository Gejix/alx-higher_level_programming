#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    s = list(roman_string)
    for x in range(len(s)):
        array = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        number = [1, 5, 10, 50, 100, 500, 1000]
        for i in range(len(array)):
            if (s[x] == array[i]):
                s[x] = number[i]
                break
    if len(s) == 1:
        return (s[0])
    else:
        for x in range(1, len(s)):
            if s[x - 1] >= s[x]:
                result = result + s[x - 1]
            else:
                result = result - s[x - 1]
        result = result + s[x]
        return result
