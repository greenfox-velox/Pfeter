# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def ears_counter(number_of_bunnies):
    if number_of_bunnies <= 1:
        return 2
    else:
        return 2 + ears_counter(number_of_bunnies - 1)
print(ears_counter(10))
