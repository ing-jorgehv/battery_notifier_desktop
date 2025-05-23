import sys
import codecs
from pystray import Icon, Menu, MenuItem
from PIL import Image



# Change the codification of the output terminal to UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())





class TrayApp:
    def __init__(self, stop_event, monitor_thread):
        self.icon = Icon("Battery Monitor")
        self.stop_event = stop_event
        self.monitor_thread = monitor_thread


    def setup(self):
        image = Image.open("assets/battery_icon.ico")
        self.icon.icon = image
        self.icon.title = "Battery Monitor is running"
        self.icon.menu = Menu (
            MenuItem("Quit", self.exit_app)
        )

    def run(self):
        self.setup()
        self.icon.run_detached() # run in the background
    
    def exit_app(self):
        print('🛑 Stopping Tray app...')
        self.stop_event.set() # Trigger to stop monitoring
        self.icon.stop() # Stop tray icon
        self.monitor_thread.join()
        try:
            sys.exit(0) # Finish python process
        except SystemExit:
            pass # Avoid pystray register the exit as error
