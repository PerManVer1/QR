#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter as tk
from PIL import Image
import qrcode




def data_input(evant):
    #エントリーから情報を取得
    value = EditBox.get()
    #つくりたいQRコードの情報をmake_qrに渡す
    Make_QR(value)

def Make_QR(data):
    qr=qrcode.QRCode(version=4,box_size=5)
    qr.add_data(str(data))
    qr.make()
    img=qr.make_image()
    img.save(str(data)+".png")
    img.show()
    

    
root = tk.Tk()
root.title(u"QRコード製作プログラム")
root.geometry("400x100")


#ラベル
label1 = tk.Label(text=u'下の文字入力欄の中に名前をローマ字、入室をEnter,退室をleftと入力してください')
label1.pack()

label2 = tk.Label(text=u'記入例)SARD Enter')
label2.pack()


#エントリー
EditBox = tk.Entry(width=50)
EditBox.insert(tk.END,"QRコードに埋め込みたい情報を入力")
EditBox.pack()

#ボタン
Button = tk.Button(text=u'QR作成',width=50)
Button.pack()
Button.bind("<Button-1>",data_input)

#エントリーの中身を削除
EditBox.delete(0, tk.END)

root.mainloop()
