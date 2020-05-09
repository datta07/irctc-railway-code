import requests
from datetime import datetime
print('Date\t\tCLX\t\tTEL\t\tTEL\t\tSC\t\tSITUATION\t\t\t\tgap')
print('---'*35)
dates=['1','09','2019']
#input()
while True:
	if (dates[0]=='31'):
		dates[0]='1'
		dates[1]='10'
		continue
	if (dates[1]=='10')&(dates[0]=='4'):
		break

	date='-'.join(dates)
	print(date,end='\t')
	try:
		k=requests.get('https://whereismytrain.in/cache/live_status?date='+date+'&appVersion=6.1.3&from_day=1&wid=1572804407&train_no=12709&cellinfo=null&from=CLX&to=TEL&lang=en&user=null&sb_version=0&qid=null')
		k=k.json()
		k=k['days_schedule']
	except Exception:
		dates[0]=str(int(dates[0])+1)
		print('\n'+'---'*35)
		continue
	for i in k:
		if (i['station_code']=='CLX'):
			print(i['actual_arrival_time'],end='\t')
		if (i['station_code']=='TEL'):
			print(i['actual_arrival_time'],end='\t')
			k1=i['actual_arrival_time'].split(':')
	k=requests.get('https://whereismytrain.in/cache/live_status?date='+date+'&appVersion=6.1.3&from_day=1&wid=1572804407&train_no=17626&cellinfo=null&from=RAL&to=SC&lang=en&user=null&sb_version=0&qid=null')
	k=k.json()
	k=k['days_schedule']
	for i in k:
		if (i['station_code']=='TEL'):
			print(i['actual_arrival_time'],end='\t')
			k2=i['actual_arrival_time'].split(':')
		if (i['station_code']=='SC'):
			print(i['actual_arrival_time'],end='\t')
	dates[0]=str(int(dates[0])+1)
	t1=0
	if (k2[0]>k1[0]):
		print('can catch the train    ',end='\t')
	elif (k2[0]==k1[0]):
		if (k1[1]<k2[1]):
			print('can catch the train    ',end='\t')
		else:
			print('!!!!HURRY-no train!!!!',end='\t')
	else:
		print('!!!!HURRY-no train!!!!',end='\t')
	k1=':'.join(k1)
	k2=':'.join(k2)
	gap=datetime.strptime(k2,"%H:%M")-datetime.strptime(k1,"%H:%M")
	print(gap)
	print('---'*35)

