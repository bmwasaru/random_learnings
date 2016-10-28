from tornado import gen

from monguo import *

Connection.connect('test_async')


class UserDocument(Document):
    name = StringField(required=True, unique=True, max_length=20)
    email = EmailField(required=True)
    age = IntegerField()
    sex = StringField(candidate=['male', 'female'])

    meta = {
        'collection': 'user'
    }

    @gen.coroutine
    def get_user_list(skip=0, limit=None):
        cursor = UserDocument.find().skip(skip)
        if limit is not None:
            assert isinstance(limit, int) and limit > 0
            cursor.limit(limit)
        user_list = yield cursor.to_list(None)
        raise gen.Return(user_list)


user_id = UserDocument.insert({
    'name': 'Britone Mwasaru',
    'email': 'bmwasaru@gmail.com',
    'sex': 'male'
})

user = UserDocument.find_one({'name': 'Britone Mwasaru'})
