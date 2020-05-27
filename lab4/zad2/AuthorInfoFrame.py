# coding=utf-8
import wx
from FileManager import FileManager


class AuthorInfoFrame(wx.Frame):

    def __init__(self, author_info):
        wx.Frame.__init__(
            self, None, -1, "Информация об авторе", size=(340, 160))
        panel = wx.Panel(self, -1)

        self._info = author_info
        id, name, country, years = author_info

        wx.StaticText(panel, -1,
                      "ID: " + str(id).encode('utf-8'), pos=(5, 8))
        wx.StaticText(panel, -1,
                      "ФИО: " + name.encode('utf-8'), pos=(5, 28))
        wx.StaticText(panel, -1,
                      "Страна: " + country.encode('utf-8'), pos=(5, 48))
        wx.StaticText(panel, -1,
                      "Годы жизни: " + years.encode('utf-8'), pos=(5, 68))

        add_button = wx.Button(panel, -1, "Сохранить в файл",
                               size=(120, 25), pos=(5, 88))
        self.Bind(wx.EVT_BUTTON, self.save_info, add_button)

    def save_info(self, event):
        FileManager.save_author_info(self._info)
