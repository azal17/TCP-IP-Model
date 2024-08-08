

import numpy as np

def generate_hamming_code():
    n = 4  

    data_word = np.empty(n, dtype=int)
    for i in range(n):
        element = int(input(f"Enter element {i + 1} (4 bits): "))
        data_word[i] = element

    print("NumPy Array Dataword:", data_word)

   
    code_word = np.zeros(7, dtype=int)  
    code_word[:4] = data_word  


    p1 = code_word[0] ^ code_word[2] ^ code_word[4]  # p1: 1, 3, 5, 7 (0, 2, 4, 6 in code_word)
    p2 = code_word[0] ^ code_word[1] ^ code_word[4]  # p2: 2, 3, 6, 7 (1, 2, 4, 5 in code_word)
    p4 = code_word[0] ^ code_word[1] ^ code_word[2]  # p4: 4, 5, 6, 7 (0, 1, 2, 3 in code_word)


    code_word[3] = p4
    code_word[5] = p2
    code_word[6] = p1

    print("NumPy Array Codeword with Hamming Code:", code_word)
    return code_word

def binary_division(dataword, divisor):
    dataword_int = int("".join(map(str, dataword)), 2)
    divisor_int = int("".join(map(str, divisor)), 2)

    while dataword_int >= divisor_int:
        shift = len(bin(dataword_int)) - len(bin(divisor_int))
        dataword_int ^= (divisor_int << shift)

    remainder_bin = bin(dataword_int)[2:]
    remainder = np.array([int(bit) for bit in remainder_bin])
    return remainder

def generate_crc_code():
    choice = input("Choose an option: 1) Bits, 2) Polynomial: ")

    if choice == "1": 
        n = int(input("Enter the number of bits for dataword: "))
        dataword = np.empty(n, dtype=int)
        for i in range(n):
            element = int(input(f"Enter the {i + 1}st bit: "))
            dataword[i] = element

        print("Entered dataword:", dataword)

        m = int(input("Enter the number of bits for divisor: "))
        divisor = np.empty(m, dtype=int)
        for i in range(m):
            element = int(input(f"Enter the {i + 1}st bit: "))
            divisor[i] = element

        print("Entered divisor:", divisor)

        syndrome_length = m - 1 
        augmented_dataword = np.concatenate((dataword, np.zeros(syndrome_length, dtype=int)))  # Concatenate dataword with zeros for syndrome
        remainder = binary_division(augmented_dataword, divisor)
        print("Remainder:", remainder)

        codeword = np.concatenate((dataword, remainder))
        print("Codeword:", codeword)

    elif choice == "2": 
        n = int(input("Enter the degree of polynomial dataword: ")) + 1
        dataword = np.empty(n, dtype=int)
        for i in range(n):
            element = int(input(f"Enter the coefficient of x^{n - i - 1}: "))
            dataword[i] = element

        print("Entered dataword: ", dataword)

        m = int(input("Enter the degree of generator polynomial : ")) + 1
        divisor = np.empty(m, dtype=int)
        for i in range(m):
            element = int(input(f"Enter the coefficient of x^{m - i - 1}: "))
            divisor[i] = element

        print("Entered divisor: ", divisor)

        syndrome_length = m - 1  
        augmented_dataword = np.concatenate((dataword, np.zeros(syndrome_length, dtype=int)))  # Concatenate dataword with zeros for syndrome
        remainder = binary_division(augmented_dataword, divisor)
        print("Remainder:", remainder)

        codeword = np.concatenate((augmented_dataword, remainder))
        print("Codeword:", codeword)

    else:
        print("Invalid option. Please choose either '1' or '2'.")
        return None

    return codeword

if __name__ == "__main__":
    print("Select an option:")
    print("1. Generate 7-bit Hamming Code")
    print("2. Generate CRC Code")
    option = input("Enter your choice (1 or 2): ")

    if option == "1":
        generate_hamming_code()
    elif option == "2":
        generate_crc_code()
    else:
        print("Invalid choice. Please enter '1' or '2'.")
