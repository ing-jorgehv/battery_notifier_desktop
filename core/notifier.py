from plyer import notification



def notify_battery_low():
    notification.notify(
        title="🪫 Battery at 20%",
        message="Your battery is almost empty. Plug the charger.",
        timeout=30 # seconds
    )


def notify_battery_not_found():
    notification.notify(
        title="No battery found.",
        message="No battery was found in the system.",
        timeout=30
    )
