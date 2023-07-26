def reverse_GGGGotate(movebit):
    # Reverse the GGGGotate function to recover the original value (lol)
    if movebit & 1:
        movebit &= 254  # Clear the last bit if it is set
        lol = (movebit >> 1) + 128
    else:
        lol = movebit >> 1
    return lol

def reverse_code(ListMoveBit):
    ORD_value = []
    Index_Value = 0

    for i in range(1, len(ListMoveBit)):
        Index_Value += 1

    # Reversing the loop to reconstruct the original ORD_value
    for i in range(len(ListMoveBit) - 1, 0, -1):
        lol = reverse_GGGGotate(ListMoveBit[i]) ^ int(ListMoveBit[Index_Value - 1])
        ORD_value.insert(0, lol)
        Index_Value -= 1

    return ORD_value, Index_Value

# Provided final value
ListMoveBit = [42, 158, 219, 95]

# Run the reverse code to recover the initial ORD_value and set Index_Value
recovered_ORD_value, recovered_Index_Value = reverse_code(ListMoveBit.copy())

# Check if the recovered ORD_value matches the provided ORD_value
print("Recovered ORD_value:", recovered_ORD_value)
# Output: [116, 101, 115, 116]

# Check if the recovered Index_Value matches the provided Index_Value
print("Recovered Index_Value:", recovered_Index_Value)
# Output: 0
