# coding=utf-8
import wx
import sqlite3
from FileManager import FileManager


class AddAuthorFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(
            self, None, -1, "Добавление автора", size=(340, 160))
        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, "ФИО автора:", pos=(5, 8))
        self.name = wx.TextCtrl(
            panel, -1, "", size=(200, -1), pos=(100, 5))

        wx.StaticText(panel, -1, "Страна:", pos=(5, 35))
        self.country = wx.TextCtrl(
            panel, -1, "", size=(200, -1), pos=(100, 32))

        wx.StaticText(panel, -1, "Годы жизни:", pos=(5, 63))
        self.years = wx.TextCtrl(
            panel, -1, "", size=(200, -1), pos=(100, 60))

        add_button = wx.Button(panel, -1, "Добавить",
                                       size=(100, 25), pos=(5, 88))

        load_file_button = wx.Button(panel, -1, "Загрузить из файла",
                                       size=(150, 25), pos=(110, 88))

        self.Bind(wx.EVT_BUTTON, self.add_author, add_button)
        self.Bind(wx.EVT_BUTTON, self.load_from_file, load_file_button)

    def add_new_author(self, author_data):
        name, country, years = author_data
        db = sqlite3.connect('Library.db')
        with db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO Авторы VALUES(NULL, ?,?,?)',
                           (name, country, years))
            db.commit()

            cursor.execute('SELECT * FROM Авторы')
            authors = cursor.fetchall()
            for author in authors:
                id, cort_n, cort_c, cort_y = author
                if (name, country, years) == (cort_n, cort_c, cort_y):
                    wx.MessageBox('id автора: ' + str(id), 'Саксес!', wx.OK)
                    break

    def add_author(self, event):
        name, country, years = self.name.Value, self.country.Value, self.years.Value
        self.add_new_author((name, country, years))

    def load_from_file(self, event):
        author = FileManager.load_author_info()
        if author is not None:
            self.add_new_author(author)
