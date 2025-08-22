def FCFS(requests, head):
    total_head_movement = 0
    c_head = head
    order = []

    requests = [r for r in requests if r != head]

    for i in requests:
        distance = abs(i - c_head)
        total_head_movement += distance
        order.append(i)
        c_head = i

    return total_head_movement, order


requests = list(map(int, input("Input requests: ").split()))
head = int(input("Input head number: "))

total_movement, order = FCFS(requests, head)
print("\nOrder of execution:", order)
print("Total head movement:", total_movement)
