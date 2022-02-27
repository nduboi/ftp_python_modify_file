from tkinter import *
from typing import Collection 
import webbrowser
import os
from ftplib import FTP
import time
import tkinter
def open_primary_windows() :
    # Partie Script
     
    def open_site():
        webbrowser.open_new("")
    def name_stream():
        ftp = FTP('')
        ftp.login(user='', passwd='')
        ftp.cwd('/test/build/includes')
        namestream = title_stream_entry.get()

        def grabFile():
            fileName = ''
            localfile = open(fileName,'wb')
            ftp.retrbinary('RETR ' + fileName, localfile.write, 1024)
            localfile.close()

        def placeFile():
            filename = ''
            ftp.storbinary('STOR ' +filename, open(filename, 'rb'))

      
        fullname =""
        fo = open("", "w")
        fo.write(fullname);
        fo.close()
        placeFile()
        ftp.quit()
    def open_second_windows():
        windows_streamname.destroy()
        def open_second_windows_version():
        # Partie Script
            def open_site():
                webbrowser.open_new("")
            def version_stream():
                ftp = FTP('')
                ftp.login(user='', passwd='')
                ftp.cwd('')
                version = title_stream_entry.get()

                def grabFile():
                    fileName = ''
                    localfile = open(fileName,'wb')
                    ftp.retrbinary('RETR ' + fileName, localfile.write, 1024)
                    localfile.close()

                def placeFile():
                    filename = ''
                    ftp.storbinary('STOR ' +filename, open(filename, 'rb'))

                
                fullname =""
                fo = open("", "w")
                fo.write(fullname);
                fo.close()
                placeFile()
                ftp.quit()
            def leave():
                windows_version.destroy()
            # Fin de la partie Script
            windows_version = Tk()
                #personaliser la fenêtre
            windows_version.title("Changement info site")
            windows_version.iconbitmap('Nduboi.ico')
            windows_version.geometry("420x220")
            windows_version.minsize(400, 200)
            windows_version.maxsize(420, 220)
            windows_version.config(background='#2f4f4f')
                #Boite container
            windows_frame= Frame(windows_version, bg="#2f4f4f")
                # Boite sous conatiner
            windows_top = Frame(windows_frame, bg="#2f4f4f", borderwidth=3, relief="solid")

            windows_top_frame= Frame(windows_version, bg="#2f4f4f", borderwidth=3, relief="solid")

            windows_right_frame= Frame(windows_frame, bg="#2f4f4f", borderwidth=3, relief="solid")

            windows_bottom_frame= Frame(windows_version, bg="#2f4f4f", borderwidth=3, relief="solid")
                #Ajouter un titre
            label_title = Label(windows_top, text="Changement de la version du site", font=("Courrier", 13), bg='#2f4f4f', fg='white')
            label_title.pack()
                #Ajouter un second titre
            label_subtitle = Label(windows_top_frame, text="Version du site", font=("Courrier", 10), bg='#2f4f4f', fg='white')
            label_subtitle.pack()
                #création d'un champ
            title_stream_entry = Entry(windows_top_frame, font=("Arial", 10), bg='white')
            title_stream_entry.pack(pady=10)

                #ajouter un button
            submit_button = Button(windows_top_frame, text="Envoyer", font=("Courrier", 10), bg='White', command=version_stream)
            submit_button.pack()
                # boite bottom frame left and right
            windows_bottom_frame_left= Frame(windows_bottom_frame, bg='#2f4f4f' )
            windows_bottom_frame_right= Frame(windows_bottom_frame, bg='#2f4f4f' )
                #affichage de la boite subtitle and champs
            site_button = Button(windows_bottom_frame_left, text="Vers le site Web", font=("Courrier", 9), bg='White', command=open_site)
            site_button.pack()
            version_button = Button(windows_bottom_frame_right, text="Quitter", font=("Courrier", 9), bg='White', command=leave)
            version_button.pack()
            windows_frame.pack()
            windows_top.pack()
            windows_top_frame.pack(expand=YES)
            windows_right_frame.pack(side="right", expand=YES)
            windows_bottom_frame_right.grid(row=0, column=2, sticky=E)
            windows_bottom_frame_left.grid(row=0, column=1, sticky=W)
            windows_bottom_frame.pack(side=BOTTOM)
                # Boite Gauche
            windows_left= Frame(windows_version, bg="#2f4f4f", borderwidth=3, relief="solid")
            windows_left.pack(side="left")
                # Boite Droite
            windows_right= Frame(windows_version, bg="#2f4f4f", borderwidth=3, relief="solid")
            windows_right.pack(side="right")
                #Afficher la fenêtre
            windows_version.mainloop()  
        open_second_windows_version()
    # Fin de la partie Script
    windows_streamname = Tk()
        #personaliser la fenêtre
    windows_streamname.title("Changement info site")
    windows_streamname.geometry("420x220")
    windows_streamname.iconbitmap('Nduboi.ico')
    windows_streamname.minsize(400, 200)
    windows_streamname.maxsize(420, 220)
    windows_streamname.config(background='#2f4f4f')
        #Boite container
    windows_frame= Frame(windows_streamname, bg="#2f4f4f")
        # Boite sous conatiner
    windows_top = Frame(windows_frame, bg="#2f4f4f", borderwidth=3, relief="solid")

    windows_top_frame= Frame(windows_streamname, bg="#2f4f4f", borderwidth=3, relief="solid")

    windows_right_frame= Frame(windows_frame, bg="#2f4f4f", borderwidth=3, relief="solid")

    windows_bottom_frame= Frame(windows_streamname, bg="#2f4f4f", borderwidth=3, relief="solid")
        #Ajouter un titre
    label_title = Label(windows_top, text="Changement du nom du stream", font=("Courrier", 13), bg='#2f4f4f', fg='white')
    label_title.pack()
        #Ajouter un second titre
    label_subtitle = Label(windows_top_frame, text="Le nom du stream", font=("Courrier", 10), bg='#2f4f4f', fg='white')
    label_subtitle.pack()
        #création d'un champ
    title_stream_entry = Entry(windows_top_frame, font=("Arial", 10), bg='white')
    title_stream_entry.pack(pady=10)

        #ajouter un button
    submit_button = Button(windows_top_frame, text="Envoyer", font=("Courrier", 10), bg='White', command=name_stream)
    submit_button.pack()
        # boite bottom frame left and right
    windows_bottom_frame_left= Frame(windows_bottom_frame, bg='#2f4f4f' )
    windows_bottom_frame_right= Frame(windows_bottom_frame, bg='#2f4f4f' )
        #affichage de la boite subtitle and champs
    site_button = Button(windows_bottom_frame_left, text="Vers le site Web", font=("Courrier", 9), bg='White', command=open_site)
    site_button.pack()
    version_button = Button(windows_bottom_frame_right, text="Changer la version", font=("Courrier", 9), bg='White', command=open_second_windows)
    version_button.pack()
    windows_frame.pack()
    windows_top.pack()
    windows_top_frame.pack(expand=YES)
    windows_right_frame.pack(side="right", expand=YES)
    windows_bottom_frame_right.grid(row=0, column=2, sticky=E)
    windows_bottom_frame_left.grid(row=0, column=1, sticky=W)
    windows_bottom_frame.pack(side=BOTTOM)
        # Boite Gauche
    windows_left= Frame(windows_streamname, bg="#2f4f4f", borderwidth=3, relief="solid")
    windows_left.pack(side="left")
        # Boite Droite
    windows_right= Frame(windows_streamname, bg="#2f4f4f", borderwidth=3, relief="solid")
    windows_right.pack(side="right")
        #Afficher la fenêtre
    windows_streamname.mainloop()  
open_primary_windows()