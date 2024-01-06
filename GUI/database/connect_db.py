import sqlite3
import os

class LicensePlateDatabase:
    def __init__(self, direktori_path='D:/python/LicensePlateDetector/GUI/database', database_name='license_plate.db'):
        self.database_path = os.path.join(direktori_path, database_name)
        self.conn = sqlite3.connect(self.database_path)
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS LICENSE_PLATES
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            FILENAME TEXT NOT NULL,
                            PLATE_PREDICTION TEXT NOT NULL,
                            FILEPATH CHAR(50));''')
        self.conn.commit()

    def insert_record(self, filename, plate_prediction, filepath):
        query = '''INSERT INTO LICENSE_PLATES (FILENAME, PLATE_PREDICTION, FILEPATH)
                   VALUES (?, ?, ?)'''
        values = (filename, plate_prediction, filepath)
        self.conn.execute(query, values)
        self.conn.commit()

    def update_record(self, record_id, filename, plate_prediction, filepath):
        query = '''UPDATE LICENSE_PLATES
                   SET FILENAME=?, PLATE_PREDICTION=?, FILEPATH=?
                   WHERE ID=?'''
        values = (filename, plate_prediction, filepath, record_id)
        self.conn.execute(query, values)
        self.conn.commit()

    def delete_record(self, record_id):
        query = 'DELETE FROM LICENSE_PLATES WHERE ID=?'
        self.conn.execute(query, (record_id,))
        self.conn.commit()
        
    # -------------------------- GET DATA ----------------------------- #
        
    def get_filepath_list(self):
        query = 'SELECT FILEPATH FROM LICENSE_PLATES'
        result = self.conn.execute(query).fetchall()

        filepath_list = [row[0] for row in result] if result else []
        return filepath_list
    
    def get_file_name(self):
        query = 'SELECT FILENAME FROM LICENSE_PLATES'
        result = self.conn.execute(query).fetchall()

        filepath_list = [row[0] for row in result] if result else []
        return filepath_list
    
    def get_file_predict(self):
        query = 'SELECT PLATE_PREDICTION FROM LICENSE_PLATES'
        result = self.conn.execute(query).fetchall()

        filepath_list = [row[0] for row in result] if result else []
        return filepath_list
    
     # ---------------------------------------------------------------- #


    def close_connection(self):
        self.conn.close()

