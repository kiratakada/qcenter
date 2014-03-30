import os

from django.conf import settings

def create_dir_if_not_exists(dir):
    os.umask(0002)
    d = os.path.dirname(dir)

    if not os.path.exists(d):
        os.makedirs(d, 0775)
        #os.chmod(dir, 0775)
        return True

    #os.chmod(dir, 0775)
    return False

def handle_uploaded_file(f):
    path = settings.IMAGE_ROOT+'user/'

    create_dir_if_not_exists(path)

    fp = open(os.path.join(path, f.name), 'wb')
    for chunk in f.chunks():
        fp.write(chunk)
    fp.close()
