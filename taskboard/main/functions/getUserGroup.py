def getUserGroup(user):
    if user.is_superuser:
        return "superuser"
    elif user.groups.filter(name = "L1").exists():
        return "L1"
    elif user.groups.filter(name = "L2").exists():
        return "L2"
    else:
        return "L3"