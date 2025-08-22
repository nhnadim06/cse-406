requests = list(map(int, input("Input requests: ").split()))
head = int(input("Input head: "))
c_head = head
total_distance = 0


requests = [r for r in requests if r != head]

print("Sequence:", c_head, end="")

while requests:
    closest = None
    min_distance = float("inf")

    for i in requests:
        distance = abs(c_head - i)
        if distance < min_distance:
            min_distance = distance
            closest = i

    print(" ", closest, end="")
    total_distance += min_distance
    c_head = closest
    requests.remove(closest)

print("\nTotal Distance:", total_distance)
