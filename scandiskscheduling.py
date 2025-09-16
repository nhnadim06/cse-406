r_seq = [14, 20, 29, 40, 50, 110]
head = 29
direction = "left"

r_seq.sort()


start = 0
for i in range(len(r_seq)):
    if r_seq[i] > head:
        start = i
        break
    elif r_seq[i] == head:
        start = i
        break

order = []
if direction == "left":
    for i in range(start - 1, -1, -1):
        order.append(r_seq[i])
    for i in range(start, len(r_seq)):
        order.append(r_seq[i])
else:
    for i in range(start, len(r_seq)):
        order.append(r_seq[i])
    for i in range(start - 1, -1, -1):
        order.append(r_seq[i])

seek_seq = []
seek_count = 0
current = head

for track in order:
    seek_seq.append(track)
    seek_count += abs(current - track)
    current = track

print("Head movement:", [head] + seek_seq)
print("Total seek:", seek_count)
