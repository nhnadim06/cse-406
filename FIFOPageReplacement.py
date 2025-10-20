def fifo(pages, frame_size):
    frames = []      
    page_faults = 0  
    page_hits = 0    
    fifo_index = 0   

    for page in pages:

        if page in frames:
            page_hits += 1
            print(f"Page {page} -> Hit  | Frames: {frames}")

        else:
            page_faults += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames[fifo_index] = page
                fifo_index = (fifo_index + 1) % frame_size

            print(f"Page {page} -> Miss | Frames: {frames}")

    print(f"Total Page Faults: {page_faults}")
    print(f"Total Page Hits: {page_hits}")

page_input = input("Enter page reference string: ")
pages = list(map(int, page_input.split()))
frame_size = int(input("Enter frame size: "))

fifo(pages, frame_size)
