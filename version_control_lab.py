# Harrison Chojnowski's encoder function
def encoder(data):
    encoded_data = ''
    for num in data:
        num = int(num)
        num += 3
        if num > 9:
            num -= 10
        encoded_data += str(num)
    return encoded_data


# Cyrus Smeltzer' Code
def decoder(encoded_password):
    decoded_password = ''
    for num in encoded_password:
        new_num = int(num) - 3
        if new_num < 0:
            new_num += 10
        decoded_password += str(new_num)
    return decoded_password


def main():
    playing = True
    while playing:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        choice = input('Please enter an option: ')
        encoded_password = ''
        if choice == '1':
            user_input = input('Please enter your password to encode: ')
            encoded_password = encoder(user_input)
            print('Your password has been encoded and stored!\n')
        elif choice == '2':
            print(f'The encoded passwrod is {encoded_password}, and the original password is {decoder(encoded_password)}.\n')
        elif choice == '3':
            playing = False

if __name__ == '__main__':
    main()
