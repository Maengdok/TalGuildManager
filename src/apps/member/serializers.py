def list_serializer(members):
    result = []
    
    print('list_serializer')
    for member in members:
        item = {
            'id': member.id,
            'username': member.username,
            'grade': {
                'id': member.grade.id,
                'label': member.grade.label,
            },
            'weapon': {
                'id': member.weapon.id,
                'label': member.weapon.label,
            },
            'combatType': {
                'id': member.combat_type.id,
                'label': member.combat_type.label,
            },
            'addedAt': member.added_at,
            'isActivate': member.is_activate
        }

        result.append(item)

    return result

def show_serializer(member):
    return {
        'id': member.id,
        'username': member.username,
        'grade': {
            'id': member.grade.id,
            'label': member.grade.label
        },
        'weapon': {
                'id': member.weapon.id,
                'label': member.weapon.label,
        },
        'combatType': {
                'id': member.combat_type.id,
                'label': member.combat_type.label,
        },
        'addedAt': member.added_at.strftime('%Y-%m-%d') if member.added_at else "",
        'removedAt': member.removed_at.strftime('%Y-%m-%d') if member.removed_at else "",
        'isOnDiscord': member.is_on_discord,
        'isActive': member.is_active,
        'hasPrivilege': member.has_privilege,
        'isActivate': member.is_activate,
    }