def filter_average(cand):
    if cand[6] >= 85:
        return True
    return False

def filter_no_fail(cand):
    for i in range(0, 5):
        if cand[i] < 65:
            return False
    return True

def filter_4_high(cand):
    amount_over_85 = 0
    for i in range(len(cand)):
        if cand[i] >= 85:
            amount_over_85 += 1
    if amount_over_85 >= 4:
        return True
    return False
    
def filter_averageCS(cand):
    total = 0
    for i in range(0, 5):
        total += cand[i]
    average = total / 5
    if average >= 85:
        return True
    return False

def filter_all_nf(applicants_list):
    never_failed = []
    for index, ele in enumerate(applicants_list):
        if filter_no_fail(ele):
            never_failed.append(index)
    return never_failed

def aggregated_filter(applicants_list):
    succeeded_tests = []
    for index, ele in enumerate(applicants_list):
        amount_succeedeed = int(filter_average(ele)) + int(filter_no_fail(ele)) + int(filter_4_high(ele)) + int(filter_averageCS(ele))
        if amount_succeedeed >= 3:
            succeeded_tests.append(index)
    return succeeded_tests

def cosine_sim(x, y):
    summationNum = 0
    for i in range(len(x)):
        summationNum += x[i] * y[i]

    summationDemX = 0
    for i in range(len(x)):
        summationDemX += x[i] ** 2
    
    summationDemY = 0
    for i in range(len(y)):
        summationDemY += y[i] ** 2
    
    return ((summationNum) / ((summationDemY * summationDemX) ** 0.5))

if __name__ == '__main__':
    applicants = [
        [95, 93, 50, 91, 98, 90, 82],
        [65, 75, 85, 95, 100, 100, 85],
        [100, 100, 95, 85, 75, 65, 80],
        [98, 70, 55, 61, 98, 90, 90],
        [100, 95, 55, 61, 75, 95, 90],
        [95, 90, 98, 88, 93, 95, 94],
        [90, 80, 80, 100, 70, 75, 90],
        [80, 83, 79, 83, 77, 77, 82],
        [90, 100, 100, 98, 100, 99, 55],
        [77, 82, 92, 100, 95, 92, 70]
    ]

    xapp = [ 85,  70,  99, 100,  81,  82,  91]
    yapp = [ 68,  75,  92,  99,  95,  97,  90]
    zapp = [100,  95,  80,  89,  91,  75,  83]
    print("XY Cosine Sim:", cosine_sim(xapp, yapp))


    qapp = [100, 100, 100, 100, 100, 100, 100]
    rapp = [ 50,  50,  50,  50,  50,  50,  50]

    print("QR Cosine Sim:", cosine_sim(qapp, rapp))

    mapp = [100, 100, 100,   0,   0,   0,   0]
    napp = [  0,   0,   0, 100, 100, 100, 100]
    print("MN Cosine Sim:", cosine_sim(mapp, napp))





