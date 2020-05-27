# encoding: utf8
import wx
import os
import re
from datetime import datetime

class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          'Искатель по шаблону', size=(500, 400))
        self.create_menu()
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([-3, -2])

        self.list_box = wx.ListBox(self, -1, (20, 20), (80, 120),
                              [''], wx.LB_SINGLE)

        self.statusbar.SetStatusText('Открыт лог')
        self.statusbar.SetStatusText("0 байт", 1)

    def menu_data(self):
        data = (("&Файл",
                 ({"&Открыть...": self.on_open_file},)),
                ("&Лог",
                 ({"&Экспорт": self.export_log},
                  {"&Добавить в лог": self.add_to_log},
                  {"&Просмотр": self.show_log})
                 ))
        return data

    def create_menu(self):
        menu = wx.MenuBar()

        for item in self.menu_data():
            menu_item = self.create_sub_menu(item[1])
            menu.Append(menu_item, item[0])

        self.SetMenuBar(menu)

    def create_sub_menu(self, itemgroup):
        groupmenu = wx.Menu()

        for item in itemgroup:
            title, handler = item.items()[0]
            menu_item = groupmenu.Append(-1, title)
            if handler:
                self.Bind(wx.EVT_MENU, handler, menu_item)

        return groupmenu

    def on_open_file(self, event):
        dlg = wx.FileDialog(self, message='Выберите файл', defaultDir='',
                            defaultFile='', wildcard='*.*', style=wx.FLP_OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            self.statusbar.SetStatusText(
                'Обработан файл '.decode('utf-8') + dlg.GetPath())

            size = str(os.path.getsize(dlg.GetPath()))
            if len(size) > 3:
                formatted_size = ''
                counter = 0
                for sym in size[::-1]:
                    formatted_size += sym if counter % 3 else ' ' + sym
                    counter += 1

                size = formatted_size[::-1]

            self.statusbar.SetStatusText(size + ' байт', 1)
            if self.list_box.Count == 1:
                self.list_box.Clear()

            self.list_box.Append(self.get_search_results(dlg.GetPath()))

    def get_search_results(self, filename):
        title = 'Файл {0} был обработан {1}:'.format(
            filename, str(datetime.now())[:-7].replace('-', '.')
        )
        result_list = [title]

        with open(filename, 'rt') as f:
            lines = f.readlines()

        pattern = r'\d{2}-\d{2}-\d{4}'
        counter = 0
        for line in lines:
            counter += 1
            result = re.findall(pattern, line)
            if result:
                for each_result in result:
                    result_list += ['Строка {0}, позиция {1} : найдено "{2}"'.format(
                        counter, line.index(each_result), each_result
                    )]

        return result_list + ['']

    def export_log(self, event):
        dlg = wx.FileDialog(self, message='Выберите файл для сохранения',
                            defaultDir='', defaultFile='',
                            wildcard='*.*', style=wx.FLP_OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            with open(dlg.GetPath(), 'w') as f:
                log_strings = [self.list_box.GetString(i)
                               for i in range(self.list_box.Count)]
                for line in log_strings:
                    f.write(line.encode('utf-8') + '\n')

    def add_to_log(self, event):
        with open('script18.log', 'a') as f:
            log_strings = [self.list_box.GetString(i)
                           for i in range(self.list_box.Count)]
            for line in log_strings:
                f.write(line.encode('utf-8') + '\n')

    def show_log(self, event):
        ask_dialog = wx.MessageDialog(self,
            'Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!',
            'Вы уверены?', wx.YES_NO | wx.ICON_QUESTION)
        if ask_dialog.ShowModal() == wx.ID_YES:
            with open('script18.log', 'r') as f:
                log_lines = f.readlines()

            self.list_box.Clear()
            self.list_box.Append(log_lines)


if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    if not os.path.exists('script18.log'):
        wx.MessageBox('Файл лога не найден. Файл будет создан автоматически.',
                      'Файл лога не найден!',
                      wx.OK | wx.ICON_INFORMATION)
        open('script18.log', 'w').close()

    app.MainLoop()

#Complete, unchecked
