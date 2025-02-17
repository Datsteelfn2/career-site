from flask import Flask,render_template

app=Flask(__name__)#creating object

@app.route("/")# when url is requested
def hello():
  return render_template("home.html")

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)# this is to run the web server