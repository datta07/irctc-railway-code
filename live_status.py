###############################################################
#                       garuda.inc                            #
###############################################################
# Author : Akula Guru Datta
# Date   : 15-09-2019

import sqlite3
import requests

class train:
  def __init__(self,train_no,date,source,dest):
    self.date=date
    self.train_no=train_no
    self.src=source
    self.dest=dest
    self.updated=False

  # returns title,station_code
  def get_name_sql(self,wish,key,value):
    conn=sqlite3.connect('train.db')
    name=conn.execute('SELECT '+wish+' FROM station_info where '+key+'=?',(value,))
    for i in name:
      k=i[0]
    conn.close()
    return k

  def update_info(self):
    k=requests.get('https://whereismytrain.in/cache/live_status?date='+self.date+'&appVersion=6.1.3&from_day=1&wid=1572804407&train_no='+self.train_no+'&cellinfo=null&from='+self.src+'&to='+self.dest+'&lang=en&user=null&sb_version=0&qid=null')
    k=k.json()
    #print(k)
    self.curStn=k['curStn']
    self.departedCurStn=k['departedCurStn']
    self.lastUpdated=k['lastUpdated']
    self.distance=k['distance']
    self.curStnDistance=k['curStnDistance']
    self.updated=True
    self.index=0
    k=k['days_schedule']
    no=0
    self.stations=[]
    self.stationsInfo={}
    unwanted=['actual_arrival_tm','updated_at','delay_in_departure','delay_in_arrival','platform','lng','station_code','stops','gtfs_sno','actual_departure_tm','lat','sno','platform_info','non_agg_arrival_tm','non_agg_departure_tm']
    for i in k:
      if (i['station_code']==self.src):
        self.srcPos=no
      if (i['station_code']==self.dest):
        self.destPos=no
      if (i['station_code']==self.curStn):
        if (i['stops']):
          self.curPos=no
        else:
          self.curPos=no*-1
      no+=1
      self.stations.append(i['station_code'])
      self.stationsInfo[i['station_code']]=i
      self.stationsInfo[i['station_code']]['name']=self.get_name_sql('title','station_code',i['station_code'],)
      self.stationsInfo[i['station_code']]={j:self.stationsInfo[i['station_code']][j] for j in self.stationsInfo[i['station_code']] if j not in unwanted}



  def showCurMap(self):
    if not self.updated:
      self.update_info()

    pt=True
    if (self.curPos<0):
      self.curPos=self.curPos*-1
      pt=False

    arr=[self.curPos,self.srcPos,self.destPos]
    arr.sort()

    print('__'*35,end='\n         ')
    started=False
    for i in range(arr[0],arr[2]+1):
      if (i==self.curPos):
        if not started:
          print(self.stations[i-1],end='>>')
        if pt:
          print('*'+self.stations[i],end='>>')
        else:
          tol_dis=round(self.stationsInfo[self.stations[self.curPos+1]]['distance']-self.stationsInfo[self.stations[self.curPos-1]]['distance'],2)
          dis=round(self.distance-self.stationsInfo[self.stations[self.curPos-1]]['distance'],2)
          pos=int(round(dis/tol_dis*10,0))
          print('-'*(pos-1)*2+'*'+self.stations[i]+'-'*(10-pos)*2,end='>>')
        continue
      print(self.stations[i],end='>>')
      started=True
    try:
      print(self.stations[arr[2]+1])
    except Exception:
      print('')
    print('__'*35)


  def showCurDetails(self):
    if not self.updated:
      self.update_info()
    print(round(self.curStnDistance,1),'kms from the',self.stationsInfo[self.curStn]['name'])
    print('_'*25)
    times=['sch_arrival_time','actual_arrival_time','non_agg_arrival_time']
    stations=[self.curStn,self.src,self.dest]
    print('Stop   schd   actu   ML')
    print('_'*25)
    for i in stations:
      print(i,end='   ')
      for j in times:
        try:
          print(self.stationsInfo[i][j],end='  ')
        except Exception:
          print('Nope',end='  ')
      print('\n'+'_'*25)
    print('last updated on',self.lastUpdated)

train1=train('12615','21-10-2019','CLX','WL')
train1.update_info()
train1.showCurMap()
train1.showCurDetails()
