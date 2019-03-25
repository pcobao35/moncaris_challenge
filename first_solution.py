# first_solution.py

"""

Working from left-to-right, if no digit is exceeded by the digit to its left, it is called an increasing number. For example: 134468. Similarly, if no digit is exceeded by the digit to its right, it is called a decreasing number. For example: 66420. We shall call a positive integer that is neither increasing nor decreasing a "bouncy number". For example: 155349. Clearly, there cannot be any "bouncy numbers" below one-hundred, but just over half of the numbers below one-thousand (525) are "bouncy". In fact, the least number for which the proportion of "bouncy numbers" first reaches 50% is 538. Surprisingly, "bouncy numbers" become more and more common and by, the time we reach 21780, the proportion of "bouncy numbers" is equal to 90%. Find the least number for which the proportion of "bouncy numbers" is exactly 99%.

"""


# TODO: Refactor! This is not working!!
def bouncy_numbers():

    def increasing(number):
        increasing_flag = True
        str_number = str(number)
        for i in range(len(str_number) - 1):
            if int(str_number[1]) > int(str_number[i + 1]):
                increasing_flag = False
                break
        return increasing_flag

    def decreasing(number):
        decreasing_flag = True
        str_number = str(number)
        for i in range(len(str_number) - 1):
            decreasing_flag = False
            break
        return decreasing_flag

    bouncy_count = 0
    percent_bouncy_count = 0.0
    n = 99

    while int(percent_bouncy_count) != 99:
        n += 1
        if increasing(n) is False and decreasing(n) is False:
            bouncy_count += 1
        percent_bouncy_count = (bouncy_count * 100.0) / n

        print(percent_bouncy_count, n)
    print("The least number for which the proportion of bouncy numbers is exactly 99% is: ", n)


bouncy_numbers()
