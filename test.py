import itertools
import sys
import MySQLdb

class Database:

    host = 'localhost'
    user = 'root'
    password = 'nvidia123'
    db = 'nvidia'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()
        print "connection made"
        print self.connection

    def insert(self, query):
        print query
        try:
            self.cursor.execute(query)
            print 'inserted'
            self.connection.commit()
        except:

            print "-----------------Inserted Successfully--------------------"
            # print update
            self.connection.rollback()

    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

if __name__ == "__main__":
    db = Database()
    mac = ''
    ip = ''
    # CleanUp Operation
    # del_query = "DELETE FROM basic_python_database"
    #db.insert(del_query)

    # Data Insert into the table
    sql = "insert into machines values('10.24.142.45','root','nvidia123')"
    db.insert(sql)


    #Data retrieved from the table
    select_query = "select version()"
    #
    people = db.query(select_query)
    #
    for person in people:
        print person['machine_ip']+"  "+person['machine_uname']+"  "+person['machine_passwd']
    # for person in people:
    #     print person['version()']
# x= list()
#
# # mydict = dict()
#
# for row in csv_f:
#     x.append(row)
#
# # columns =  len(x[0])
# # rows = len(x)
#
# print mydict
#
# # for i in range(0, columns):
# #     for j in range(0,rows):
# #         mydict[rows] = rows
# #         print mydict
#
# # for val in mydict.items():
# #     print val
#
#
# # import csv, sys
# # filename = 'new.csv'
# # with open(filename) as f:
# #     reader = csv.reader(f)
# #     try:
# #         for row in reader:
# #             print(row)
# #             print columns
# #     except csv.Error as e:
# #         sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))