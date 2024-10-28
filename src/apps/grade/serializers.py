def list_serializer(grades):
    result = []

    for grade in grades:
        item = {
            'id': grade['id'],
            'label': grade['label'],
            'isActivate': grade['is_activate']
        }

        result.append(item)

    return result

def show_serializer(grade):
    return {
        'id': grade.id,
        'label': grade.label,
        'isActivate': grade.is_activate
    }