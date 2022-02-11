# requires: pyrogram, tgcrypto, apscheduler

from pyrogram import Client
from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep

API_ID = 16623
API_HASH = "8c9dbfe58437d1739540f5d53c72ae4b"

app = Client('olokill', API_ID, API_HASH, ipv6=True)

CHAT = -1001494427468
MSG = 103540
USER = 200164142

def job():
    m = app.send_message(CHAT, '-', reply_to_message_id=MSG)
    m.delete()
    sleep(5)

    for i in range(1, 11):
        msg = app.get_messages(CHAT, m.message_id + i)
        if not msg.from_user:
            break
        if msg.from_user.id == USER:
            app.delete_messages(CHAT, msg.message_id)
            break

scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', seconds=125)

scheduler.start()
app.run()