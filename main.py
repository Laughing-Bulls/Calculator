""" This is a script to run the Python calculator"""
from filehandling.watcher import Watchdog
from csvmanager.make_table import Table


def main():
    """ Run the calculator program"""

    print("Calculator program is running. Monitoring for new input files to calculate...")

    Table.create_fake_users(20)
    # Watchdog.watch()

    print("That's all, Folks!")


if __name__ == "__main__":
    main()
