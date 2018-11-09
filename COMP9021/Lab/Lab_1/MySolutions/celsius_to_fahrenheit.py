# Written by Jingyun Shen for COMP9021 Lab_1

"""
This program plays a conversion table from Celsius
degrees to Fahrenheit degrees, with the former ranging
from 0 to 100 in steps of 10.
"""

def main():
    min_temperature = 0
    max_temperature = 100
    step = 10
    print('Celsius\tFahrenheit')

    for celsius in range(min_temperature, max_temperature + step, step):
        fahrenheit = 9 * celsius / 5 + 32
        print(f'{celsius:7}\t{fahrenheit:10.1f}')

    return 0

if __name__ == '__main__':
    main()
