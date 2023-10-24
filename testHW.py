def test(num):
    '''
    Purpose:
      Overwrites the top half of an image with the bottom, and vice versa.
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions, with the top and bottom halves
      swapped.
    '''
    half_length = num // 2
    mod_length = num % 2
    for row_num in range(0, half_length):
        print(row_num)
    for row_num in range(half_length + mod_length, num):
        print(row_num)


test(3)
