def end_zeros(num: int) -> int:
    #You can reverse a string in python using a backwards slice [::-1]
    temp_string = str(num)[::-1]
    noughts = 0
    for i in temp_string:
        if i == "0":
            noughts+=1
        else:
            break
    return noughts




if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))
    print(end_zeros(100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
