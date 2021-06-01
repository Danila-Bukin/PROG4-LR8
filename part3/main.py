from orator import DatabaseManager
from orator import Model

config = {
    'sqlite': {
        'driver': 'sqlite',
        'database': 'Chinook_Sqlite.sqlite'
    }
}

db = DatabaseManager(config)

Model.set_connection_resolver(db)


class Artist(Model):
    __table__ = 'Artist'
    __primary_key__ = 'ArtistId'
    __timestamps__ = False


# Получение одиночной записи
artist = Artist.find(1)
print(artist.ArtistId, artist.Name)

# Получение модели по ключу или выброс исключения
model = Artist.find_or_fail(2)
print(model.ArtistId, model.Name)

# Запрос с условием
artists = Artist.where('ArtistId', '>', 100).take(10).get()
for artist in artists:
    print(artist.Name)

# Счётчик количества записей по условию
count = Artist.where('Name', '>', 'S').count()
print(count)

# Параметризация запроса
artists = Artist.where_raw('ArtistId < ?', [25]).get()

# Вставка
new_artist = Artist()
new_artist.Name = "Thalía"
new_artist.save()
print(new_artist.ArtistId)

# Обновление
artist_upd = Artist.find(4)
artist_upd.Name = 'Gloria Estefan'
artist_upd.save()

# Удаление
artist_del = Artist.find(53)
artist_del.delete()
