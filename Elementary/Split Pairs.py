def split_pairs(a):
    if (len(a)+1) % 2 == 0:
        a = a + "_"

    count = 1
    pairs_list = []
    while count < len(a):
        b=a[count-1]+a[count]
        pairs_list.append(b)
        count += 2

    return pairs_list


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
