def main():
    list_a = [1, 2, 3, 4, 5]
    list_b = list_a
    for i in range(10):
        list_a.append(0)
        list_a = list_a[:-1]
    print(len(list_a) + len(list_b))

if __name__ == "__main__":
    main()
    