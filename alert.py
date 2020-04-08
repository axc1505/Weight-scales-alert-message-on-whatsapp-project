
from twilio.rest import Client //twilio library
import serial
import time
ser=serial.Serial('COM3',9600)



account_sid = 'AC54a272607e0778385abe68c4af4acdd8'
auth_token = '9f5f36f983665b5bfae1368bd0bb8b96'

client = Client(account_sid, auth_token)

while True:
    while ser.inWaiting():
        grame=ser.readline().decode()
        messageTosend = "Alert, the detected weight has exceeded 50 grams! Weight registered: " + str(grame) + " grams. Check your sensor!"
        message = client.messages.create(
                            body=messageTosend,
                            from_="whatsapp:+14155238886",
                            to="whatsapp:+4071234567"
                        )
        time.sleep(10)

print(message.sid)
