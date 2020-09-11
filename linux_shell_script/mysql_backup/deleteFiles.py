# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 09:34:17 2020

@author: inuya
"""
import os
import time 
import datetime
import json

config=open('config.json','r')
configstr=config.read()
config.close

configDict = json.loads(configstr)





def getFileName(fileUrl):
    filepath, tmpfilename = os.path.split(fileUrl)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension
def GetFileList(dir, fileList): 
    
    newDir = dir 

    if os.path.isfile(dir): 
        filepath, shotname, extension=getFileName(dir)
        if '.bak'  ==  extension or '.sql'  ==  extension:
            fileList.append(dir) 

    elif os.path.isdir(dir):   

        for s in os.listdir(dir): 

            #如果需要忽略某些文件夹，使用以下代码 

            '''if '.bak' not in  s: 

                continue '''

            newDir=os.path.join(dir,s) 

            GetFileList(newDir, fileList)   

    return fileList 

def fileTime(file):
    return [
        time.ctime(os.path.getatime(file)),#访问时间
        #time.ctime(os.path.getatime(file)),
        time.ctime(os.path.getmtime(file)),#修改时间
        time.ctime(os.path.getctime(file)) #创建时间
        ]
    
    
    
    
def getdays(targetTime):
    timenow= datetime.datetime.fromtimestamp(time.time())
    targetTime=datetime.datetime.fromtimestamp(targetTime)
    return (timenow-targetTime).days






def getFileLsitSize(FileList):
    sizecount=0
    for File in FileList:
        sizecount=sizecount+os.path.getsize(File)

    return sizecount



def getFirstfile(FileList):
    tempatime=0
    Firstfile=''
    for File in FileList:
        
        if tempatime==0:
            tempatime=os.path.getctime(File)
            Firstfile=File
        elif tempatime>=os.path.getctime(File):
            tempatime=os.path.getctime(File)
            Firstfile=File
    return Firstfile


def getLastfile(FileList):
    tempatime=0
    Firstfile=''
    for File in FileList:
        
        if tempatime==0:
            tempatime=os.path.getctime(File)
            Firstfile=File
        elif tempatime<=os.path.getctime(File):
            tempatime=os.path.getctime(File)
            Firstfile=File
    return Firstfile



def getdelListBySize(FileList,Size):
    delLsit=[]
    targetFileList=[]
    for File in FileList:
        targetFileList.append(File)
    Size=Size*1024*1024*1024
    while(getFileLsitSize(targetFileList)>Size):
        Firstfile=getFirstfile(targetFileList)
        delLsit.append(Firstfile)
        targetFileList.remove(Firstfile)
        #print(targetFileList,getFileLsitSize(targetFileList)>Size)
    return delLsit


def getdelListByTime(FileList,days):
    delLsit=[]

    for File in FileList:
        if getdays(os.path.getctime(File))>int(days):
            delLsit.append(File)
    
    return delLsit

def getdelListByCount(FileList,Count):
    Count=int(Count)
    delLsit=[]
    targetFileList=[]
    for File in FileList:
        targetFileList.append(File)
    
    while(len(targetFileList)>Count):
        #print(targetFileList)
        Firstfile=getFirstfile(targetFileList)
        #print(Firstfile,"zuizao")
        delLsit.append(Firstfile)
        targetFileList.remove(Firstfile)
    return delLsit

def getdelList(FileList,configDict):
    delList=[]
    if FileList==[]:
        return []
    if configDict["delBySize"]:
        delList=getdelListBySize(FileList,configDict["Size(G)"])
    elif configDict["delBytime"]:
        delList=getdelListByTime(FileList,configDict["days"])
    elif configDict["delByCount"]:
        delList=getdelListByCount(FileList,configDict["Count"])
    
    if len(FileList)==len(delList):
        Lastfile=getLastfile(delList)
        #print(Lastfile)
        delList.remove(Lastfile)

    return delList
    
def delFiles(FileList):
    for File in FileList:
        print("删除的文件路径：{}".format(File))
	os.remove(File)
        
        
for Path in configDict["delPath"]:     
    bakFileList=GetFileList(Path,[])
    delList=getdelList(bakFileList,configDict)  
    delFiles(delList) 
    print(Path,"done")



