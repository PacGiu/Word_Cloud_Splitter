def flatten(pool):
    res = []
    for v in pool:
        if isinstance(v, list):
            res += flatten(v)
        else:
            res.append(v)
    return res 