ab = 123
credits = 220
is_bonus = True
# if credits are at least 50,
# and is_bonus is False decrement ab by 2
# if credits are smaller than 50,
# and is_bonus is False decrement ab by 1
# if is_bonus is True ab should remain the same
if credits > 50 and not is_bonus:
    ab -= 2
elif credits < 50 and not is_bonus:
    ab -= 1
elif is_bonus:
    ab = ab
print(ab)
