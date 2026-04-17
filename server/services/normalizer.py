from config.keywords import normalization_map

def normalizer(token):
    return normalization_map.get(token, token)