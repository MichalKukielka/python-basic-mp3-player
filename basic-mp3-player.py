# Basic Python Music Player - using tkinter and pygame

from tkinter import *
import tkinter.filedialog as filedlg
import tkinter.messagebox as msgbocx
import pygame

playlist = []


class MP3Player(Frame):

    def __init__(self, master):
        """
        Constructor responsible for GUI and connecting methods with buttons.
        :param master:
        """

        super(MP3Player, self).__init__(master)

        # self.create_widgets()
        self.playlist_box = Listbox(self, width=40, height=10, selectmode=SINGLE)
        for song in playlist:
            self.playlist_box.insert(END, song)

        self.grid(rowspan=5, columnspan=4)
        self.playlist_box.grid(row=1)
        self.playButton = Button(self, text='Play', command=self.play)
        self.loopButton = Button(self, text='Loop', command=self.loop)
        self.addButton = Button(self, text='Add', command=self.add)
        self.playButton.grid(row=4, column=0)
        self.loopButton.grid(row=4, column=1)
        self.addButton.grid(row=4, column=2)
        self.pack()

        pygame.init()

    def play(self):
        """
        A method that uses pygame to play the selected song from the playlist.
        """
        if len(playlist) == 0:
            msgbocx.showinfo('Notice', 'No songs in your playlist!\nClick Add to add songs.')
        else:
            pygame.mixer.music.stop()
            selected_songs = self.playlist_box.curselection()
            global playlist_box
            play_it = playlist[int(selected_songs[0])]
            pygame.mixer.music.load(play_it)
            pygame.mixer.music.play(0, 0.0)

    @staticmethod
    def loop():
        """
        The method to loop the song.
        """
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1, 0.0)

    def add(self):
        """
        A method calling window for selecting songs for a playlist. It supports this mechanism.
        :return:
        """
        file = filedlg.askopenfilenames(initialdir='C:/Users/babbu/Downloads')
        songs = root.splitlist(file)  # turn user's opened filenames into tuple
        songs_ist = list(songs)  # convert to list
        # Add the full filename of songto playlist list, and a shortened version to the listBox
        for song in songs_ist:
            playlist.append(song)
            temp = song.split('/')
            song_short = temp[len(temp) - 1]
            self.playlist_box.insert(END, song_short)


root = Tk()
root.title('MP3 - Player')
root.geometry('330x200')
app = MP3Player(root)
app.mainloop()

