import datetime
from uuid import uuid4

def generate_image_id():
    now = datetime.datetime.now()
    return "IMG" + str(now.year) + '%02d' % now.month + '%02d' % now.day + \
        str(uuid4().int)[:5] 