from plyer import battery


def getBatteryStt():
    status = battery.get_state()
    return status