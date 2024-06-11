import sys
import os
import time
import shutil
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/username/Desktop/from'
to_dir = 'C:/Users/username/Desktop/to'




class FileMovementHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        print(f"Hey, {event.src_path} has been modified!")
    
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Hey, {event.src_path} has been deleted!")

    def on_moved(self, event):
        print(f"Hey, {event.src_path} has been moved to {event.dest_path}!")

    event_handler = FileMovementHandler()

    Observer = Observer()

    observer.schedule(event_handler, from_dir, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(2) 
            print('running....')
    except KeyboardInterrupt:
        print("Stopped")
        observer.stop()