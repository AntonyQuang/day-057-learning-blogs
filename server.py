from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.date.today().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    age_response = requests.get(url=f"https://api.agify.io/?name={name}")
    age_data = age_response.json()
    age = age_data["age"]
    gender_response = requests.get(url=f"https://api.genderize.io/?name={name}")
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/7249457ee7f003f58750"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

