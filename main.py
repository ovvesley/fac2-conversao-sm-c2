import sys


# ----------START UTILITÁRIOS---------------
def get_file():
    path_file = sys.argv[1]
    file = open(path_file, 'r')
    return file
def print_decimal(value, **kwargs):
    string = str(f"{value:,.0f}").replace(",", '.')
    print(string, **kwargs)


def reverse_string(string):
    return string[::-1]


# ----------END UTILITÁRIOS---------------

# ----------START CORE---------------

def binary_to_decimal(binary):
    count = len(binary)
    sum = 0
    binary = reverse_string(binary)

    for index_i in range(count):
        if binary[index_i] == '1':
            sum += 2 ** index_i
    return sum

def binary_to_decimal_sm(binary):
    signal = binary[0]

    binary_without_signal = binary[1:]
    decimal = binary_to_decimal(binary_without_signal)

    if signal == '1':
        return -1 * decimal
    return decimal

def change_signal(binary):
    count = len(binary)
    signal = binary[0]
    binary = reverse_string(binary)

    if signal == '0':
      binary = binary[:count-1] + '1'
    else:
      binary = binary[:count-1] + '0'
  
    binary = reverse_string(binary)
    return binary

def binary_c2(binary):
    signal = binary[0]

    binary_c2_parcial = binary
    if signal == '1':
        binary = binary.replace('1', 'x')
        binary = binary.replace('0', '1')
        binary = binary.replace('x', '0')
        binary_c2_parcial = sum_binaries_sm(binary, '0' * (len(binary) - 1) + '1')
    return binary_c2_parcial, signal

def binary_to_decimal_c2(binary):

    b_c2, signal = binary_c2(binary)
    binary_c2_parcial_without_signal = b_c2[1:]
    decimal = binary_to_decimal(binary_c2_parcial_without_signal)
    if signal == '1':
        return -1 * decimal

    return decimal


def C2(binary): 

            
    return binary



def sum_binaries_sm(binary_1, binary_2):
    count = len(binary_1)
    fit_binary_1 = binary_1
    fit_binary_2 = binary_2
    sum = []
    higher_magnitude = 0
    carry = 0

    for index_i in range(1, count):
        if fit_binary_1[index_i] == "1" and fit_binary_2[index_i] == "0":
            higher_magnitude = 1
            break
        elif fit_binary_1[index_i] == "0" and fit_binary_2[index_i] == "1":
            higher_magnitude = 2
            break

    fit_binary_1 = reverse_string(fit_binary_1)
    fit_binary_2 = reverse_string(fit_binary_2)

    if fit_binary_1[-1] == fit_binary_2[-1]:
        for index_i in range(count - 1):
            if (fit_binary_1[index_i] == "0" and fit_binary_2[index_i] == "0" and carry == 0):
                carry = 0
                sum.append('0')
            elif (fit_binary_1[index_i] == "1" and fit_binary_2[index_i] == "0" and carry == 0) or (fit_binary_1[index_i] == "0" and fit_binary_2[index_i] == "1" and carry == 0) or (
                    fit_binary_1[index_i] == "0" and fit_binary_2[index_i] == "0" and carry == 1):
                carry = 0
                sum.append('1')
            elif (fit_binary_1[index_i] == "1" and fit_binary_2[index_i] == "1" and carry == 0) or (fit_binary_1[index_i] == "0" and fit_binary_2[index_i] == "1" and carry == 1) or (
                    fit_binary_1[index_i] == "1" and fit_binary_2[index_i] == "0" and carry == 1):
                carry = 1
                sum.append('0')
            elif (fit_binary_1[index_i] == "1" and fit_binary_2[index_i] == "1" and carry == 1):
                carry = 1
                sum.append('1')

    else:
        if higher_magnitude == 2:
            fit_binary_1, fit_binary_2 = fit_binary_2, fit_binary_1
        for index_i in range(count - 1):
            if (fit_binary_1[index_i] == "0" and fit_binary_2[index_i] == "0" and carry == 0) or (fit_binary_1[index_i] == "1" and fit_binary_2[index_i] == "1" and carry == 0) or (
                    fit_binary_1[index_i] == "1" and fit_binary_2[index_i] == "0" and carry == 1):
                carry = 0
                sum.append('0')
            elif (fit_binary_1[index_i] == "0" and fit_binary_2[index_i] == "0" and carry == 1) or (fit_binary_1[index_i] == "1" and fit_binary_2[index_i] == "1" and carry == 1) or (
                    fit_binary_1[index_i] == "0" and fit_binary_2[index_i] == "1" and carry == 0):
                carry = 1
                sum.append('1')
            elif (fit_binary_1[index_i] == "1" and fit_binary_2[index_i] == "0" and carry == 0):
                carry = 0
                sum.append('1')
            elif (fit_binary_1[index_i] == "0" and fit_binary_2[index_i] == "1" and carry == 1):
                carry = 1
                sum.append('0')
        fit_binary_1 = reverse_string(binary_1)
        fit_binary_2 = reverse_string(binary_2)

    if (fit_binary_1[-1] == "1" and fit_binary_2[-1] == "1") or (fit_binary_1[-1] == "1" and fit_binary_2[-1] == "0" and higher_magnitude == 1) or (fit_binary_1[-1] == "0" and fit_binary_2[-1] == "1" and higher_magnitude == 2):
        sum.append('1')
    else:
        sum.append('0')

    sum = reverse_string(sum)
    sum = ''.join(sum)
    return (sum)

