from flask import Flask, request, render_template
import os
import redis
import socket

app = Flask(__name__)

# Load configurations from environment or config file
app.config.from_pyfile('config_file.cfg')

if ("VOTE1VALUE" in os.environ and os.environ['VOTE1VALUE']):
    button1 = os.environ['VOTE1VALUE']
else:
    button1 = app.config['VOTE1VALUE']

if ("VOTE2VALUE" in os.environ and os.environ['VOTE2VALUE']):
    button2 = os.environ['VOTE2VALUE']
else:
    button2 = app.config['VOTE2VALUE']

if ("VOTE3VALUE" in os.environ and os.environ['VOTE3VALUE']):
    button3 = os.environ['VOTE3VALUE']
else:
    button3 = app.config['VOTE3VALUE']

if ("VOTE4VALUE" in os.environ and os.environ['VOTE4VALUE']):
    button4 = os.environ['VOTE4VALUE']
else:
    button4 = app.config['VOTE4VALUE']

if ("VOTE5VALUE" in os.environ and os.environ['VOTE5VALUE']):
    button5 = os.environ['VOTE5VALUE']
else:
    button5 = app.config['VOTE5VALUE']

if ("VOTE6VALUE" in os.environ and os.environ['VOTE6VALUE']):
    button6 = os.environ['VOTE6VALUE']
else:
    button6 = app.config['VOTE6VALUE']

if ("VOTE7VALUE" in os.environ and os.environ['VOTE7VALUE']):
    button7 = os.environ['VOTE7VALUE']
else:
    button7 = app.config['VOTE7VALUE']

if ("VOTE8VALUE" in os.environ and os.environ['VOTE8VALUE']):
    button8 = os.environ['VOTE8VALUE']
else:
    button8 = app.config['VOTE8VALUE']

if ("TITLE" in os.environ and os.environ['TITLE']):
    title = os.environ['TITLE']
else:
    title = app.config['TITLE']

if ("TITLE1" in os.environ and os.environ['TITLE1']):
    title1 = os.environ['TITLE1']
else:
    title1 = app.config['TITLE1']

if ("TITLE2" in os.environ and os.environ['TITLE2']):
    title2 = os.environ['TITLE2']
else:
    title2 = app.config['TITLE2']



# Redis configurations
redis_server = os.environ['REDIS']

# Redis Connection
try:
    if "REDIS_PWD" in os.environ:
        r = redis.StrictRedis(host=redis_server,
                        port=6379,
                        password=os.environ['REDIS_PWD'])
    else:
        r = redis.Redis(redis_server)
    r.ping()
except redis.ConnectionError:
    exit('Failed to connect to Redis, terminating.')

# Change title to host name to demo NLB
if app.config['SHOWHOST'] == "true":
    title = socket.gethostname()

if app.config['SHOWHOST'] == "true":
    title1 = socket.gethostname()

if app.config['SHOWHOST'] == "true":
    title2 = socket.gethostname()



# Init Redis
if not r.get(button1): r.set(button1, 0)
if not r.get(button2): r.set(button2, 0)
if not r.get(button3): r.set(button3, 0)
if not r.get(button4): r.set(button4, 0)


@app.route('/', methods=['GET', 'POST'])
def index():


    if request.method == 'GET':


        # Get current values
        vote1 = r.get(button1).decode('utf-8')
        vote2 = r.get(button2).decode('utf-8')
        vote3 = r.get(button3).decode('utf-8')
        vote4 = r.get(button4).decode('utf-8')
        vote5 = r.get(button5).decode('utf-8')
        vote6 = r.get(button6).decode('utf-8')
        vote7 = r.get(button7).decode('utf-8')
        vote8 = r.get(button8).decode('utf-8')

        # Return index with values
        return render_template("index.html", value1=int(vote1), value2=int(vote2), value3=int(vote3), value4=int(vote4),
                                   value5=int(vote5), value6=int(vote6), value7=int(vote7), value8=int(vote8),
                                   button1=button1, button2=button2, button3=button3, button4=button4, title=title)


if __name__ == "__main__":
    app.run()
