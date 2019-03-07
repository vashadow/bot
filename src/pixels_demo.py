import time
import threading
from pixels import Pixels, pixels
from alexa_led_pattern import AlexaLedPattern
from google_home_led_pattern import GoogleHomeLedPattern
from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='microblog', template_mode='bootstrap3')


@app.route('/')
def root():
    return 'Hello Ferguson Maker Space!'

def flaskThread():
    app.run(host="0.0.0.0", port=80, threaded=True)
	
	
if __name__ == '__main__':

    threading.Thread(target=flaskThread).start()
	
    pixels.pattern = GoogleHomeLedPattern(show=pixels.show)
    #pixels.pattern = AlexaLedPattern(show=pixels.show)
	
    while True:

        try:
            pixels.wakeup()
            time.sleep(3)
            pixels.think()
            time.sleep(3)
            pixels.speak()
            time.sleep(6)
            pixels.off()
            time.sleep(3)
        except KeyboardInterrupt:
            break


    pixels.off()
    time.sleep(1)
