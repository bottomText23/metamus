import os
import eyed3

def main():
    music_dir = input("Enter directory in 'Music': ")
    music_dir = os.path.join(os.path.expanduser("~/Music/"), music_dir)
    
    songs = []
    for _, _, filenames in os.walk(music_dir):
        for name in filenames:
            if name.endswith(".mp3"): songs.append(name)
   
    if input("Set metadata? (y/n): ") == "y":
        artist = ""
        album = ""
        same_ar = input("Do all songs have the same ARTIST? (y/n): ")
        if same_ar == "y": artist = input("Artist name: ")
        same_al = input("Do all songs have the same ALBUM? (y/n): ")
        if same_al == "y": album = input("Album name: ")
        same_ti = input("Do all songs have the same TITLE as the FILE NAME? (y/n): ")
        print()

        for song in songs: set_data(music_dir, song, artist, album, same_ar, same_al, same_ti)

    if input("Print summary? (y/n): ") == "y":
        for song in songs: summ(music_dir, song)


def set_data(music_dir, song, artist, album, same_ar, same_al, same_ti):
    fileloc = os.path.join(music_dir, song) 
    audiofile = eyed3.load(fileloc)
    audiofile.tag.title = song[:-4]
    audiofile.tag.artist = artist
    audiofile.tag.album = album
    
    if same_ti != "y": audiofile.tag.title = input("TITLE of '" + song + "': ")
    if same_ar != "y": audiofile.tag.artist = input("ARTIST of '" + song + "': ")
    if same_al != "y": audiofile.tag.album = input("ALBUM of '" + song + "': ")
    audiofile.tag.track_num = int(input("TRACK NUMBER  of '" + song + "': "))
    audiofile.tag.save()
    print()

def summ(music_dir, song):
    audiofile = eyed3.load(os.path.join(music_dir, song))
    print(str(audiofile.tag.track_num[0]) + " - " + str(audiofile.tag.title) + " - " + str(audiofile.tag.artist) + " - " + str(audiofile.tag.album))
    print()

if __name__ == "__main__":
    main()
