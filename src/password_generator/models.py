from mongoengine import Document, signals, StringField

import uuid


class Password(Document):
    pk = StringField(max_length=36, primary_key=True,
                     default=str(uuid.uuid4()))

    @classmethod
    def check_password_visualization_limit(sender, document):
        pass


signals.post_save.connect(Password.check_password_visualization_limit)
