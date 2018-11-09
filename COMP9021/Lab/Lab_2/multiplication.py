# Decodes all multiplications of the form
#
#                        *  *  *
#                   x       *  *
#                     ----------
#                     *  *  *  *
#                     *  *  *
#                     ----------
#                     *  *  *  *
#
# such that the sum of all digits in all 4 columns is constant.


# Insert your code here.

for x in range(100, 1_000):
    for y in range(10, 100):
        # Replace pass above with your code.
        # Compute the first partial product product0, namely, x * (y % 10),
        # and make sure it is at least equal to 1000.
        # Compute the second partial product product1 and make sure it is smaller than 1000.
        # Perform all other necessary tests...
        col = [0, 0, 0, 0]
        mid1 = x * (y % 10)
        if mid1 < 1000:
            continue
        mid2 = x * (y // 10)
        if mid2 >= 1000:
            continue
        result = x * y
        if result >= 10000:
            continue
        col[0] = mid1 // 1000 + mid2 // 100 + result // 1000
        col[1] = x // 100 + (mid1 // 100) % 10 + (mid2 // 10) % 10 \
                 + (result // 100) % 10
        col[2] = (x // 10) % 10 + y // 10 + (mid1 // 10) % 10 + \
                 mid2 % 10 + (result // 10) % 10
        col[3] = x % 10 + y % 10 + mid1 % 10 + result % 10
        set_col = set(col)
        if len(set_col) == 1:
            print(f'{x} * {y} = {result}, all columns adding up to {col[0]}.')
