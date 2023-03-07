# We willen in kaart brengen welke dieren we hebben
# Diertabel
# Dier - poten - geluid - voeding
# "Kat" - 4 - "Miauw" - "Vis"
# "Slang" - 0 - "Ssssss" - "Muis"
# "Koe" - 4 - "Boeeee" - "Gras"
# "Hond" - 4 "Bark" - "Brokjes"
# "Muis" - 4 - "Piep" - "Kaas"
# "Vogel" - 2 "Tjilp" - "Zaadjes"

# Voor voedel willen we extra informatie over de voeding
# Voedseltabel
# Voedsel - Kiloprijs - Vegetarisch
# "Vis" - 5 - False
# "Muis" - 4 - Flase
# "Gras" - 2 - True
# "Brokjes" - 6 - False
# "Kaas" - 15 - True
# "Zaadjes" - 2 - True

from peewee import Model, SqliteDatabase, CharField, ForeignKeyField, AutoField

db = SqliteDatabase("zoo.db")

class BaseModel(Model):
    class Meta:
        database = db


class ZooKeeper(BaseModel):
    # id = AutoField()
    name = CharField()


class Enclosure(BaseModel):
    # id = AutoField()
    name = CharField()
    feeder = ForeignKeyField(ZooKeeper, backref = "enclosures_to_feed")


class Animal(BaseModel):
    # id = AutoField()
    name = CharField()
    type = CharField()
    enclosure = ForeignKeyField(Enclosure, backref = "inhabitants")


