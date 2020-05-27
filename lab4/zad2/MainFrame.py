# coding=utf-8
import wx
import sqlite3
from AuthorInfoFrame import AuthorInfoFrame
from BookInfoFrame import BookInfoFrame
from AddAuthorFrame import AddAuthorFrame
from AddBookFrame import AddBookFrame


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(
            self, None, -1, "Библиотека", size=(340, 130))
        panel = wx.Panel(self, -1)
        wx.StaticText(panel, -1, "ID автора:", pos=(5, 8))
        self.author_id = wx.TextCtrl(
            panel, -1, "", size=(50, -1), pos=(65, 5))
        search_author_button = wx.Button(panel, -1, "Поиск",
                                         size=(100, 25), pos=(120, 4))

        wx.StaticText(panel, -1, "Название книги:", pos=(5, 35))
        self.book_title = wx.TextCtrl(
            panel, -1, "", size=(115, -1), pos=(100, 32))
        search_book_button = wx.Button(panel, -1, "Поиск",
                                         size=(100, 25), pos=(220, 31))

        add_author_button = wx.Button(panel, -1, "Добавить автора",
                                       size=(100, 25), pos=(5, 61))
        add_book_button = wx.Button(panel, -1, "Добавить книгу",
                                      size=(100, 25), pos=(110, 61))

        self.Bind(wx.EVT_BUTTON, self.show_author_info, search_author_button)
        self.Bind(wx.EVT_BUTTON, self.show_book_info, search_book_button)
        self.Bind(wx.EVT_BUTTON, self.add_author, add_author_button)
        self.Bind(wx.EVT_BUTTON, self.add_book, add_book_button)

    def show_author_info(self, event):
        author_id = self.author_id.Value
        db = sqlite3.connect('Library.db')
        with db:
            cursor = db.cursor()
            request = u'SELECT * FROM Авторы WHERE id = ' + author_id
            cursor.execute(request)
            try:
                finded_authors = cursor.fetchall()
                if len(finded_authors) == 0:
                    raise Exception('Автора с таким ID нет в базе данных!')

                author = finded_authors[0]
                author_info_frame = AuthorInfoFrame(author)
                author_info_frame.Show()

            except Exception as ex:
                wx.MessageBox(str(ex), 'Ошибка!', wx.OK | wx.ICON_ERROR)

    def show_book_info(self, event):
        book_title = self.book_title.Value
        db = sqlite3.connect('Library.db')
        with db:
            cursor = db.cursor()
            request = u'SELECT * FROM Книги WHERE Название = "' + book_title + u'"'
            cursor.execute(request)
            try:
                finded_books = cursor.fetchall()
                if len(finded_books) == 0:
                    raise Exception('Книги с таким названием нет в базе данных!')

                book = finded_books[0]
                book_info_frame = BookInfoFrame(book)
                book_info_frame.Show()

            except Exception as ex:
                wx.MessageBox(str(ex), 'Ошибка!', wx.OK | wx.ICON_ERROR)

    def add_author(self, event):
        add_author_frame = AddAuthorFrame()
        add_author_frame.Show()

    def add_book(self, event):
        add_book_frame = AddBookFrame()
        add_book_frame.Show()
