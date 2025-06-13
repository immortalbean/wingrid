import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def asset_path(*paths):
    path = os.path.join(BASEDIR, *paths)
    return path

