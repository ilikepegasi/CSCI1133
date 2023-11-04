fpin = open('ex9-6.py')
data = fpin.readlines()
fpin.close()

if data[-1].strip() == "print('Yes')":
    data[-1] = "print('No')"
else:
    data[-1] = "print('Yes')"

fpout = open('ex9-6.py', 'w')
fpout.writelines(data)
fpout.close()

print('Yes')