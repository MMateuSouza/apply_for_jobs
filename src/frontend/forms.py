from datetime import datetime
from wtforms import BooleanField, DateTimeLocalField, Form, IntegerField, StringField
from wtforms.validators import InputRequired, NumberRange, ValidationError


def check_datetime_lte_now(form, field):
    if field.data <= datetime.now():
        raise ValidationError("Data e Hora para Expiração precisa ser maior que o momento atual")


class PasswordForm(Form):
    description = StringField(id="description", name="description", label="Descrição da Senha", validators=[InputRequired("Descrição é um campo obrigatório")])
    expires_at = DateTimeLocalField(id="expires_at", name="expires_at", label="Data e Hora para Expiração", validators=[InputRequired("Data e Hora para Expiração é um campo obrigatório"), check_datetime_lte_now], format='%Y-%m-%dT%H:%M')
    max_value_for_viewing = IntegerField(id="max_value_for_viewing", name="max_value_for_viewing", label="Quantidade Máxima de Visualizações", validators=[InputRequired("Quantidade Máxima de Visualizações é um campo obrigatório"), NumberRange(min=1)])
    length = IntegerField(id="length", name="length", label="Comprimento da Senha", validators=[InputRequired("Comprimento da Senha é um campo obrigatório"), NumberRange(min=1)])
    allow_numbers = BooleanField(id="allow_numbers", name="allow_numbers", label="Permitir Números")
    allow_special_characters = BooleanField(id="allow_special_characters", name="allow_special_characters", label="Permitir Caracteres Especiais")
    allow_letters = BooleanField(id="allow_letters", name="allow_letters", label="Permitir Letras")
    allow_uppercase_letters = BooleanField(id="allow_uppercase_letters", name="allow_uppercase_letters", label="Maiúsculas")
    allow_lowercase_letters = BooleanField(id="allow_lowercase_letters", name="allow_lowercase_letters", label="Minúsculas")
