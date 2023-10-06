import time

def ourTime():
    seconds = (time.time() - 18000) % 86400
    print(seconds)
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    print(f"{int(hours)}:{int(minutes)}")

ourTime()