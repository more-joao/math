def euclid_divide(number, divisor): # acelerar o algoritmo
    quotient = 0
    remainder = number
    print(f'{number} = {quotient} * {divisor} + {remainder}')
    while remainder < 0 or remainder >= divisor:
        remainder = remainder-divisor if number > 0 else remainder+divisor
        quotient = quotient+1 if number > 0 else quotient-1
        print(f'{number} = {quotient} * {divisor} + {remainder}')
    return quotient, remainder


def to_decimal(number, actual_base):
    this_quotient = int(str(number)[0])
    print(f'{this_quotient} = 3 * 0 + {this_quotient}')
    for x in str(number)[1:]:
        print(f'{actual_base*this_quotient+int(x)} = {actual_base} * {this_quotient} + {x}')
        this_quotient = actual_base*this_quotient+int(x)
    return this_quotient


def to_given_base(number, actual_base, target_base):
    if actual_base != 10:
        number = to_decimal(number, actual_base)
    
    q, r = euclid_divide(number, target_base)
    converted_number = [r]
    while q != 0:
        q, r = euclid_divide(q, target_base)
        converted_number.insert(0,r)
    
    print(converted_number)

n = 29182281
to_given_base(n, 10, 3)

