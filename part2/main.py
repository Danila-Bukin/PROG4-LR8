from peewee import *

# Создаем соединение с нашей базой данных
conn = SqliteDatabase('Chinook_Sqlite.sqlite')


# Шаблон запроса
def print_last_five_artists():
    """ Печатаем последние 5 записей в таблице испольнителей"""
    print('#######################################################')
    cur_query = Artist.select().limit(5).order_by(Artist.artist_id.desc())
    for item in cur_query.dicts().execute():
        print('artist: ', item)


# Определяем базовую модель о которой будут наследоваться остальные
class BaseModel(Model):
    class Meta:
        database = conn  # соединение с базой, из шаблона выше


# Определяем модель исполнителя
class Artist(BaseModel):
    artist_id = AutoField(column_name='ArtistId')
    name = TextField(column_name='Name', null=True)

    class Meta:
        table_name = 'Artist'


# Создаем курсор - специальный объект для запросов и получения данных с базы
cursor = conn.cursor()

# Получение одиночной записи
artist = Artist.get(Artist.artist_id == 1)
print('artist: ', artist.artist_id, artist.name)

# Получение набора записей
query = Artist.select()
print(query)
# SELECT "t1"."ArtistId", "t1"."Name" FROM "Artist" AS "t1"

query = Artist.select().where(Artist.artist_id < 10).limit(5).order_by(Artist.artist_id.desc())
print(query)
# SELECT "t1"."ArtistId", "t1"."Name" FROM "Artist" AS "t1"
# WHERE ("t1"."ArtistId" < 10) ORDER BY "t1"."ArtistId" DESC LIMIT 5

# Ответ в виде словаря
artists_selected = query.dicts().execute()
for artist in artists_selected:
    print('artist: ', artist)

# Создание записи
# Первый способ: Model.create() — передаем все требуемые параметры сразу
Artist.create(name='1-Qwerty')

# Второй способ: Мы создаем объект класса нашей модели, работаем в коде в содержимым его полей,
# а в конце вызываем его метод .save()
artist = Artist(name='2-asdfg')
artist.save()

# Третий способ — массовое добавление из коллекции методом модели Model.insert_many()
artists_data = [{'name': '3-qaswed'}, {'name': '4-yhnbgt'}]
Artist.insert_many(artists_data).execute()

# Визуализируем последние 5 записей в таблице исполнителей
print_last_five_artists()

# Обновление записей
# 1 способ
artist = Artist(name='2-asdfg+++++')
artist.artist_id = 277  # Первичный ключ
artist.save()

# Обновление многих записей сразу
query = Artist.update(name=Artist.name + '!!!').where(Artist.artist_id > 275)
query.execute()
print_last_five_artists()

# Удаление записей
# Первый способ
artist = Artist.get(Artist.artist_id == 279)
artist.delete_instance()

# Удаление набора строк
query = Artist.delete().where(Artist.artist_id > 275)
query.execute()
print_last_five_artists()

# Закрываем соединение с базой данных
conn.close()
