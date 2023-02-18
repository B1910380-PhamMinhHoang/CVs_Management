class Folder:
    def __init__(self, id, alias, name):
        self.id = id
        self.alias = alias
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'alias': self.alias,
            'name': self.name
        }

    @classmethod
    def from_json(cls, json):
        id = None if ('id' not in json) else json['id']

        return Folder(id, json['alias'], json['name'])