from flask import *
import smtplib
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<page_name>")
def page(page_name):
    return render_template(page_name)

@app.route("/submit_form",methods=['POST','GET'])
def submit_form():
    if request.method=="POST":
        data=request.form.to_dict()
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        EMAIL="tazeen.fatima.khan.1986@gmail.com"
        PASSWORD="orguobjwdqexxrzq"

        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=EMAIL,password=PASSWORD)
            conn.sendmail(from_addr=EMAIL,
            to_addrs="tazeen_86@hotmail.com",
            msg=f"Email:{email},Subject:{subject},Message:{message}")
        return redirect('/thankyou.html')
    else:
        return "Something went wrong. Form Submitted!"
    