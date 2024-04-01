import re


# Přijímá hesla o délce 8-16 znaků, obsahující alespoň jedno velké písmeno, jedno číslo a jeden speciální znak.
def validate_password(password):
    return re.search(r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[a-zA-Z\d@$!%*?&]{8,16}$", password) is not None
    # nejdřív zjistí výskyt velkých písmen, číslic a special znaků, pak matchne délku hesla
