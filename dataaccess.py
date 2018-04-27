import MySQLdb


class DataAccess():

    def __init__(self, conf):
        self.conf = conf
        self.server = self.conf["db"]["server"]
        self.user = self.conf["db"]["user"]
        self.password = self.conf["db"]["password"]
        self.database = self.conf["db"]["database"]
    
    def select_row(self, query):
        result = []

        db = MySQLdb.connect(self.server, self.user, self.password, self.database)
        cursor = db.cursor()
        cursor.execute(query)
        
        column_names = [i[0] for i in cursor.description]
        rows = cursor.fetchall()
        for row in rows:
            result.append(dict(zip(column_names, row)))
        db.close()
        return result