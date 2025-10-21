def fifo (pages, f_size):
    frames = []
    page_faults = 0
    page_hits = 0
    fifo_indx =0

    for page in pages:
        if page in frames:
            page_hits += 1
            print(f"page {page} ---- Hit | Frame: {frames}")
        else:
            page_faults += 1
            if len(frames)<f_size:
                frames.append(page)
            else:
                frames[fifo_indx ] = page
                fifo_indx = (fifo_indx + 1) % f_size
            print(f"page {page} --- Miss | Frames: {frames}")
    print(f"Total Page Fault: {page_faults}")
    print(f"Total Page Hit: {page_hits}")

page_input = input("enter page reference: ")
pages = list(map(int, page_input.split()))
f_size = int(input("enter frame size :"))

fifo(pages,f_size)

