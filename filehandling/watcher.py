""" This class contains all the filehandling methods. Directories will be 'input' and 'output' """
import pandas as pd
# pip install watchdog
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler

# Use Pandas library with alias pd for file actions

from filehandling.filehandling import Filehandling
import os


class Filehandling:
    """ Contains all the filehandling methods"""

    directory_path_in = "/home/myusr/input/"
    directory_path_out = "/home/myusr/output/"

    @staticmethod
    def monitor_directory():
        """ Return an alert if file is added to the directory"""
        pass

    def on_created(event):
        print(f"hey, {event.src_path} has been created!")

        def on_deleted(event):
            print(f"what the f**k! Someone deleted {event.src_path}!")

        def on_modified(event):
            print(f"hey buddy, {event.src_path} has been modified")

    def on_moved(event):
        print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    path = "."
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    print("STARTED AND WAITING")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
