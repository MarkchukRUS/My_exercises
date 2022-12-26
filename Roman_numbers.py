def from_roman(roman_num):
    result_pause = 0
    result = 0
    counter = 0
    roman_numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in roman_num:
        if counter == 0:
            if roman_numbers[i] >= roman_numbers[roman_num[counter+1]]:
                result += roman_numbers[i]

        elif counter != len(roman_num)-1:
            if roman_numbers[i] <= roman_numbers[roman_num[counter-1]]:
                result+=result_pause
                result_pause=0
                if roman_numbers[i] >= roman_numbers[roman_num[counter+1]]:
                    result += roman_numbers[i]


            if roman_numbers[i] >= roman_numbers[roman_num[counter-1]]:
                if roman_numbers[i] < roman_numbers[roman_num[counter+1]]:
                    result_pause += roman_numbers[i]

                elif roman_numbers[i] > roman_numbers[roman_num[counter+1]]:
                    if roman_numbers[i] > roman_numbers[roman_num[counter-1]]:
                        if result_pause!=0:
                            result += roman_numbers[i]-result_pause
                        else:
                            result += roman_numbers[i] - roman_numbers[roman_num[counter-1]]

            if roman_numbers[i] > roman_numbers[roman_num[counter-1]]:
                if roman_numbers[i] > roman_numbers[roman_num[counter+1]]:
                    result_pause += roman_numbers[i]-roman_numbers[roman_num[counter-1]]

        elif counter == len(roman_num)-1:
            if roman_numbers[i] > roman_numbers[roman_num[counter-1]]:
                result += roman_numbers[i]-roman_numbers[roman_num[counter-1]]
            elif roman_numbers[i] < roman_numbers[roman_num[counter-1]]:
                if result_pause != 0:
                    result += roman_numbers[i]+result_pause
                else:
                    result += roman_numbers[i]
        counter += 1
    return result
roman_string = input()
print(from_roman(roman_string))