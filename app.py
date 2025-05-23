import time
import threading
from ui.tray import TrayApp
from core.battery_monitor import start_monitoring



def main():
    stop_event = threading.Event()

    # Start a monitoring in a separated thread
    monitor_thread = threading.Thread(target=start_monitoring, args=(stop_event,), daemon=True)
    monitor_thread.start()

    # Run system tray in background & pass monitor_thread for a clean stop
    tray = TrayApp(stop_event, monitor_thread)
    tray.run()
    
    try:
        while not stop_event.is_set():
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by the user's keyboard.")
        stop_event.set()
        tray.icon.stop()
        monitor_thread.join()



if __name__ == "__main__":
    main()
