##CScan

r_seq = [14, 20, 29, 40, 50, 110]
head = 29
direction = "right"

seek_seq = []
seek_count = 0

r_seq.sort()

if direction == "left":
    for track in reversed(r_seq):
        if track <= head:
            seek_seq.append(track)
            seek_count += abs(head - track)
            head = track
    if r_seq[-1] > head:
        seek_count += abs(head - r_seq[-1])
        head = r_seq[-1]

    for track in reversed(r_seq):
        if track < head and track not in seek_seq:
            seek_seq.append(track)
            seek_count += abs(head - track)
            head = track

else: 
    for track in r_seq:
        if track >= head:
            seek_seq.append(track)
            seek_count += abs(head - track)
            head = track
    if r_seq[0] < head:
        seek_count += abs(head - r_seq[0])
        head = r_seq[0]
    for track in r_seq:
        if track > head and track not in seek_seq:
            seek_seq.append(track)
            seek_count += abs(head - track)
            head = track

print("Head movement:", seek_seq)
print("Total Seek Count:", seek_count)
