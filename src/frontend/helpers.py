"""
Solução encontrada em: https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
"""
from datetime import date, datetime


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))
