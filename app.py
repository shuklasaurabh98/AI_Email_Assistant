from flask import Flask, request, render_template
from email_generator import generate_email

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form

        email = generate_email(
            # subject=data["subject"],
            # purpose=data["purpose"],
            # tone=data["tone"],
            # recipient=data["recipient"],
            # key_points=data["key_points"],
            # sender=data["sender"]

            subject=data.get("subject"),
            purpose=data.get("purpose", ""),
            tone=data.get("tone"),
            recipient=data.get("recipient"),
            key_points=data.get("key_points"),
            sender=data.get("sender")
        )
        # exract subject and body
        subject_line = ""
        body = email

        if "Subject:" in email:
            parts = email.split("Body")
            subject_line = parts[0].replace("Subject:", "").strip()
            body = parts[1].strip() if len(parts) > 1 else ""
            

        # return render_template("index.html", result=email)
        return render_template("index.html", result=body, subject=subject_line)

    return render_template("index.html", result="")

if __name__ == "__main__":
    app.run(debug=True)