def get_binary_nmumber(decimal_number):
    print(isinstance(decimal_number,int))
    assert isinstance(decimal_number,int)
    return bin(decimal_number)
print(get_binary_nmumber(10))
print(get_binary_nmumber('10'))