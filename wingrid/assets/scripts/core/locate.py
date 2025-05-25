import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def asset_path(*paths):
    return os.path.join(BASEDIR, *paths)