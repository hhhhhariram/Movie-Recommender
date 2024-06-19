import pickle
import streamlit as st
import requests
import base64
from PIL import Image

# Function to fetch movie poster and details
def fetch_movie_details(movie_name):
    api_key = "8265bd1679663a7ea12ac168da84d2e8"
    search_url = "https://api.themoviedb.org/3/search/movie"
    movie_url = "https://api.themoviedb.org/3/movie"
    poster_base_url = "https://image.tmdb.org/t/p/w500"

    search_params = {
        'api_key': api_key,
        'query': movie_name,
        'language': 'en-US'
    }
    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()

    if search_data['results']:
        movie_id = search_data['results'][0]['id']
        movie_response = requests.get(f"{movie_url}/{movie_id}", params={'api_key': api_key, 'language': 'en-US'})
        movie_data = movie_response.json()

        poster_path = movie_data.get('poster_path')
        poster_url = f"{poster_base_url}{poster_path}" if poster_path else "Poster not found"
        release_date = movie_data.get('release_date', 'N/A')
        rating = movie_data.get('vote_average', 'N/A')
        genres = ', '.join([genre['name'] for genre in movie_data.get('genres', [])])

        credits_url = f"{movie_url}/{movie_id}/credits"
        credits_response = requests.get(credits_url, params={'api_key': api_key})
        credits_data = credits_response.json()

        director = ', '.join([crew['name'] for crew in credits_data.get('crew', []) if crew['job'] == 'Director'])
        actors = ', '.join([cast['name'] for cast in credits_data.get('cast', [])][:5])  # Top 5 actors

        return poster_url, release_date, rating, genres, director, actors
    else:
        return "Movie not found", "N/A", "N/A", "N/A", "N/A", "N/A"

# Recommendation function
def recommend(movie):
    index = movies[movies['movie_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_details = []
    for i in distances[1:10]:  # Displaying 8 recommended movies
        movie_name = movies.iloc[i[0]].movie_title
        details = fetch_movie_details(movie_name)
        recommended_movie_names.append(str(movie_name).capitalize())
        recommended_movie_details.append(details)

    return recommended_movie_names, recommended_movie_details

im = Image.open("—Pngtree—movie element movie icon_4380477.png")
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="expanded",

)


# Load movies and similarity data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_list = movies['movie_title'].values

def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://assets.aboutamazon.com/dims4/default/16a8439/2147483647/strip/true/crop/1066x600+67+0/resize/1320x743!/format/webp/quality/90/?url=https%3A%2F%2Famazon-blogs-brightspot.s3.amazonaws.com%2F6e%2F65%2F8beecded4f798e2d6d77c650b27b%2Frday-movie-poster.jpg");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local()

# Streamlit app layout
custom_css = """
<style>
    .title {
        font-family: 'Times New Roman', Times, serif;
        font-weight: bold;
        color: white;
    }
    .instructions {
        font-family: 'Times New Roman', Times, serif;
        font-size:20px;
        font-weight: bold;
        color: black;
    }
</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Title and instructions with custom styling
st.markdown('<h1 class="title">🎬 Movie Recommender System Using Machine Learning 🎥</h1>', unsafe_allow_html=True)
st.markdown('<p class="instructions">**Select a movie and get recommendations:**</p>', unsafe_allow_html=True)
selected_movie = st.selectbox("Type or select a movie", movie_list, key="selected_movie")


if st.button('Show Recommendation', key="recommend_button"):
    recommended_movie_names, recommended_movie_details = recommend(selected_movie)

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .movie-container {
            background-color: #fafafa;
            padding: 15px;
            margin: 10px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            text-align: center;
            height: 650px;
            width: 100%;
        }
        .movie-container:hover {
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        }
        .movie-container img {
            border-radius: 10px;
            width: 100%;
            height: auto;
            object-fit: cover;
            max-height: 300px;
        }
        .movie-name {
            background-color:#2dfd37;
            font-family: 'Times New Roman', Times, serif;
            font-size: 24px;
            color:black;
            font-weight: bold;
            margin: 10px 0 5px 0;
        }
        .release-date, .rating, .genres, .director, .actors {
            font-family: 'Times New Roman', Times, serif;
            font-size: 16px;
            color: #666;
            margin-bottom: 5px;
        }
        .director, .rating, .actors {
            background-color: #f0f0f0;
            padding: 5px;
            border-radius: 5px;
            font-weight: bold;
        }
        .genres {
            color: #4CAF50; /* Green color for genres */
        }
        .director {
            color: #2196F3; /* Blue color for director */
        }
        .rating {
            color: #FF9800; /* Orange color for rating */
        }
        .actors {
            color: #9C27B0; /* Purple color for actors */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display recommended movies in three columns
    cols = st.columns(3)
    for i in range(len(recommended_movie_names)):
        name, details = recommended_movie_names[i], recommended_movie_details[i]
        poster_url, release_date, rating, genres, director, actors = details

        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="movie-container">
                    <img src="{poster_url}" alt="{name}">
                    <div class="movie-name">{name}</div>
                    <div class="release-date">Release Date: {release_date}</div>
                    <div class="rating">Rating: {rating}</div>
                    <div class="genres">Genres: {genres}</div>
                    <div class="director">Director: {director}</div>
                    <div class="actors">Actors: {actors}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
