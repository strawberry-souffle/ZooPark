def rangeBitwiseAnd(left: int, right: int) -> int:
    output = 0
    for i in reversed(range(32)):
        if left>>i == right>>i:
            if left>>i & 1:
                output += 2**i
        else:
            break
    return output

# Smarter works because 'shift' right bits from are different, once we figure out that number we can shift-right the numbers by it,
# and then shift-left(0 to 'shift'th bits will become zero). Thus leaving us with only those which are similar.
def rangeBitwiseAnd_alt(left: int, right: int) -> int:

    # Initialize a variable 'shift' to 0.
    shift = 0

    # While the left and right limits are not equal,
    while left < right:
        # Right shift the left limit by 1 bit.
        left >>= 1

        # Right shift the right limit by 1 bit.
        right >>= 1

        # Increment the 'shift' variable by 1.
        shift += 1

    # Left shift the left limit by 'shift' bits and return the result.
    return left << shift

print(rangeBitwiseAnd(1,2147483647))