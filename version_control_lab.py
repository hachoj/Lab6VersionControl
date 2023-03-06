def encoder(data):
    data_list = list(data)
    return_data_list = []
    for num in data_list:
        num = int(num)
        num += 3
        if num > 9:
            num -= 10
        return_data_list.append(str(num))
    return ''.join(return_data_list)


def main():
    pass


if __name__ == '__main__':
    main()
