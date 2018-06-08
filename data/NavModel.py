from data import BaseDB


class NavModel(BaseDB.BaseDB):

    def insert_item(self, nav):
        self.cursor.execute('''
            INSERT INTO NAV (ITEM)
            VALUES ("%s")''' % nav)
        self.conn.commit()

    def select_all(self):
        select = self.cursor.execute('''SELECT item FROM NAV''')
        result = []
        for row in select:
            result.append(row[0])
        return result

    def delete_item(self, nav):
        try:
            self.cursor.execute('''DELETE FROM NAV where nav="%s"''' % nav)
            self.conn.commit()
            return True
        finally:
            return False
