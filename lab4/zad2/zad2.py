# -*- coding: utf-8 -*-
import sqlite3
import wx
import hashlib
from MainFrame import MainFrame


class AuthorizationFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(
            self, None, -1, "Авторизация", size=(270, 130))
        panel = wx.Panel(self, -1)

        wx.StaticText(panel, -1, "Логин:", pos=(5, 8))
        self.login = wx.TextCtrl(
            panel, -1, "", size=(195, -1), pos=(55, 5))
        self.login.Value = 'Jarvis'

        wx.StaticText(panel, -1, "Пароль:", pos=(5, 35))
        self.password = wx.TextCtrl(
            panel, -1, "", size=(195, -1), pos=(55, 32))
        self.password.Value = '114380'

        sign_in_button = wx.Button(panel, -1, "Вход",
                                         size=(100, 25), pos=(150, 60))

        self.Bind(wx.EVT_BUTTON, self.sign_in, sign_in_button)

    def sign_in(self, event):
        db = sqlite3.connect('Library.db')
        with db:
            cursor = db.cursor()
            hash_pass = hashlib.md5(self.password.Value).hexdigest()
            cursor.execute('SELECT * FROM Пользователи')
            users = cursor.fetchall()
            for each_user in users:
                login, password = each_user
                if self.login.Value == login and hash_pass == password:
                    main_frame = MainFrame()
                    main_frame.Show()
                    self.Close()
                    break

            else:
                wx.MessageBox('Пользователя с такими данными не существует.',
                              'Ошибка!',
                              wx.OK | wx.ICON_ERROR)


if __name__ == '__main__':
    app = wx.App()
    start_frame = AuthorizationFrame()
    start_frame.Show()
    app.MainLoop()

#Complete
