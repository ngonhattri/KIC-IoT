from matplotlib.pyplot import title
from plyer import notification

TITLE = "通知のテスト"
MESG = "これは通知の本文です。\n改行もできます。これは2行目です。"

notification.notify(title=TITLE, message=MESG)