def main():
    with open("testFiles/2.5_day.csv") as file_pointer:
        data = file_pointer.read()
    data = data.split("\n")
    data.pop(0)
    for i, line in enumerate(data):
        line = line.split(",")
        print(f"{line[4]} at {line[13][1:]} {line[14][:-1]}")

main()