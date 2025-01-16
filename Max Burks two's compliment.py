dec_num = int(input("please enter a decimal integer less than 128 and greater than or equal to -128: "))
twos_comp = ''
if dec_num > 127 or dec_num < -128:
    exit('ERROR, INVALID NUMBER')
for num_pow in range(7,-1,-1):
    if dec_num > (2 ** num_pow) -1:
        twos_comp += '1'
        dec_num -= 2**num_pow
    elif dec_num < 0:
        twos_comp = '1'
        dec_num = (2**num_pow+dec_num)
    else:
        twos_comp += '0'
print(twos_comp)