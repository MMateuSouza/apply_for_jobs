from . import scheduler
from .models import Password


@scheduler.task("cron", id="check_expired_passwords", minute="*")
def check_expired_passwords():
    Password.delete_expired_passwords()
