import cv2
from pyzbar.pyzbar import decode
import requests
from PIL import Image
import datetime
import pyqrcode
import time
import csv

cap=cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_SIMPLEX 

barcodes=[]
QRread=[]
QRdata=[]

while cap.isOpened():
    ret,frame=cap.read()
    #print(ret)カメラから情報を取得できているかの確認用
    with open("QRdata.csv","r",encoding="utf-8")as f:
        QRread=f.read()
    if ret:
        d=decode(frame)
        
        if d:
            for barcode in d:
                barcodes=barcode.data.decode('utf-8')
                
                font_color=(0,154,87)
                
                x,y,w,h=barcode.rect
                cv2.rectangle(frame,(x,y),(x+w,y+h),font_color,2)
                frame=cv2.putText(frame,barcodes,(x,y-10),font,5,font_color,2,cv2.LINE_AA)
    elif not ret:
        break

    cv2.imshow('BARCODE READER',frame)
    key=cv2.waitKey(1)

    #バーコードを読み取れなかった時
    if not barcodes:
        print("no data")
        time.sleep(1)
    #バーコードを読み取れた時   
    else:
        print("get data")
        #QRdataにデータを代入
        QRdata=str(barcodes)
        





        #スキャンしたデータが前の情報と同じものだった場合
        if QRread==barcodes:
            with open("QRdata.csv","w",encoding="utf-8")as f:
                f.write(str(barcodes))
            #print(barcodes)データを取得できているかの確認用
            print("前のデータと同じなので送信しません")
        #スキャンしたデータが前の情報と異なるものだった場合  
        else:
            with open("QRdata.csv","w",encoding="utf-8")as f:
                f.write(str(barcodes))
            print(QRdata)
            TOKEN='h7tJRVEypnYuHgmGCQGlA1mMD8oiCHzrousa9EpZBc3'
            
            api_url='https://notify-api.line.me/api/notify'
            
            date=datetime.datetime.now()
            
            print(barcodes)
            send_contents=str(barcodes)+str(date.month)+"月"+str(date.day)+"日"+str(date.hour)+"時"+str(date.minute)+"分"+str(date.second)+"秒"
            TOKEN_dic={'Authorization':'Bearer'+' '+TOKEN}
            send_dic={'message':send_contents}
            requests.post(api_url,headers=TOKEN_dic,data=send_dic)
            
            print("正常に送信しました")
                
cap.release()
cv2.destroyAllWindows()
