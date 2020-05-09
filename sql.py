import sqlite3
def get_name(code):
	k=[]
	conn=sqlite3.connect('train.db')
	#name=conn.execute('SELECT title from station_info where station_code=?',(code,))
	name=conn.execute('SELECT * FROM station_info where title like ?',(code,))
	for i in name:
		print(i)
		k.append(i)
	conn.close()
	return k
an=get_name('Per%')
#print(an)