import tkinter
from tkinter.ttk import *
import os
from tkinter import messagebox
from pygame import mixer
from random import choice
from tkinter import filedialog
import threading

cwd = os.getcwd()
root = tkinter.Tk()
root.geometry("700x370")
root.minsize(700, 370)
root.maxsize(700, 370)
root.resizable(False, False)
root.iconbitmap(f"{cwd}\\New folder (2)\\music_player_1.ico")
root.title("Music Player (Harsh)")


class MusicPlayer:
    def __init__(self):
        os.chdir(f"{cwd}\\My_music")
        self.i = -1
        self.a = os.listdir()
        for i in self.a:
            c = i.split('.')[1:]
            for j in c:
                if j != 'mp3' and j != 'wav' and j != 'ogg':
                    self.a.pop(self.a.index(i))
        self.p_unp = 'Resume'
        self.m_unm = 'Mute'
        self.open_file2 = 'Not opened'
        self.loaded = None
        self.vol = None
        self.var = False
        self.var2 = 0
        self.color_list = ['gainsboro', 'old lace',
                           'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
                           'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
                           'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
                           'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue',
                           'dark slate blue',
                           'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
                           'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue',
                           'light steel blue',
                           'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise',
                           'turquoise',
                           'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green',
                           'dark olive green',
                           'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green',
                           'spring green',
                           'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
                           'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod',
                           'light goldenrod yellow',
                           'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod',
                           'rosy brown',
                           'indian red', 'saddle brown', 'sandy brown',
                           'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
                           'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink',
                           'light pink',
                           'pale violet red', 'maroon', 'medium violet red', 'violet red',
                           'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
                           'thistle', 'snow2', 'snow3',
                           'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
                           'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
                           'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
                           'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
                           'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
                           'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
                           'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
                           'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
                           'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
                           'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
                           'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
                           'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
                           'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
                           'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
                           'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
                           'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
                           'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
                           'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
                           'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
                           'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
                           'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
                           'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
                           'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
                           'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
                           'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
                           'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
                           'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
                           'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
                           'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
                           'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
                           'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
                           'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
                           'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
                           'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
                           'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
                           'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
                           'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
                           'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
                           'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
                           'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
                           'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
                           'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
                           'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
                           'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
                           'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
                           'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
                           'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
                           'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
                           'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
                           'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
                           'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
                           'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
                           'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
                           'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
                           'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
                           'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
                           'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

    def change_colr(self):
        rand_color = choice(self.color_list)
        music_playing.config(fg=rand_color)
        rand_color2 = choice(self.color_list)
        main_img.config(bg=rand_color2)
        music_playing.after(1000, self.change_colr)

    def change_colrbg(self):
        rand_color2 = choice(self.color_list)
        main_img.config(bg=rand_color2)
        main_img.after(250, self.change_colrbg)
    def add_dir(self, x):
        ch_dir_name = filedialog.askdirectory()
        if ch_dir_name!= '':
            for songs in range(len(cl.a)):
                list_song.delete(tkinter.END)
            os.chdir(ch_dir_name)
            self.a = os.listdir()
            for i in self.a:
                c = i.split('.')[1:]
                if c != ['mp3'] and c != ['wav'] and c != ['ogg']:
                    del self.a[self.a.index(i)]
                self.i = 0
            for songs in range(len(cl.a)):
                ins = cl.a[songs].split('.')[1:]
                for o in ins:
                    if o == 'mp3' or o == 'wav' or o == 'ogg':
                        list_song.insert(songs, cl.a[songs])
    def open_file(self, x):
        file_name = filedialog.askopenfilename()
        try:
            mixer.music.load(file_name)
            mixer.music.play(mixer.music.get_pos())
            self.open_file2 = 'Opened'
            if self.p_unp == 'Resume':
                self.p_unp = 'Pause'
                btn.config(image=img)
            var1 = os.path.split(file_name)
            var2 = var1[1:]
            for q in var2:
                if len(q)<=30:
                    music_playing.config(text=q)
                    self.loaded = q
                else:
                    a = q[:30]
                    a+='....'
                    music_playing.config(text=a)
                    self.loaded = a
        except:
            var1 = os.path.split(file_name)
            var2 = var1[1:]
            for q in var2:
                messagebox.showinfo(title='ERROR', message=f'Cannot play {q}')

    def rewind(self, x):
        try:

            rand_color = choice(self.color_list)
            music_playing.config(fg=rand_color)
            mixer.music.play(mixer.music.get_pos())
        except:
            self.a.pop(self.a.index(self.a[self.i]))
            mixer.music.play()
        if self.p_unp == 'Resume':
            self.p_unp = 'Pause'
            btn.config(image=img)
        if self.open_file2 == 'Opened':
            music_playing.config(text=self.loaded)
        else:
            if len(self.a[self.i])<=30:
                music_playing.config(text=self.a[self.i])
            else:
                a = self.a[self.i][:30]
                a+='....'
                music_playing.config(text=a)

    def after(self, x):
        mixer.init()
        self.open_file2 = 'Not opened'
        try:
            self.i += 1
            mixer.init()
            mixer.music.load(self.a[self.i])
            mixer.music.play(mixer.music.get_pos())
            if self.p_unp == 'Resume':
                self.p_unp = 'Pause'
                btn.config(image=img)
        except:
            self.i -= len(self.a)
            mixer.init()
            mixer.music.load(self.a[self.i])
            mixer.music.play(mixer.music.get_pos())
            mixer.init()
            mixer.music.load(self.a[self.i])
            mixer.music.play(mixer.music.get_pos())
            if self.p_unp == 'Resume':
                self.p_unp = 'Pause'
                btn.config(image=img)
        if len(self.a[self.i])<=30:
            music_playing.config(text=self.a[self.i])
        else:
            a = self.a[self.i][:30]
            a+='....'
            music_playing.config(text=a)
        rand_color = choice(self.color_list)
        music_playing.config(fg=rand_color)

    def before(self, x):
        mixer.init()
        self.open_file2 = 'Not opened'
        try:
            self.i -= 1
            try:
                mixer.init()
                mixer.music.load(self.a[self.i])
                mixer.music.play(mixer.music.get_pos())
            except:
                self.a.pop(self.a.index(self.a[self.i]))
                self.i -= 1
                mixer.init()
                mixer.music.load(self.a[self.i])
                mixer.music.play(mixer.music.get_pos())
            if self.p_unp == 'Resume':
                self.p_unp = 'Pause'
                btn.config(image=img)
        except:
            self.i += len(self.a)
            if self.p_unp == 'Resume':
                self.p_unp = 'Pause'
                btn.config(image=img)
                try:
                    mixer.init()
                    mixer.music.load(self.a[self.i])
                    mixer.music.play(mixer.music.get_pos())
                except:
                    self.a.pop(self.a.index(self.a[self.i]))
                    self.i += len(self.a)
                    mixer.init()
                    mixer.music.load(self.a[self.i])
                    mixer.music.play(mixer.music.get_pos())
        if len(self.a[self.i])<=30:
            music_playing.config(text=self.a[self.i])
        else:
            a = self.a[self.i][:30]
            a+='....'
            music_playing.config(text=a)
        color_list = ['red', 'purple', 'gold', 'pink', 'orange', 'black', 'blue']
        rand_color = choice(color_list)
        music_playing.config(fg=rand_color)

    def pause_unpause(self, x):
        if self.p_unp != 'Resume':
            mixer.music.pause()
            self.p_unp = 'Resume'
            self.img = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\pause.png')
            btn.config(image=self.img)
        else:
            mixer.music.unpause()
            self.p_unp = 'Pause'
            btn.config(image=img)

    def mute_unmute(self, x):
        if self.m_unm != 'UnMute':
            mixer.music.set_volume(0)
            volume.set(0)
            self.m_unm = 'UnMute'
            self.img1 = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\mute (1).png')
            btn6.config(image=self.img1)
        else:
            if self.vol != None:
                mixer.music.set_volume(25)
                volume.set(25)
            else:
                mixer.music.set_volume(self.vol)
                volume.set(self.vol)
            self.m_unm = 'Mute'
            btn6.config(image=img11)

    def volume(self, x):
        vol2 = volume.get() / 100
        self.vol = vol2
        mixer.music.set_volume(vol2)
        if vol2 == 0:
            self.m_unm = 'UnMute'
            self.img1 = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\mute (1).png')
            btn6.config(image=self.img1)
        else:
            self.m_unm = 'Mute'
            btn6.config(image=img11)

    def play_selected(self, x):
        try:
            mixer.init()
            mixer.music.load(list_song.get(tkinter.ACTIVE))
            mixer.music.play(mixer.music.get_pos())
            color_list = ['red', 'purple', 'gold', 'pink', 'orange', 'black', 'blue']
            rand_color = choice(color_list)
            self.i = self.a.index(list_song.get(tkinter.ACTIVE))
            if len(list_song.get(tkinter.ACTIVE))<=30:
                music_playing.config(text=list_song.get(tkinter.ACTIVE), fg=rand_color)
            else:
                a = list_song.get(tkinter.ACTIVE)[:30]
                a+='....'
                music_playing.config(text=a, fg=rand_color)
            if self.p_unp == 'Resume':
                self.p_unp = 'Pause'
                btn.config(image=img)
        except:
            color_list = ['red', 'purple', 'gold', 'pink', 'orange', 'black', 'blue']
            rand_color = choice(color_list)
            music_playing.config(text=list_song.get(tkinter.ACTIVE), fg=rand_color)

    def sleep(self, x):
        if self.var2 == 0:
            root.attributes('-alpha', 0.5)
            self.var2 = 1
        elif self.var2 == 1:
            root.attributes('-alpha', 0.1)
            self.var2 = 2
        elif self.var2 == 2:
            root.attributes('-alpha', 0.02)
            self.var2 = 3
        else:
            root.attributes('-alpha', 10.0)
            self.var2 = 0


if __name__ == '__main__':
    cl = MusicPlayer()
    mixer.init()
    vol = mixer.music.get_volume()
    image = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\music.gif')
    main_img = tkinter.Label(root, image=image, borderwidth=5)
    main_img.place(x=0, y=0)
    scrl = Scrollbar(root)
    scrl.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    list_song = tkinter.Listbox(root, width=50, bg='cyan', height=13)
    list_song.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    list_song.bind('<Double-1>', cl.play_selected)
    music_playing = tkinter.Label(root, font="Arial 14 bold")
    music_playing.place(x=10, y=250)
    music_playing.bind('<Double-1>', cl.rewind)
    img11 = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\sound.png')
    btn6 = Label(root, image=img11)
    btn6.place(x=0, y=330)
    btn6.bind('<Button-1>', cl.mute_unmute)
    volume = Scale(root, from_=0, to=100, orient=tkinter.HORIZONTAL, command=cl.volume, length=150)
    volume.place(x=40, y=335)
    volume.set(25)
    img = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\play.png')
    btn = tkinter.Label(image=img)
    btn.place(x=240, y=330)
    btn.bind('<Button-1>', cl.pause_unpause)
    img44 = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\rewind.png')
    btn3 = Label(image=img44)
    btn3.place(x=340, y=330)
    btn3.bind('<Button-1>', cl.rewind)
    img3 = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\next.png')
    btn5 = Label(image=img3)
    btn5.place(x=290, y=330)
    btn5.bind('<Button-1>', cl.after)
    img2 = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\previous.png')
    btn4 = Label(image=img2)
    btn4.place(x=190, y=330)
    btn4.bind('<Button-1>', cl.before)
    img20 = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\music-note.png')
    btn20 = Label(image=img20)
    btn20.place(x=0, y=0)
    img10 = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\night-mode.png')
    btn10 = Label(image=img10)
    btn10.place(x=345, y=0)
    btn10.bind('<Button-1>', cl.sleep)
    btn20.bind('<Button-1>', cl.open_file)
    img67 = tkinter.PhotoImage(file=f'{cwd}\\New folder (2)\\plus.png')
    btn67 = Label(image=img67)
    btn67.place(x=0, y=220)
    btn67.bind('<Button-1>', cl.add_dir)
    for songs in range(len(cl.a)):
        ins = cl.a[songs].split('.')[1:]
        for o in ins:
            if o == 'mp3' or o == 'wav' or o == 'ogg':
                list_song.insert(songs, cl.a[songs])
    scrl.config(command=list_song.yview)
    list_song.config(yscrollcommand=scrl.set)
    thr = threading.Thread(target=cl.change_colr)
    thr.start()
    thr2 = threading.Thread(target=cl.change_colrbg)
    thr2.start()
    root.mainloop()