def sum_binaries_c2(binary_1, binary_2):
    binary_1_c2, _s2 = binary_c2(binary_1)
    binary_2_c2, _s1 = binary_c2(binary_2)
    if _s1 != _s2:
        sum = sum_binaries_sm(binary_1, change_signal(binary_2))
    else:
        sum = sum_binaries_sm(binary_1, binary_2)
    return sum

def subtration_binaries_c2(binary_1, binary_2):
    sum = sum_binaries_sm(binary_1, binary_2)
    return sum


# ----------END CORE---------------

def handle_binary_pair(binary_1, binary_2):
    
    #  SINAL E MAGNITUDE

    decimal_1 = binary_to_decimal_sm(binary_1)
    decimal_2 = binary_to_decimal_sm(binary_2)

    print(decimal_1)
    print(decimal_2, end="\n\n")


    sum_b1_b2 = sum_binaries_sm(binary_1, binary_2)
    subtraction_b1_b2 = sum_binaries_sm(binary_1, change_signal(binary_2))   # b2 * (-1) =>  no caso do SM trocar o bit de sinal
    
    print(sum_b1_b2)
    print(subtraction_b1_b2, end="\n\n")

    decimal_sum = binary_to_decimal_sm(sum_b1_b2)
    decimal_subtraction = binary_to_decimal_sm(subtraction_b1_b2)

    print(decimal_sum)
    print(decimal_subtraction, end="\n\n")

    # COMPLEMENTO A DOIS
    binary_1_c2 = binary_to_decimal_c2(binary_1)
    binary_2_c2 = binary_to_decimal_c2(binary_2)

    print_decimal(binary_1_c2)
    print(binary_2_c2, end="\n\n")

    # -----

    sum_b1_b2_binary = sum_binaries_c2(binary_1, binary_2)
    sum_b1_b2_decimal = binary_to_decimal_c2(sum_b1_b2_binary)

    subtraction_b1_b2_binary = subtration_binaries_c2(binary_1, binary_2)   # b2 * (-1)
    subtraction_b1_b2_decimal = binary_to_decimal_c2(subtraction_b1_b2_binary)  # b2 * (-1)

    print(sum_b1_b2_binary)
    print(subtraction_b1_b2_binary, end="\n\n")

    print_decimal(sum_b1_b2_decimal)
    print_decimal(subtraction_b1_b2_decimal, end="\n\n")



    

def main():
    file = get_file()

    while True:
        binary_1 = file.readline().strip()
        binary_2 = file.readline().strip()

        if not binary_1 or not binary_2:
            break

        handle_binary_pair(binary_1, binary_2)

    file.close()


main()
