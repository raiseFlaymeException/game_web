from flask import Flask, render_template, request, send_file
import threading
module = True
try:
    import webbrowser
    import pynput
except ModuleNotFoundError:
    module = False
import os.path
import sys

# TODO: ADD A DISCLAIMER SAYING THAT DOWNLOADING THE GAME AND RUNNING THE EXECUTABLE MAY TRIGGER SOME WARNING OF THE ANTIVIRUS

app = Flask(__name__)

sites = ["HOME", "DOWNLOAD", "UPDATE", "HOW TO PLAY", "TEXTURE PACK", "REPORT BUG", "FORUM", "LICENSE"]

platforms = ["windows", "linux"]

@app.route("/")
def home():
    return render_template("index.html", sites=sites)

@app.route("/download")
def download():
    return render_template("download.html", sites=sites, platforms=platforms)

@app.route("/download-windows")
def download_windows():
    return send_file(os.path.join("static", "bin", "install.exe"))

@app.route("/download-linux")
def download_linux():
    return send_file(os.path.join("static", "bin", "install.exe"))

@app.route("/update")
def update():
    return render_template("update.html", sites=sites)

@app.route("/how_to_play")
def how_to_play():
    return render_template("play.html", sites=sites)

@app.route("/texture_pack")
def texture_pack():
    return render_template("texture.html", sites=sites)

@app.route("/report")
def report_bug():
    return render_template("report.html", sites=sites)

@app.route("/forum")
def forum():
    return render_template("forum.html", sites=sites)

@app.route("/license")
def license():
    return render_template("license.html", sites=sites)


t = threading.Thread(target=app.run, daemon=True, kwargs={"host": "0.0.0.0"})
t.start()

if module and len(sys.argv)>1:
    argv = sys.argv[1:]

    if "open" in argv:
        webbrowser.open("http://127.0.0.1:5000/")
        
    if "key" in argv:
        def onpress(key):
            if type(key)==pynput.keyboard.Key and key==key.end:
                exit(0)

        key = pynput.keyboard.Listener(onpress)
        key.start()
        key.join()
    else:
        t.join()
else:
    t.join()

