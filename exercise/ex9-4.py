
def remove_t(fname):
    try:
        file1 = open(fname)
        new_name = fname
        new_name = "no_t_" + new_name
        file2 = open(new_name, "x")
        file2.write(file1.read().replace("t", ""))
        file1.close()
        file2.close()
    except:
        print('File does not exist')


