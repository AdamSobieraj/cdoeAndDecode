def GGGGotate(lol):
    bit = lol << 1
    movebit = bit & 255
    if (lol > 127 ):
        movebit = movebit | 1
    return (movebit)



def main():
    value = input("Enter your value: ")
    ListMoveBit = []
    Index_Value = 0
    ORD_value = []
    ORD_key = []
    Final_encrypted = ""

    # rev 1
    for i in value:
        ORD_value.append(ord(i))
    # rev 1 end

    a = ord("a")
    ORD_key.append(a)

    # rev 2
    lol = int(ORD_key[0]) ^ int(ORD_value[0])
    ListMoveBit.append(GGGGotate(lol))
    # rev 2 end

    # rev 3
    for chars in ORD_value:
        if Index_Value == 0:
            Index_Value += 1
            pass
        else:
            lol = int(ListMoveBit[Index_Value-1]) ^ int(chars)
            ListMoveBit.append(GGGGotate(lol))
            Index_Value += 1
    # rev 3 end

    # rev 10 end
    for i in ListMoveBit:
        x = hex(i)
        val = x[2:]
        if(i > 9) and (i < 16):
            Final_encrypted = Final_encrypted + "0" + val
        else:
            if (i<10):
                Final_encrypted = Final_encrypted +"0"+val
            else:
                Final_encrypted = Final_encrypted + val

    # rev 10 end


    print("\nThe encrypted message is:")
    print(Final_encrypted + "\n")
if __name__ == '__main__':
    main()

# 703e966d1ed86f08daf503d6678e99eb09d47f18