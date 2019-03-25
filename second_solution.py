# second_solution.py

"""

Working from left-to-right, if no digit is exceeded by the digit to its left, it is called an increasing number. For example: 134468. Similarly, if no digit is exceeded by the digit to its right, it is called a decreasing number. For example: 66420. We shall call a positive integer that is neither increasing nor decreasing a "bouncy number". For example: 155349. Clearly, there cannot be any "bouncy numbers" below one-hundred, but just over half of the numbers below one-thousand (525) are "bouncy". In fact, the least number for which the proportion of "bouncy numbers" first reaches 50% is 538. Surprisingly, "bouncy numbers" become more and more common and by, the time we reach 21780, the proportion of "bouncy numbers" is equal to 90%. Find the least number for which the proportion of "bouncy numbers" is exactly 99%.

"""


def bouncy_number(number):

    increasing_sequence = False
    decreasing_sequence = False

    right_digit = number % 10
    number = number // 10

    while number > 0:
        left_digit = number % 10

        if left_digit < right_digit:
            increasing_sequence = True
        elif left_digit > right_digit:
            decreasing_sequence = True

        right_digit = left_digit
        number = number // 10

        if increasing_sequence and decreasing_sequence:
            return True

    return False


count = 0
i = 99

while count < 0.99 * i:
    i += 1

    if bouncy_number(i):
        count += 1

print(i)
