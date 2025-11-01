def decimal_to_binary(n):
    if n == 0:
        return '0'
    result = ''
    while True:
        a = n%2
        b = n//2
    
        n = b
        if b == 1:
            a = str(a)
            result = str(b) + a + result
            break
        a = str(a)
        result = a + result
    
    return result


def binary_to_decimal(binary_str):
    new_order_for_calculation = ''
    for i in binary_str:
        new_order_for_calculation = i + new_order_for_calculation
    
    order = 0
    total = 0

    for i in new_order_for_calculation:
        i = int(i)
        total += i * pow(2, order)
        order += 1

    return total


def decimal_to_hex_digit(n):
    check = 1
    if n == 0:
        return '0'
    result = ''
    while n > 0:
       if n // 16 < 1:
           if n == 15:
               result = "F" + result
           elif n == 14:
               result = "E" + result
           elif n == 13:
               result = "D" + result
           elif n == 12:
               result = "C" + result
           elif n == 11:
               result = "B" + result
           elif n == 10:
               result = "A" + result
           else:
               result = str(n) + result

       elif n // 16 >= 1:
           if n % 16 == 15:
               result = "F" + result
           elif n % 16 == 14:
               result = "E" + result
           elif n % 16 == 13:
               result = "D" + result
           elif n % 16 == 12:
               result = "C" + result
           elif n % 16 == 11:
               result = "B" + result
           elif n % 16 == 10:
               result = "A" + result
           else:
               result = str(n % 16) + result

       n = n // 16       
       if check == 3:
           break

       if n // 16 < 16:
           check += 1
        
    return result
    
    
def is_valid_binary(binary_str):
    j = 0
    for i in binary_str:
        if i == '0' or i == '1':
            j += 0
        else:
            j += 1
        
    if j == 0:
        return True
    else:
        return False


def count_ones_in_binary(binary_str):
    count = 0
    for i in binary_str:
        if i == '1':
            count += 1

    return count

print("\n\nNumber System Converter\n"
"----------------------------------------")

n = 25
binary = decimal_to_binary(n)
print(f"Decimal {n} to binary: {binary}")

binary = '11011'
decimal = binary_to_decimal(binary)
print(f"Binary {binary} to decimal: {decimal}\n")

n = '1010'
print(f"Is '{n}' valid binary? {is_valid_binary(n)}")
n = '1012'
print(f"Is '{n}' valid binary? {is_valid_binary(n)}")
n = '1111'
print(f"Is '{n}' valid binary? {is_valid_binary(n)}\n")

n = '110101'
number_of_ones = count_ones_in_binary(n)
print(f"Number of 1s in '{n}': {number_of_ones}\n")

n = 9
hexa = decimal_to_hex_digit(n)
print(f"Decimal {n} to hex: {hexa}")
n = 10
hexa = decimal_to_hex_digit(n)
print(f"Decimal {n} to hex: {hexa}")
n = 15
hexa = decimal_to_hex_digit(n)
print(f"Decimal {n} to hex: {hexa}\n\n")




    
 