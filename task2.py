def div_ide(string):
    l = len(string) // 2
    first_half = string[:l]
    second_half = string[l:]
    return [first_half, second_half]

def trever(string):
    reversed = string[::-1]
    return reversed


def encoder(string):
    l = len(string) // 2
    encoded_string = []

    if l > 1:
        divided_string = div_ide(string)
        for half in divided_string:
            encoded_string += encoder(trever(half))
    else:
        return string

    return encoded_string


encoded_flag = '4mcr3_bllwma{san1nth!}gsl_4l3_th'
flag = ''.join(encoder(encoded_flag))
print(flag)
