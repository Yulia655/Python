def get_frames(signal, size, overlap):
    step = int(size * overlap)
    start = 0
    while start < len(signal) - 1:
        yield signal[start: start + size]
        start += step


sig = [1, -2, 5, 7, 0, -7, 6, 2, 1]
for el in get_frames(sig, 4, 0.5):
    print(el)

#Complete
