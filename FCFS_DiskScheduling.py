def FCFS(request, head):
    total_head_movement = 0
    c_head = head
    order = []

    for i in request:
        if i == c_head: 
            continue
        else:
            distance = abs(i - c_head)
            total_head_movement += distance
            order.append(i)
            c_head = i

    return total_head_movement, order


request = list(map(int, input("Input requests: ").split()))
head = int(input("Input head number: "))

total_movement, order = FCFS(request, head)
print("\nOrder of execution:", order)
print("Total head movement:", total_movement)
