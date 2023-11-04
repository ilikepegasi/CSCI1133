def join(queue, student):
    queue.append(student)
    print(student, "has joined the queue.")

def kick(queue):
    next = queue.pop(0)
    print(next+", it is your turn.")

def position(queue, student):
    print(student, "is in position", queue.index(student)+1)
    return None

def display(queue):
    place = 1
    for student in queue:
        print(place, student)
        place += 1
