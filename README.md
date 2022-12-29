# 実行環境

使用した環境
・Ubuntu 20.04
・Python 3.10.2

# Pythonライブラリのインストール
```
pip install --upgrade pip #pip更新

pip install opencv-python #カメラを使うときに必要
pip install glob #「*.jpg」で必要
pip install numpy #数値計算
```

# 外付けまたは内蔵カメラでカメラのピント調節(Escキーでカメラオフ)
```testing.py
import cv2
import glob
import os
import numpy as np
def tesing_camera():
    cap = cv2.VideoCapture(0)
    while True:
        # 1フレームずつ取得する。
        ret, frame = cap.read()
        #フレームが取得できなかった場合は、画面を閉じる
        if not ret:
            break
    
        # ウィンドウに出力
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        # Escキーを入力されたら画面を閉じる
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

tesing_camera() #test camera
```

# 数秒間カメラから録画を行う。
```recording.py
import cv2
import glob
import os
import numpy as np
def Recording():
    #撮影時間を秒で指定  3分の場合は180
    time = int(input("enter the number of seconds\n>>"))
    
    #USBカメラの場合は1、パソコン内蔵カメラの場合は0
    print("PC CAMERA:0, USB CAMERA:1")
    setting = int(input("enter 0 or 1\n>>"))
    cap = cv2.VideoCapture(setting)
    
    #fpsを20.0にして撮影したい場合はfps=20.0にします
    fps = 30.0
    
    #カメラの幅を取得
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #カメラの高さを取得
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    #動画保存時の形式を設定
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    name = "sample.mov"
    
    #(保存名前、fourcc,fps,サイズ)
    video = cv2.VideoWriter(name, fourcc, fps, (w,h))
 
    #fps×指定した撮影時間の値繰り返す
    print("start")
    roop = int(fps * time)
    for i in range(roop):
        ret, frame = cap.read()#1フレーム読み込み
        video.write(frame)#1フレーム保存する
    
    print("stop")
    video.release()
    cap.release()
    cv2.destroyAllWindows()
    
    return video

Recording() #録画
```

実行結果です。
```
enter the number of seconds
>>3 #適当
PC CAMERA:0, USB CAMERA:1
enter 0 or 1
>>0
start

stop
```

# 録画した動画を再生する。
```playback.py
import cv2
import glob
import os
import numpy as np
def playback():
    cap = cv2.VideoCapture(r'data/sample.mov')
    if (cap.isOpened()== False):  
        print("ビデオファイルを開くとエラーが発生しました")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow("Video", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'): 
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

playback() #再生
```

実行結果です。
```
#再生
```
おわり
***
>他の記事
・[[2022年]SVMの学習セットのフォーマット(CSVファイル)](https://qiita.com/netineti512/items/2596d4fbdebd700a7aa0)
・[[2022年]MediaPipeで取得した座標データの統一化の方法[CSVファイル]](https://qiita.com/netineti512/items/fd5929361a6fdb8f629b)
・[[2022年]PythonのMediaPipeを使い、動画ファイルの手を認識し、CSVファイルに座標データを保存する方法](https://qiita.com/netineti512/items/b79ff4f878c7795b6b91)
・[[2022年]PythonのOpenCVを使って動画を録画する方法](https://qiita.com/netineti512/items/57b532d5acd29ab36e67)
