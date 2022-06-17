from plyer import battery
import pyttsx3
from plyer import notification



status = battery.get_state()
print(status)
engine = pyttsx3.init()

MIN = 20
MAX = 80

if(status['isCharging'] == False and status['percentage'] >= MAX):
    notification.notify(title="バッテリーが80％以上です。", message="充電器を外すことを推奨です。")
    engine.say('バッテリーが80％以上です。充電器を外すことを推奨です。')
elif(status['isCharging'] == False and status['percentage'] <= MIN):
    notification.notify(title="バッテリーが20％以下です。", message="充電器を繋ぐことを推奨です。")
    engine.say('バッテリーが20％以下です。充電器を繋ぐことを推奨です。')




engine.runAndWait()