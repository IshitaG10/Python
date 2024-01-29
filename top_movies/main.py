from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = "f12c5b5cbcd5b98cc641ea87bbd9fd43"
API_URL = "https://api.themoviedb.org/3/search/movie"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer f12c5b5cbcd5b98cc641ea87bbd9fd43"
}

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db.init_app(app)

class Movie(db.Model):
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String(250), unique=True, nullable=False) 
    year:Mapped[str] = mapped_column(String, nullable=False)
    description:Mapped[str] = mapped_column(String(500), nullable=False)
    rating:Mapped[float] = mapped_column(Float, nullable=True)
    ranking:Mapped[int] = mapped_column(Integer, nullable=True)
    review:Mapped[str] = mapped_column(String(250), nullable=True)
    img_url:Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    new_rating = StringField(label = 'Your Rating out of 10 e.g. 7.3',validators=[DataRequired()])
    new_review = StringField(label = 'Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')

class AddMovieForm(FlaskForm):
    movie_name = StringField(label = "Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    movies = result.scalars().all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()
    
    return render_template("index.html", all_movies = movies)

@app.route("/edit", methods = ['GET', 'POST'])
def edit():
    # "POST /edit?id=2 HTTP/1.1" 302- as the POST request also has id argument in it's endpoint so when the edit function is called again the value is assigned again
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    update_form = RateMovieForm()
    if update_form.validate_on_submit():
        movie.rating = float(update_form.new_rating.data)
        movie.review = update_form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form = update_form, movie = movie)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods = ['GET', 'POST'])
def add():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        movie_title = add_form.movie_name.data
        response = requests.get(url=API_URL,  params={"api_key": API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", movies = data)
    return render_template("add.html", form = add_form)

@app.route("/fetch_data")
def fetch_data():
    id =  request.args.get('id')
    print(id)
    movie_url = "https://api.themoviedb.org/3/movie"
    response = requests.get(url=f"{movie_url}/{id}" , params={"api_key": API_KEY})
    data = response.json()
    print(data)
    new_movie = Movie(
        title=data["title"],
        year=data["release_date"].split("-")[0],
        rating = data["vote_average"],
        img_url=f"https://image.tmdb.org/t/p/original/{data['poster_path']}",
        description=data["overview"]
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id = new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
