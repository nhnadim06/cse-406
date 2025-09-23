

requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53
seek_sequence = [head]
total_seek = 0

while requests:
   
    nearest = min(requests, key=lambda x: abs(head - x))
    
    total_seek += abs(head - nearest)
    head = nearest
    seek_sequence.append(nearest)
    requests.remove(nearest)

print("\n--- SSTF Disk Scheduling ---")
print("Seek Sequence:", seek_sequence)
print("Total Seek Operations:", total_seek)
