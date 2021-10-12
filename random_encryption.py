from random import randint

choice = input("would you like the encryptor or decryptor: ")

if choice == "e" or choice == "encryptor":
    '''ENCRYPTOR'''
    print(" welcome to the encryptor!\n what message would you like to encrypt:\n type: ? to finish")
    offset = randint(1, 100)
    line_arr = []
    while True:
        for sen in list(input().rstrip()):
            line_arr.append(sen)
        if line_arr[-1] == "?":
            del line_arr[-1]
            break
        line_arr.append("\n")
    for lines in line_arr:
        print(hex(ord(lines) + offset)[2:], end = '')
    print(hex(offset)[2:])

else:
    '''DECRYPTOR'''
    print(" welcome to the decryptor!")
    print(" what message would you like to decrypt: ", end = '\n ')
    dec = input().rstrip()
    dec_offset = int(dec[-2:], 16)
    for j in range(0, len(dec), 2):
        print(chr(int(dec[j:j+2], 16) - dec_offset), end = '')
