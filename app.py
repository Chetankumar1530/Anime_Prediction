from flask import Flask , render_template , request, redirect
from anime_predictor import anime_pred ,genere , rating , checker
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/anime" , methods = ["POST" ,"GET"])
def anime():
    if request.method == "POST":
        a = request.form["input"]
        if len(checker(a)) > 4:
                
            
            b = anime_pred(a,10)
            gg = genere(a,10)
            rr = rating(a,10)
            return render_template("anime.html" , ll = b  , gg = gg , rr = rr)
        else:
            ll = checker(a)
            return render_template("anime.html" , ll = ll  )
            

    ll = []      
    return render_template("anime.html" , ll = ll)


if __name__ == "__main__":
    app.run(debug=True)
