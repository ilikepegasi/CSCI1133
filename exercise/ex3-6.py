def grad_TAs(number, labs, students):
    if(number[0] in ["1", "2"]):
        return 1
    elif (students < 50) and (labs >= 1):
        return 1
    else:
        return (students // 50)

def main():
    print(grad_TAs('1133', 9, 292))     #1  (starts w/ '1' or '2')
    print(grad_TAs('2011', 13, 560))    #1  (starts w/ '1' or '2')
    print(grad_TAs('8211', 0, 20))      #0  (<50 students, no labs)
    print(grad_TAs('4271W', 2, 27))     #1  (<50 students, has lab)
    print(grad_TAs('5801', 0, 118))     #2  (118//50 = 2)


if __name__ == '__main__':
    main()
