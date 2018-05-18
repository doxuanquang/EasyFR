import re

def check_mask(mask):
    if mask.isdigit() and 0 <= int(mask) <= 32:
            return mask
    else:
        return long_mask(mask)

def long_mask(mask):
    mask = mask.split(".")
    # print(mask)
    binary_mask = ""
    for octet in mask:
        if octet.isdigit():
            octet = int(octet)
            if octet == 0:
                binary_mask += "00000000"
                continue
            if 0 < octet <= 255:
                octet = bin(octet)
                # print(octet)
                octet = octet[2:10]
                # print(octet)
                binary_mask += octet
            else:
                print("Octet must be between 0 and 255")
                break
        else:
            print("Octet must be a number")
            break

    if len(binary_mask) != 32:
        print("You provided a bad mask")
        return False
    elif re.search("01", binary_mask) is not None:
        print("You provided an invalid mask")
        return False
    else:
        return binary_mask.count("1")


