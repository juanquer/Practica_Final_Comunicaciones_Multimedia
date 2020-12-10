from flask import Flask, render_template, session, url_for

app = Flask(__name__)

@app.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/home', methods=['GET','POST'])
def home():
	return render_template('home.html')

@app.route('/meetings', methods=['GET','POST'])
def meetings():
	return render_template('meetings.html')

@app.route('/text', methods=['GET','POST'])
def text():
	return render_template('text.html')

@app.route('/video_room', methods=['GET','POST'])
def video_room():
	return render_template('video_room.html')

@app.route('/video_room2', methods=['GET','POST'])
def video_room2():
	return render_template('video_room2.html')
@app.route('/video_room_bg', methods=['GET','POST'])
def video_room_bg():
	return render_template('video_room_bg.html')

@app.route('/calls', methods=['GET','POST'])
def calls():
	return render_template('calls.html')

if __name__ == "__main__":
	app.run()