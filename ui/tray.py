import os
import sys
import codecs
from pystray import Icon, Menu, MenuItem
from PIL import Image



# Safe UTF-8 output redirection for production (when creating .exe file) to avoid errors
try:
    # Change the codification of the output terminal to UTF-8
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
except (AttributeError, ValueError):
    pass  # Happens when running with PyInstaller and --noconsole





class TrayApp:
    def __init__(self, stop_event, monitor_thread):
        self.icon = Icon("Battery Monitor")
        self.stop_event = stop_event
        self.monitor_thread = monitor_thread


    def setup(self):
        icon_path = self.resource_path("assets/battery_icon.ico")
        try:
            image = Image.open(icon_path)
        except Exception as e:
            raise RuntimeError(f"Failed to load tray icon image: {e}")
        
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


    @staticmethod  
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
