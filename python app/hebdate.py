import hdate
import datetime
def Zmane_hayom():
    c = hdate.Location("פתח תקוה", 32.08707, 34.88747, "Asia/Jerusalem", 54)
    z = hdate.Zmanim(date=datetime.datetime(2023,1,17), location=c, hebrew=True)
    return z