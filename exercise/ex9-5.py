def test_half(func, x):
    try:
        if func(x) == x / 2:
            return "Correct"
        else:
            return "Incorrect"
    except:
        return "Error"