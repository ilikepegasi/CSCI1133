import statistics as stats

def stocks_ew(file_name):
    try:
        with open(file_name) as file_pointer:
            data = file_pointer.read()
            data = data.split("\n")
            data.pop(0)
            for i, line in enumerate(data):
                data[i] = line.split(",")
                data[i] = float(data[i][3])
        stocks_median = stats.median(data)
        stocks_maximum = max(data)
        stocks_minimum = min(data)
        stocks_mean = stats.mean(data)
        return {"mean":stocks_mean, "median":stocks_median, "minimum":stocks_minimum, "maximum":stocks_maximum}
    except FileNotFoundError:
        print("you are a bad girl")


print(stocks_ew("testFiles/MDT.csv"))