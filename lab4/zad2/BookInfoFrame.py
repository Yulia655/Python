# coding=utf-8
import wx


class BookInfoFrame(wx.Frame):

    def __init__(self, book_info):
        wx.Frame.__init__(
            self, None, -1, "Информация о книге", size=(400, 160))
        panel = wx.Panel(self, -1)

        authors_id, title, sheets, publisher, year = book_info

        wx.StaticText(panel, -1,
                      "ID автора: " + str(authors_id).encode('utf-8'),
                      pos=(5, 8))
        wx.StaticText(panel, -1,
                      "Название: " + title.encode('utf-8'),
                      pos=(5, 28))
        wx.StaticText(panel, -1,
                      "Кол-во страниц: " + str(sheets).encode('utf-8'),
                      pos=(5, 48))
        wx.StaticText(panel, -1,
                      "Издательство: " + publisher.encode('utf-8'),
                      pos=(5, 68))
        wx.StaticText(panel, -1,
                      "Год издания: " + str(year).encode('utf-8'),
                      pos=(5, 88))
