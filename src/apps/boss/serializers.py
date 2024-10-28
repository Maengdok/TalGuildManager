def list_serializer(bosss):
    result = []

    for boss in bosss:
        item = {
            'id': boss['id'],
            'label': boss['label'],
            'isActivate': boss['is_activate']
        }

        result.append(item)

    return result

def show_serializer(boss):
    return {
        'id': boss.id,
        'label': boss.label,
        'isActivate': boss.is_activate
    }