

from exportd import exportd
from printd import printd

def quest(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None 