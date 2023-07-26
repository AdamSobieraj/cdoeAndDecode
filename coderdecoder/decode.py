def convert_ascii_to_string(ascii_list):
    return ''.join(chr(ascii_val) for ascii_val in ascii_list)


def reverse_hex_to_list(hex_string):
    hex_pairs = [hex_string[i:i + 2] for i in range(0, len(hex_string), 2)]
    decrypted_list = [int(pair, 16) for pair in hex_pairs]
    return decrypted_list


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

    return ORD_value


def main():
    value = input("Enter your value to decode: ")

    # rev 10
    ListMoveBit = reverse_hex_to_list(value)
    # rev 10 end

    # rev 3
    recovered_ORD_value = reverse_code(ListMoveBit.copy())
    ORD_value = recovered_ORD_value
    # rev 3 end

    # rev 1
    decoded_message = convert_ascii_to_string(ORD_value)
    # rev 1 end

    print("\nThe decoded message is:")
    print(decoded_message + "\n")


if __name__ == '__main__':
    main()
