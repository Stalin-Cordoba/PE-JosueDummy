import sys

def main():
    
    sys.set_int_max_str_digits(3000000)
    
    base = 28433
    base *= (2 ** 7830457)
    base += 1
    print(base)

main()