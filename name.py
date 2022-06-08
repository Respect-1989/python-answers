def get_full_name(ism,familyasi,otasi=''):
    if otasi:
        return f"{ism} {otasi} {familyasi}".title()
    else:
        return f"{ism} {familyasi}".title()
