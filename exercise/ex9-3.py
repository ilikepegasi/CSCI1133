def csv_to_matrix(filename):
    file = open(filename, "r")
    text = file.read()
    text = text.split("\n")
    matrix = []
    for i, line in enumerate(text):
        matrix.append([])
        nums = line.split(",")
        for j, num in enumerate(nums):
            matrix[i].append(int(num))
    file.close()
    return matrix
