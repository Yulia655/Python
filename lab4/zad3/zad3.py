# coding=utf-8
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey


def dec(string):
    return string.decode('utf-8')


Base = declarative_base()


class Author(Base):
    __tablename__ = dec('Авторы')

    id = Column(Integer, primary_key=True)
    name = Column(String, name=dec('Имя'))
    country = Column(String, name=dec('Страна'))
    years = Column(String, name=dec('Годы_жизни'))

    def __repr__(self):
        return "<Author(id={}, name='{}', country='{}', years='{}')>" \
            .format(self.id, self.name, self.country, self.years)


class Book(Base):
    __tablename__ = dec('Книги')

    author_id = Column(Integer, ForeignKey('Авторы.id'), name=dec('id_автора'))
    title = Column(String, primary_key=True, name=dec('Название'))
    sheets_count = Column(Integer, name=dec('Количество_страниц'))
    publisher = Column(String, name=dec('Издательство'))
    year = Column(Integer, name=dec('Год_издания'))

    def __repr__(self):
        return "<Author(author_id={}, title='{}', sheets_count={}," \
               " publisher='{}', year={})>" \
            .format(self.author_id, self.title, self.sheets_count,
                    self.publisher, self.year)


class User(Base):
    __tablename__ = dec('Пользователи')

    login = Column(String, primary_key=True, name=dec('Логин'))
    password = Column(String, name=dec('Пароль'))

    def __repr__(self):
        return "<User(login='{}', password='{}')>" \
            .format(self.login, self.password)


# -------------------------------TASKS-------------------------------
def task1():
    print 'First task:'
    for author in session.query(Author):
        birth = int(author.years.split('-')[0])
        if birth > 1900 and birth < 1950:
            print author.name

    print ''


def task2():
    print 'Second task:'
    authors = session.query(Author).filter(
        Author.country == dec('Россия') or Author.country == dec('Russia'))
    for author in authors:
        books = session.query(Book).filter(Book.author_id == author.id)
        for book in books:
            print book.title

    print ''


def task3():
    print 'Third task:'
    books = session.query(Book).filter(Book.sheets_count > 200)
    for book in books:
        print book.title

    print ''


def task4():
    print 'Fourth task:'
    for author in session.query(Author):
        books = list(session.query(Book).filter(Book.author_id == author.id))
        if len(books) > 2:
            print author.name


engine = sqlalchemy.create_engine('sqlite:///Library.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

task1()
task2()
task3()
task4()

session.close()

#Complete
