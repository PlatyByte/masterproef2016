import gettext

from SimpleUI import MyApp
from field_dock import FieldDock


def start_field_dock():
    print("FIELD DOCK -- initialisation")
    field_dock = FieldDock('localhost', 54321)
    return field_dock.start_service()


def connect_to_broker():
    print("FIELD DOCK -- Connecting to Broker")


def start_gui():
    gettext.install("app")  # replace with the appropriate catalog name
    app = MyApp(0)
    app.MainLoop()


def main():
    field_dock_thread = start_field_dock()
    connect_to_broker()
    start_gui()

    # Waiting until threads are finished
    field_dock_thread.join()

if __name__ == "__main__":
    main()