import sys


# ----------START UTILITÁRIOS---------------
def get_file():
    path_file = sys.argv[1]
    file = open(path_file, 'r')
    return file


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


# ----------END CORE---------------

def handle_binary_pair(binary_1, binary_2):
    decimal_1 = binary_to_decimal_sm(binary_1)
    decimal_2 = binary_to_decimal_sm(binary_2)

    print(decimal_1)
    print(decimal_2)

    sum_b1_b2 = sum_binaries_sm(binary_1, binary_2)
    
    print(sum_b1_b2)

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
