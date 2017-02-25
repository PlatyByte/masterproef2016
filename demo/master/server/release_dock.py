import mysql.connector
import pymysql as pymysql

from dock import Dock
from message import Message
from component import Component
from tower import Tower


class ReleaseDock(Dock):
    def __init__(self, host, port, database_user, database_password, database_host, database_name):
        super(ReleaseDock, self).__init__()
        self.host = host
        self.port = port
        self.database_user = database_user
        self.database_password = database_password
        self.database_host = database_host
        self.database_name = database_name
        self.cursor = None
        self.cnx = None
        self.actions = {}
        self.initiate_actions()

    def start_service(self):
        print("RELEASE DOCK -- Starting services")
        self.connect_to_database()
        thread = super(ReleaseDock, self).start_service()
        print("RELEASE DOCK -- Services started")
        return thread

    def connect_to_database(self):
        print("RELEASE DOCK -- Connecting to database")
        self.cnx = mysql.connector.connect(user=self.database_user, password=self.database_password,
                                           host=self.database_host,
                                           database=self.database_name)
        self.cursor = self.cnx.cursor(dictionary=True)
        print("RELEASE DOCK -- Connected to database")

    def check_database_connection(self):
        sq = "SELECT NOW()"
        try:
            self.cursor.execute(sq)
        except pymysql.Error as e:
            if e.errno == 2006:
                print("RELEASE DOCK -- Something went wrong with the database connection... Reconnecting")
                return self.connect_to_database()
            else:
                print ("RELEASE DOCK -- No connection with database")
                return False

    def connect_to_broker(self, sub_dict):
        print("RELEASE DOCK -- Connecting to Broker")
        super(ReleaseDock, self).connect_to_broker(sub_dict)
        print("RELEASE DOCK -- Subscribed and ready")

    def handle_message(self):
        while True:
            data = self.message_queue.get()
            if Message.check_format(data):
                # Unpack notification
                message = Message.convert_to_message(data)
                relayed_message = message.data
                # Convert to message
                relayed_message = Message.convert_to_message(relayed_message)
                self.actions[relayed_message.message_type](relayed_message)

    def save_new_tower(self, message):
        tower = Tower.convert_to_tower(message.data)
        self.write_tower(tower)

    def change_tower(self, message):
        # TODO
        print message.data

    def initiate_actions(self):
        self.actions["new"] = self.save_new_tower
        self.actions["change"] = self.change_tower

    def write_tower(self, tower):
        try:
            query = "INSERT INTO Tower (name, alias, geolocation, idInCompany, serialNumber) VALUES " \
                    + Tower.to_tuple(tower) + ";"
            self.cursor.execute(query)
            self.cnx.commit()

            for component in tower.components:
                query = "INSERT INTO Component () VALUES " + Component.to_tuple(component) + ";"
                self.cursor.execute()
                self.cnx.commit()
        except:
            self.cnx.rollback()
