import pymysql as mysql
def ConnectionPool():
    db=mysql.connect(host="localhost", port=3306,user="root",password="Vishal@07",db="mm")
    cmd=db.cursor()
    return(db,cmd)
