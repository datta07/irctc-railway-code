import requests
from sql import get_name
def pnr(n):
  r=requests.get('https://pnrhtml.railyatri.in/api/v2/pnr/journey/'+str(n)+'/null/null/null/null/null.json')
  k=r.json()
  status=k['status']
  if (status=='OK'):
    print(k['pnr_number'],end='   ')
    print(get_name(k['board_from']),get_name(k['board_to']),k['class'],k['travel_date'],k['train_name'])
  else:
    print('not booked')

for i  in range(0,100):
  if (i<10):
    pnr('461016210'+str(i))
  else:
    pnr('46101621'+str(i))


'''
#an=get_name('clx')
#print(an)
date='04-10-2019'
k=requests.get('https://whereismytrain.in/cache/live_status?date='+date+'&appVersion=6.1.3&from_day=1&wid=1572804407&train_no=12709&cellinfo=null&from=MAS&to=SC&lang=en&user=null&sb_version=0&qid=null')
k=k.json()

for i in k:
  print(i,k[i])
  print('----'*35)

cur_code=k['curStn']
cur=get_name(k['curStn'])
is_crossed=k['departedCurStn']
updated_on=k['lastUpdated']
dis=k['distance']
near_dis=k['curStnDistance']
print(cur)
print(updated_on)
k=k['days_schedule']
l=[]
prev=k[0]
no=0
for i in k:
  if (i['station_code']==cur_code):
    print(get_name(prev['station_code']),'>>','*'+cur,'>>',get_name(k[no+1]['station_code']),end='')
    no+=1
    l.append(i)
    while True:
      if (k[no]['station_code']=='TEL'):
        print('')
        print(str(round(near_dis,2))+' kms','from the',cur)
        break
      no+=1
      print('>>',get_name(k[no]['station_code']),end='')
    #t1=prev[]
    print('---'*35)
    print(cur_code,'\t',i['sch_arrival_time'],'\t',i['actual_arrival_time'],'\t','Nope ','\t',str(round(i['distance']-dis,2))+' kms')
    print('---'*35)
  if (i['station_code']=='CLX'):
    print('CLX','\t',i['sch_arrival_time'],'\t',i['actual_arrival_time'],'\t',i['non_agg_arrival_time'],'\t',str(round(i['distance']-dis,2))+' kms')
    l.append(i)
    print('---'*35)
  if (i['station_code']=='TEL'):
    print('TEL','\t',i['sch_arrival_time'],'\t',i['actual_arrival_time'],'\t',i['non_agg_arrival_time'],'\t',str(round(i['distance']-dis,2))+' kms')
    l.append(i)
    print('---'*35)
  prev=i
  no+=1
print(l[0])
print('---'*35)
print(l[1])'''
