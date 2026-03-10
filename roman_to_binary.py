import math


ROMAN_VALUES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_decimal(roman: str) -> int:
    """Converte un numero romano in decimale."""
    roman = roman.upper().strip()
    result = 0
    prev = 0

    for char in reversed(roman):
        if char not in ROMAN_VALUES:
            raise ValueError(f"Carattere non valido nel numero romano: '{char}'")
        value = ROMAN_VALUES[char]
        if value < prev:
            result -= value
        else:
            result += value
        prev = value

    return result


def decimal_to_binary(n: int) -> str:
    """Converte un intero positivo in binario usando la libreria math."""
    if n == 0:
        return '0'

    num_bits = math.floor(math.log2(n)) + 1
    binary_digits = []

    for i in range(num_bits - 1, -1, -1):
        bit = math.floor(n / math.pow(2, i)) % 2
        binary_digits.append(str(int(bit)))

    return ''.join(binary_digits)


def roman_to_binary(roman: str) -> str:
    """Converte un numero romano in binario."""
    decimal = roman_to_decimal(roman)
    binary = decimal_to_binary(decimal)
    return binary


if __name__ == "__main__":
    test_cases = [
        "I",       # 1   -> 1
        "IV",      # 4   -> 100
        "IX",      # 9   -> 1001
        "XIV",     # 14  -> 1110
        "XLII",    # 42  -> 101010
        "XCIX",    # 99  -> 1100011
        "CDXLIV",  # 444 -> 110111100
        "MCMXCIX", # 1999 -> 11111001111
        "MMXXVI",  # 2026 -> 11111101010
    ]

    print(f"{'Romano':<12} {'Decimale':<10} {'Binario'}")
    print("-" * 35)
    for roman in test_cases:
        decimal = roman_to_decimal(roman)
        binary = roman_to_binary(roman)
        print(f"{roman:<12} {decimal:<10} {binary}")
