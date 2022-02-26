from flask import Flask , render_template , request, redirect
from anime_predictor import anime_hunt ,genere , rating , checker ,list_gene,list_name,list_rating
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/anime" , methods = ["POST" ,"GET"])
def anime():
    if request.method == "POST":
        a = request.form["input"]
        if len(checker(a)) > 4:
                
            
            b = anime_hunt(a,10)
            gg = genere(a,10)
            rr = rating(a,10)
            return render_template("anime.html" , ll = b  , gg = gg , rr = rr)
        else:
            ll = checker(a)
            return render_template("anime.html" , ll = ll  )
            

    ll = []      
    return render_template("anime.html" , ll = ll)


@app.route("/list")
def list():
    name = list_name()
    gen = list_gene()
    rat = list_rating()

    return render_template("list.html" , name=name , gen = gen, rat = rat)


if __name__ == "__main__":
    app.run(debug=True)
