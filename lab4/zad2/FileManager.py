# coding=utf-8
import wx
import xml.etree.ElementTree as ET


class FileManager(object):

    @staticmethod
    def save_author_info(author_info):
        id, name, country, years = author_info
        born_year, death_year = years.split('-')
        xml = '''<?xml version="1.0"?>
        <author>
            <name>''' + name + '''</name>
            <country>''' + country + '''</country>
            <years born="'''+ born_year + '''" died="''' + death_year + '''"/>
        </author>
        '''
        file = open(str(id) + '.xml', 'w')
        file.write(xml.encode('utf-8'))
        file.close()

    @staticmethod
    def load_author_info():
        name, country, years = None, None, None

        dlg = wx.FileDialog(None, message='Выберите файл',
                            defaultDir='', defaultFile='',
                            wildcard='*.*', style=wx.FLP_OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            tree = ET.parse(dlg.GetPath())
            root = tree.getroot()
            for child in root:
                if child.tag == 'name':
                    name = child.text

                if child.tag == 'country':
                    country = child.text

                if child.tag == 'years':
                    years = child.attrib['born'] + '-' + child.attrib['died']

            return (name, country, years)

        return None
