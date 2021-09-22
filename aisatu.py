# 現在時刻の取得
import datetime

now =datetime.datetime.now()
if now.hour >=4 and now.hour <=10:
    print('おはようございます。現在は{}のはずです。'.format(now.strftime("%Y年%m月%d日%H時%m分")))
elif now.hour >=11 and now.hour <=17:
    print('こんにちは。現在は{}のはずです。'.format(now.strftime("%Y年%m月%d日%H時%m分")))
else:
    print('こんばんわ。現在は{}のはずです。'.format(now.strftime("%Y年%m月%d日%H時%m分")))