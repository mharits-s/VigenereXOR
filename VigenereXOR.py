def text_to_bits(text):
    # Convert text to binary representation
    bits = ''.join(format(ord(char), '08b') for char in text)
    return bits

def bits_to_text(bits):
    # Convert binary representation to text
    text = ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))
    return text

def separate_bits(bits):
    # Separate bits into groups of 8
    return ' '.join([bits[i:i+8] for i in range(0, len(bits), 8)])

def vigenere_cipher(input_data, key, mode):
    if mode == 'text':
        input_bits = text_to_bits(input_data)
        key_bits = text_to_bits(key)
    elif mode == 'bits':
        input_bits = input_data
        key_bits = text_to_bits(key)

    # Ensure the key is repeated to match the length of the input
    key_bits = (key_bits * (len(input_bits) // len(key_bits) + 1))[:len(input_bits)]

    result_bits = ""
    for i in range(len(input_bits)):
        result_bits += str(int(input_bits[i]) ^ int(key_bits[i]))

    # Convert the binary result back to text
    result_text = bits_to_text(result_bits)

    return input_bits, key_bits, result_bits, result_text

def is_valid_text_input(text_input):
    return len(text_input) >= 6

def is_valid_bit_input(bit_input):
    return all(bit == '0' or bit == '1' for bit in bit_input)

if __name__ == "__main__":
    print("Menu:")
    print("1. Input karakter")
    print("2. Input bit")
    print("3. Keluar")
    choice = input("Input Angka sesuai menu: ")

    if choice == '1':
        while True:
            plaintext = input("Masukkan plaintext (lebih dari 5 karakter): ")
            key = input("Masukkan kunci (lebih dari 5 karakter): ")
            if len(plaintext) >= 6 and len(key) >= 6:
                key_bits = text_to_bits(key)
                break
            else:
                print("Panjang plaintext atau kunci kurang dari 6 karakter. Silakan coba lagi.")
        mode = 'text'
        output_filename = "output1.txt"
    elif choice == '2':
        while True:
            plaintext_bits = input("Masukkan plaintext bits: ")
            key = input("Masukkan key text: ")
            if is_valid_text_input(key) and is_valid_bit_input(plaintext_bits):
                key_bits = text_to_bits(key)
                break
            else:
                print("Panjang key kurang dari 6 karakter atau plaintext bits tidak valid. Silakan coba lagi.")
        mode = 'bits'
        output_filename = "output2.txt"
    elif choice == '3':
        print("Keluar dari program")
        exit()
    else:
        print("Pilihan tidak valid. Keluar program.")
        exit()

    if mode == 'text':
            # Enkripsi
        input_bits, key_bits, result_bits, result_text = vigenere_cipher(
            plaintext if mode == 'text' else plaintext_bits,
            key if mode == 'text' else key_bits,
            'text'
        )

        print(f"\nBit Pesan: {separate_bits(input_bits)}")
        print(f"Bit Kunci: {separate_bits(key_bits)}")
        print(f"Bit Output: {separate_bits(result_bits)}")
        print(f"Karakter Output: {result_text}")

        with open(output_filename, "w") as output_file:
            output_file.write(f"Plaintext: {plaintext}\n")
            output_file.write(f"Key text: {key}\n")
            output_file.write(f"Bit Pesan: {separate_bits(input_bits)}\n")
            output_file.write(f"Bit Kunci:2 {separate_bits(key_bits)}\n")
            output_file.write(f"Bit Output: {result_bits}\n")
            output_file.write(f"Karakter Output: {result_text}\n")

            print(f"Hasil Output telah didokumentasikan dalam file {output_filename}")

    if mode == 'bits':
        decrypted_bits = ""
        for i in range(len(plaintext_bits)):
            decrypted_bits += str(int(plaintext_bits[i]) ^ int(key_bits[i % len(key_bits)]))

        # Convert the binary result back to text
        decrypted_text = bits_to_text(decrypted_bits)

        print(f"\nBit Pesan: {separate_bits(plaintext_bits)}")
        print(f"Key text: {key}")
        print(f"Bit Output: {separate_bits(decrypted_bits)}")
        print(f"Karakter Output: {decrypted_text}")

        with open(output_filename, "w") as output_file:
            output_file.write(f"Plaintext Bit: {separate_bits(plaintext_bits)}\n")
            output_file.write(f"Key text: {key}\n")
            output_file.write(f"Bit Output: {separate_bits(decrypted_bits)}\n")
            output_file.write(f"Karakter Output (Dekripsi): {decrypted_text}\n")

            print(f"Hasil Dekripsi telah didokumentasikan dalam file {output_filename}")