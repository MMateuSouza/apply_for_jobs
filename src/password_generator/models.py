from datetime import datetime
from mongoengine import DateTimeField, Document, IntField, signals, StringField

from .helpers import handler, PasswordGenerator

import uuid


@handler(signals.post_save)
def validate_view_limit(sender, document, **kwargs):
    # Verifica se a senha atingiu o limite de visualizações
    # Se sim, deletar.
    if document.performed_views >= document.max_value_for_viewing:
        document.delete()


@validate_view_limit.apply
class Password(Document):
    id = StringField(max_length=36, primary_key=True, default=str(uuid.uuid4()))
    description = StringField(required=True)
    password = StringField(required=True)
    performed_views = IntField(min_value=0, default=0)
    max_value_for_viewing = IntField(min_value=0, required=True)
    created_at = DateTimeField(default=datetime.now())
    expires_at = DateTimeField(required=True)

    def __init__(self, *args, **values):
        super().__init__(*args, **values)

    def set_password(self, **kwargs):
        self.password = PasswordGenerator.generate(**kwargs)

    def visualize(self):
        self.performed_views += 1
        self.save()
