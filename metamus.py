import os
import eyed3

def main():
    
    #getting directory name from user
    music_dir = input("Enter directory in 'Music': ")
    music_dir = os.path.join(os.path.expanduser("~/Music/"), music_dir)
   
    #finding mp3 files in directory
    songs = []
    for _, _, filenames in os.walk(music_dir):
        for name in filenames:
            if name.endswith(".mp3"): songs.append(name)
  
    #asking to see if anything can be skipped
    if input("Set metadata? (y/n): ").strip().lower() == "y":
        artist = ""
        album = ""
        same_ar = input("Do all songs have the same ARTIST? (y/n): ").strip().lower()
        if same_ar == "y": artist = input("Artist name: ")
        same_al = input("Do all songs have the same ALBUM? (y/n): ").strip().lower()
        if same_al == "y": album = input("Album name: ")
        same_ti = input("Do all songs have the same TITLE as the FILE NAME? (y/n): ").strip().lower()
        print()

    #call set_data() for every song
        for song in songs: set_data(music_dir, song, artist, album, same_ar, same_al, same_ti)

    #summary
    if input("Print summary? (y/n): ").strip().lower() == "y":
        for song in songs: summ(music_dir, song)


def set_data(music_dir, song, artist, album, same_ar, same_al, same_ti):
    
    #accessing metadata of song
    fileloc = os.path.join(music_dir, song)
    audiofile = eyed3.load(fileloc)
    if audiofile is None or audiofile.tag is None:
        print(f"Error: Could not load metadata for '{song}'")
        return

    #setting default values/global artist and album if defined above
    audiofile.tag.title = song[:-4]
    audiofile.tag.artist = artist
    audiofile.tag.album = album
    
    #getting and setting metadata from user input
    if same_ti != "y": audiofile.tag.title = input("TITLE of '" + song + "': ")
    if same_ar != "y": audiofile.tag.artist = input("ARTIST of '" + song + "': ")
    if same_al != "y": audiofile.tag.album = input("ALBUM of '" + song + "': ")
    try:
        audiofile.tag.track_num = int(input("TRACK NUMBER  of '" + song + "': "))
    except ValueError:
        print("Invalid input! Using default track number 0.")
        audiofile.tag.track_num = 0

    audiofile.tag.save()
    print()


def summ(music_dir, song):
    audiofile = eyed3.load(os.path.join(music_dir, song))
    print(f"{audiofile.tag.track_num[0]} - {audiofile.tag.title} - {audiofile.tag.artist} - {audiofile.tag.album}")
    print()


if __name__ == "__main__":
    main()
