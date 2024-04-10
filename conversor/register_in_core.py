def register_in_core(cls):
    _instance: dict = {}
    def decorate(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return decorate