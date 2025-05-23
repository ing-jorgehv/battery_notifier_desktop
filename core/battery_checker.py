import psutil



def get_battery_status():
    return psutil.sensors_battery()
