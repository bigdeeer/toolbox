import os
import sys

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Define a custom event handler
class MyFileSystemEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        # Print the event type and the path of the file/directory
        print(f"Event Type: {event.event_type}  Path: {event.src_path}")


# Create an observer and attach the event handler
observer = Observer()
event_handler = MyFileSystemEventHandler()
# get current using py env path
site_packages_dir = os.path.join(sys.prefix, 'site-packages')
print(site_packages_dir)
observer.schedule(event_handler, path='D:/YoungWired_venv/Lib/', recursive=True)

# Start the observer
observer.start()

try:
    # Keep the observer running until interrupted
    while True:
        pass
except KeyboardInterrupt:
    # Stop the observer when interrupted
    observer.stop()

# Wait until the observer thread completes
observer.join()
