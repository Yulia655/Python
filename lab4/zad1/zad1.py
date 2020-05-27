import struct
import argparse
import sys
import glob
import os

sample = 'python zad1.py --source "H:\kurs2\python\lab4\zad1\Album" -g 2 -d'
genres = {
    0: 'Blues',
    1: 'Eeeee, rock',
    2: 'Country',
    3: 'Dance',
    4: 'Disco',
    5: 'Funk',
    6: 'Grunge',
    7: 'Hip-Hop',
    8: 'Jazz',
    9: 'Metal',
    10: 'New Age',
    11: 'Oldies',
    12: 'Other',
    13: 'Pop',
    14: 'R&B',
    15: 'Rap',
    16: 'Reggae'
}

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', required='True')
    parser.add_argument('-g', '--genre', required='True')
    parser.add_argument('-d', '--dump', action='store_true')

    args = sys.argv[1:]
    parsed = parser.parse_args(args)

    source = parsed.source[1:-1] \
        if "'" in parsed.source or '"' in parsed.source \
        else parsed.source
    show_dump = parsed.dump
    default_genre = genres[int(parsed.genre)]
    tracklist = list(glob.glob(os.path.join(parsed.source, '*.mp3')))

    get_dump = lambda bytes: ' '.join([hex(byte)[2:] for byte in bytes])
    counter = 1
    for track in tracklist:
        with open(track, 'rb') as trackfile:
            dump = []
            last128 = os.path.getsize(track) - 128
            trackfile.seek(last128)

            dump += [get_dump(trackfile.read(3))]

            packed_title = trackfile.read(30)
            unpacked_title = struct.unpack('c' * 30, packed_title)
            title = ''.join([ch.decode('utf-8') for ch in unpacked_title])
            dump += [get_dump(packed_title)]

            packed_artist = trackfile.read(30)
            unpacked_artist = struct.unpack('c' * 30, packed_artist)
            artist = ''.join([ch.decode('utf-8') for ch in unpacked_artist])
            dump += [get_dump(packed_artist)]

            packed_album = trackfile.read(30)
            unpacked_album = struct.unpack('c' * 30, packed_album)
            album = ''.join([ch.decode('utf-8') for ch in unpacked_album])
            dump += [get_dump(packed_album)]

            dump += [get_dump(trackfile.read(4))]  # year
            dump += [get_dump(trackfile.read(30))]  # comment

            packed_genre = trackfile.read(1)
            genre_index = ord(packed_genre)
            genre = genres[genre_index] \
                if genre_index is not 255 \
                else default_genre
            dump += [get_dump(packed_genre)]

            print(str(counter) + ') ' + ' - '.join([
                artist, title, album, genre
            ]))

            if show_dump:
                print('Hex-dump: \n' + '\n'.join(dump))

            counter += 1

except Exception as ex:
    print('Error: ' + str(ex))

#Complete
