from flask import Flask, render_template, request
from jinja2 import Template

app = Flask(__name__)

malicious_patterns = ["__", ".__"]
@app.route("/", methods=["GET", "POST"])
def function_route():
    if request.method == "POST":
        emailpre = request.form.get("emailpre")
        if any(pattern in emailpre for pattern in malicious_patterns):
            result = "This is a malicious string"
        else:
            template = Template(emailpre)
            result = template.render()
            #print(result)
        return render_template("result.html", result=result)
    
    return render_template("email_template.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
