""" This class contains all the watchdog methods. Watched directory will be 'input/' """
# pylint: disable=import-error,no-name-in-module
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from filehandling.fileops import Fileops
from filehandling.filehandling import Filehandling


class Watchdog:
    """ Contains all the file watching methods"""

    @staticmethod
    def on_created(event):
        """ Calls Fileops actions when file is added to the directory"""
        print(f"Hey, {event.src_path} has been created!")
        new_file = event.src_path
        # remove path, return only filename
        filename = new_file.split('/')[-1]
        # call Fileops to perform all specified operations on the file
        Fileops.calculate_file(filename)
        return True

    @staticmethod
    def on_deleted(event):
        """ NOT USED: print(f"Someone deleted {event.src_path}!")"""
        # pylint: disable=unnecessary-pass
        pass

    @staticmethod
    def on_modified(event):
        """ NOT USED: print(f"Hey, {event.src_path} has been modified")"""
        # pylint: disable=unnecessary-pass
        pass

    @staticmethod
    def on_moved(event):
        """ NOT USED: print(f"Someone moved {event.src_path} to {event.dest_path}")"""
        # pylint: disable=unnecessary-pass
        pass

    @staticmethod
    def watch():
        """ This is the watchdog method that monitors the /input directory"""
        patterns = ["*"]
        ign_patterns = None
        ign_dirs = False
        case_sens = True
        my_event_handler = PatternMatchingEventHandler(patterns, ign_patterns, ign_dirs, case_sens)

        my_event_handler.on_created = Watchdog.on_created
        # FOR FUTURE FUNCTIONS: my_event_handler.on_deleted = Watchdog.on_deleted
        # FOR FUTURE FUNCTIONS: my_event_handler.on_modified = Watchdog.on_modified
        # FOR FUTURE FUNCTIONS: my_event_handler.on_moved = Watchdog.on_moved

        path = Filehandling.make_input_directory()
        # directory_path_in = "/home/myusr/input/"
        go_recursively = True
        my_observer = Observer()
        my_observer.schedule(my_event_handler, path, recursive=go_recursively)

        my_observer.start()
        print("WATCHDOG STARTED AND WAITING. Press Ctrl-C to end.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            my_observer.stop()
        my_observer.join()

        return True
