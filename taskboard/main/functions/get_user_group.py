"""файл с функцией для определения грыппу пользователя"""
def get_user_group(user):
    """функция для определения группы пользователя"""
    if user.is_superuser:
        return "superuser"
    elif user.groups.filter(name = "L1").exists():
        return "L1"
    elif user.groups.filter(name = "L2").exists():
        return "L2"
    else:
        return "L3"
