from prettytable import PrettyTable

class subjects:
    def __init__(self, mydb, dbcursor):
        self.mydb = mydb
        self.dbcursor = dbcursor

    def all_subjects(self):
        try:
            fetch_sql = "SELECT code, name FROM subjects"
            self.dbcursor.execute(fetch_sql)

            all_subjects = self.dbcursor.fetchall()

            table = PrettyTable(["Code", "Name"])

            for sub in all_subjects:
                table.add_row(sub)

            table.align["Name"] = "l"

            print(table)

        except Exception as e:
            print("Error while fetching")

    def add_subject(self, code, name):
        try:
            search_query = "SELECT COUNT(*) as total_rows FROM subjects where name = %s"
            self.dbcursor.execute(search_query, (name, ))
            result = self.dbcursor.fetchone()

            if result is not None and result[0] > 0:
                print(f"{name} already exists")
                return

            add_sql = "INSERT INTO subjects (code, name) VALUES (%s, %s)"
            values = (code, name)

            self.dbcursor.execute(add_sql, values)
            self.mydb.commit()
            print(f"{name} added Successfully")
        except Exception as e:
            print(f"Error while adding {name}")

    def lookup_subject(self, code):
        try:
            lookup_sql="SELECT code, name FROM subjects where code = %s"
            self.dbcursor.execute(lookup_sql, (code, ))

            subject = self.dbcursor.fetchone()

            if subjects:
                table = PrettyTable(["CODE", "NAME"])
                table.align["NAME"] = 'l'

                table.add_row(subject)
                print(table)
            else:
                print("No subject found")
        except Exception as e:
            print("Error while looking up subject")

    def delete_subject(self, code):
        try:
            lookup_sql="SELECT code, name FROM subjects where code = %s"
            self.dbcursor.execute(lookup_sql, (code, ))

            subject = self.dbcursor.fetchone()

            if (subject):
                delete_sql="DELETE FROM subjects WHERE code = %s"
                self.dbcursor.execute(delete_sql, (code, ))
                self.mydb.commit()
                print(f"{code} deleted successfully")
            else:
                print("Subject doesn't exists")
        except Exception as e:
            print("Error while deleting")
