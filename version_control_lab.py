def encoder(data):
    data_list = []
    data_list = data[:0]
    return_data_list = []
    for num in data_list:
        num += 3
        if num > 9:
            num -= 10
        return_data_list.append(num)
    return ''.join(return_data_list)


def main():
    pass


if __name__ == '__main__':
    main()
