def shorter_string(left, right):
    result = []
    for i in enumerate(left):
        if len(left[i[0]]) > len(right[i[0]]):
            result.append(right[i[0]])
        elif len(left[i[0]]) < len(right[i[0]]):
            result.append(left[i[0]])
        else:
            result.append("Tie")
    return result


