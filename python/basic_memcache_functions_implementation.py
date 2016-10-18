CACHE = {}


def set(key, value):
    """return true after setting the data"""
    CACHE[key] = value
    return True


def get(key):
    """return value for the key"""
    return CACHE.get(key)


def delete(key):
    """delete key from cache"""
    if key in CACHE:
        del CACHE[key]


def flush():
    """clear the entire cache"""
    CACHE.clear()

print(set('name', 'Britone Mwasaru'))
print(get('name'))
print(delete('name'))
print(get('name'))
