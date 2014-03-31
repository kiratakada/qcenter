import os

from django.conf import settings

def create_dir_if_not_exists(dir):
    os.umask(0002)
    d = os.path.dirname(dir)

    if not os.path.exists(d):
        os.makedirs(d, 0775)
        return True

    return False

def handle_uploaded_file(f=None, path=None):
    path = '%s/%s/' % (settings.IMAGE_ROOT, path)

    create_dir_if_not_exists(path)

    fp = open(os.path.join(path, f.name), 'wb')
    for chunk in f.chunks():
        fp.write(chunk)
    fp.close()


def day_to_int(day=None):

    if str(day) == 'Monday': return 1
    if str(day) == 'Tuesday': return 2
    if str(day) == 'Wednesday': return 3
    if str(day) == 'Thursday': return 4
    if str(day) == 'Friday': return 5
    if str(day) == 'Saturday': return 6
    if str(day) == 'Sunday': return 7
