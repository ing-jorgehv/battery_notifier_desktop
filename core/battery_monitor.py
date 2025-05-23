import sys
import codecs
import logging
from threading import Thread
from core.battery_checker import get_battery_status
from core.notifier import notify_battery_low, notify_battery_not_found
from ui.alert_window import show_battery_full_alert



# Change the codification of the output terminal to UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())



CHECK_INTERVAL = 120  # seconds
logging.basicConfig(level=logging.INFO)





def start_monitoring(stop_event):
    full_notification = False
    empty_notification = False

    while not stop_event.is_set():
        battery = get_battery_status()

        if battery is None:
            logging.warning("No battery found.")
            notify_battery_not_found()
            break

        percent = battery.percent
        plugged = battery.power_plugged

        if percent >= 100 and plugged:
            if not full_notification:
                Thread(target=show_battery_full_alert).start()
                full_notification = True
        else:
            full_notification = False

        if percent <= 21 and not plugged:
            if not empty_notification:
                notify_battery_low()
                empty_notification = True
        else:
            empty_notification = False

        stop_event.wait(CHECK_INTERVAL)
    
    print('🛑 Stopping monitoring...')
        