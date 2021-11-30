""" This class contains all the watchdog methods. Watched directory will be 'input/' """
# import pandas as pd
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


class Watchdog:
    """ Contains all the file watching methods"""

    directory_path_in = "/home/myusr/input/"
    directory_path_out = "/home/myusr/output/"
    new_file = ""

    @staticmethod
    def monitor_directory():
        """ Return an alert if file is added to the directory"""
        pass

    @staticmethod
    def on_created(event):
        print(f"Hey, {event.src_path} has been created!")
        Watchdog.new_file = event.src_path

    @staticmethod
    def on_deleted(event):
        """ NOT USED: print(f"Someone deleted {event.src_path}!")"""
        pass

    @staticmethod
    def on_modified(event):
        """ NOT USED: print(f"Hey, {event.src_path} has been modified")"""
        pass

    @staticmethod
    def on_moved(event):
        """ NOT USED: print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")"""
        pass

    @staticmethod
    def watch():
        patterns = ["*"]
        ignore_patterns = None
        ignore_directories = False
        case_sensitive = True
        my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

        my_event_handler.on_created = Watchdog.on_created
        # my_event_handler.on_deleted = Watchdog.on_deleted
        # my_event_handler.on_modified = Watchdog.on_modified
        # my_event_handler.on_moved = Watchdog.on_moved

        path = Filehandling.make_input_directory()
        # path = "."
        # print(path)
        go_recursively = True
        my_observer = Observer()
        my_observer.schedule(my_event_handler, path, recursive=go_recursively)

        my_observer.start()
        print("WATCHDOG STARTED AND WAITING")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            my_observer.stop()
        my_observer.join()

        # remove path, return only filename
        filename = Watchdog.new_file.split('/')[-1]
        return filename

