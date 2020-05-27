# coding=utf-8
import wx
import sqlite3


class AddBookFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(
            self, None, -1, "Добавление книги", size=(370, 220))
        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, "ID автора:", pos=(5, 8))
        self.author_id = wx.TextCtrl(
            panel, -1, "", size=(200, -1), pos=(130, 5))

        wx.StaticText(panel, -1, "Название:", pos=(5, 35))
        self.title = wx.TextCtrl(
            panel, -1, "", size=(200, -1), pos=(130, 32))

        wx.StaticText(panel, -1, "Количество страниц:", pos=(5, 63))
        self.sheets = wx.TextCtrl(
            panel, -1, "", size=(200, -1), pos=(130, 60))

        wx.StaticText(panel, -1, "Издательство:", pos=(5, 91))
        self.publisher = wx.TextCtrl(
            panel, -1, "", size=(200, -1), pos=(130, 88))

        wx.StaticText(panel, -1, "Год издания:", pos=(5, 119))
        self.year = wx.TextCtrl(
            panel, -1, "", size=(200, -1), pos=(130, 116))

        add_button = wx.Button(panel, -1, "Добавить",
                               size=(100, 25), pos=(5, 144))

        self.Bind(wx.EVT_BUTTON, self.add_book, add_button)

    def add_book(self, event):
        author_id = int(self.author_id.Value)
        title = self.title.Value
        sheets = int(self.sheets.Value)
        publisher = self.publisher.Value
        year = int(self.year.Value)

        db = sqlite3.connect('Library.db')
        with db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO Книги VALUES(?,?,?,?,?)',
                           (author_id, title, sheets, publisher, year))
            db.commit()

            cursor.execute('SELECT * FROM Книги')
            books = cursor.fetchall()
            for book in books:
                cur_book = (author_id, title, sheets, publisher, year)
                if cur_book == book:
                    wx.MessageBox('Название книги: ' + title.encode('utf-8'),
                                  'Саксес!', wx.OK)
                    break
