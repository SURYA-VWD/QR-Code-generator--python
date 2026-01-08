from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    qr_generated = False

    if request.method == "POST":
        data = request.form["data"]

        if data:
            img = qrcode.make(data)

            # Ensure static folder exists
            if not os.path.exists("static"):
                os.makedirs("static")

            img.save("static/qr.png")
            qr_generated = True

    return render_template("index.html", qr_generated=qr_generated)

if __name__ == "__main__":
    app.run()
