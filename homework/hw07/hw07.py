import copy

#If you're not sure how to start, look at the swap_red_blue example below.

#Problem A: Grayscale
def grayscale(img_matrix):
    '''
    Purpose:
      Creates a grayscale version of an image matrix.
    Parameter(s):
      A 3D matrix (list of lists of lists) representing an .bmp image
      Each element of the matrix represents one row of pixels in the image
      Each element of a row represents a single pixel in the image
      Each pixel is represented by a list of three numbers between 0 and 255
      in the order [red, green, blue]
    Return Value:
      A 3D matrix of the same dimensions, with each pixel set to grayscale
      (that is, each color component set to the average of the three in
      the original pixel, rounded down to the nearest integer)
    '''
    for row in img_matrix:
        for ele in row:
            avg_color = int((ele[0] + ele[1] + ele[2]) / 3)
            ele[0] = avg_color
            ele[1] = avg_color
            ele[2] = avg_color
    return img_matrix


#Problem B: Adding Column Index
def add_col(img_matrix):
    '''
    Purpose:
      Adds the column index to each component of each pixel, mod 256.
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions, but with each component of every
      pixel set to the original value plus the column index, % 256.
    '''
    length1 = len(img_matrix)
    length2 = len(img_matrix[0])
    for row in range(0, length1):
        for col in range(0, length2):
            img_matrix[row][col][0] = (img_matrix[row][col][0] + col) % 256
            img_matrix[row][col][1] = (img_matrix[row][col][1] + col) % 256
            img_matrix[row][col][2] = (img_matrix[row][col][2] + col) % 256
    return img_matrix

#Problem C: Swap Top and Bottom
def swap(img_matrix):
    '''
    Purpose:
      Overwrites the top half of an image with the bottom, and vice versa.
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions, with the top and bottom halves
      swapped.
    '''
    half_length = len(img_matrix) // 2
    mod_length = len(img_matrix) % 2
    img_matrix_copy = copy.deepcopy(img_matrix)
    for rowNum in range(0, half_length):
        img_matrix[row] = img_matrix_copy[half_length + mod_length + rowNum]
    for rowNum in range(half_length + mod_length, len(img_matrix)):
        img_matrix[row] = img_matrix_copy[rowNum - half_length]
    return img_matrix

#Problem D: Your Own Filter
def custom_filter(img_matrix):
    '''
    Purpose:
      Inverts the color of an image
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions as img_matrix,
      with changes as described in the purpose section.
    '''
    for row in img_matrix:
        for pixel in row:
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
    return img_matrix


#Example #1: Swapping red and blue components
def swap_red_blue(img_matrix):
    '''
    Purpose:
      Swaps the red and blue components in an image
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions, with red and blue values swapped
      (that is, for every pixel list, the first and last values have been
      swapped).
    '''
    height = len(img_matrix)  #Height = # of rows, i.e. length of matrix
    width = len(img_matrix[0]) #Width = # of columns, i.e. length of one row
    for y in range(height):
        for x in range(width):
            # img_matrix[y][x] is a 3-element list representing the
            # [red, green, blue] values for the pixel at coordinates (x, y)
            old_red = img_matrix[y][x][0]
            old_blue = img_matrix[y][x][2]
            img_matrix[y][x][0] = old_blue
            img_matrix[y][x][2] = old_red
    return img_matrix


#Example #2: Blur the image
#(this is a little more complex than the ones you need to do)
def blur(img_matrix):
    '''
    Purpose:
      Blurs an image by applying a 3x3 pixel filter
    Parameter(s):
      (see grayscale)
    Return Value:
      A 3D matrix of the same dimensions, with each pixel blurred:
      each color component is averaged with the surrounding 9 pixels
    '''
    height = len(img_matrix)
    width = len(img_matrix[0])
    #Make a deep copy of the matrix to use as our output matrix.
    #This is just a convenient way to get an output matrix of the same
    #dimensions as the original.
    new_matrix = copy.deepcopy(img_matrix)

    #Loops through every pixel we need to compute via (x, y) coordinates
    for y in range(height):
        for x in range(width):

            #To compute each pixel, for each of the three color components
            #take the average of that component for the surrounding 9 pixels
            new_pixel = [0, 0, 0]
            for j in range(-1,2):  #Loop through y-1, y, y+1
                for i in range(-1,2):  #Loop through x-1, x, x+1
                    for color in range(3):
                        #If x+i or y+j is out of bounds, ignore it
                        if 0 <= x+i < width and 0 <= y+j < height:
                            new_pixel[color] += img_matrix[y+j][x+i][color]/9

            #Averaging might result in a float, so truncate down to nearest int
            for color in range(3):
                new_pixel[color] = int(new_pixel[color])

            #Replace pixel in output matrix
            new_matrix[y][x] = new_pixel
    return new_matrix



#--------------------------------------------------
# DO NOT EDIT ANYTHING BELOW THIS LINE
# .bmp file manipulation functions.  You don't have to understand these.
#--------------------------------------------------

def big_end_to_int(ls):
    '''
    Byte conversion helper 
    Purpose:
      Compute the integer represented by a sequence of bytes
    Input Parameter(s):
      A list of bytes (integers between 0 and 255), in big-endian order
    Return Value:
      Integer value that the bytes represent
    '''
    total = 0
    for ele in ls[::-1]:
        total *= 256
        total += ele
    return total

def transform_image(fname, operation):
    '''
    .bmp conversion function
    Purpose:
      Turns a .bmp file into a matrix of pixel values, performs an operation
      on it, and then converts it back into a new .bmp file
    Input Parameter(s):
      fname, a string representing a file name in the current directory
      operation, a string representing the operation to be performed on the
      image. 
    Return Value:
      None
    '''
    #Open file in read bytes mode, get bytes specifying width/height
    fp = open(fname,'rb')
    data = list(fp.read())
    old_data = list(data)
    width = big_end_to_int(data[18:22])
    height = big_end_to_int(data[22:26])

    #Data starts at byte 54.  Create matrix of pixels, where each
    #pixel is a 3 element list [red,green,blue].
    #Starts in lower left corner of image.
    i = 54
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = [data[i+2],data[i+1],data[i]]
            i += 3
            row.append(pixel)
        matrix.append(row)
        #Row size must be divisible by 4, otherwise padding occurs
        i += (2-i)%4
    fp.close()

    #Perform operation on the pixel matrix
    if operation == 'add_col':
        new_matrix = add_col(matrix[::-1])
    elif operation == 'swap':
        new_matrix = swap(matrix[::-1])
    elif operation == 'grayscale':
        new_matrix = grayscale(matrix[::-1])
    elif operation == 'custom_filter':
        new_matrix = custom_filter(matrix[::-1])

    elif operation == 'blur':
        new_matrix = blur(matrix[::-1])
    elif operation == 'swap_red_blue':
        new_matrix = swap_red_blue(matrix[::-1])
    else:
        return
    new_matrix = new_matrix[::-1]
    #Write back to new .bmp file.
    #New file name is operation+fname
    i = 54
    for y in range(height):
        for x in range(width):
            pixel = tuple(new_matrix[y][x])
            data[i+2],data[i+1],data[i] = pixel
            i += 3
        i += (2-i)%4
    fp = open(operation+"_"+fname,'wb')
    fp.write(bytearray(data))
    fp.close()


if __name__ == "__main__":
    transform_image("cat.bmp", "custom_filter")
