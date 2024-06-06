import streamlit as st
import pickle
import pandas as pd
import requests
import gzip
import os



# Load the gzip-compressed movie dictionary
try:
    with gzip.open('movie_dict.pkl.gz', 'rb') as f:
        movie_dict = pickle.load(f)
    
except FileNotFoundError:
    st.write("movie_dict.pkl.gz not found.")
except Exception as e:
    st.write(f"Error loading movie_dict.pkl.gz: {e}")

# Load the gzip-compressed similarity matrix
try:
    with gzip.open('similarity.pkl.gz', 'rb') as f:
        similarity = pickle.load(f)
    
except FileNotFoundError:
    st.write("similarity.pkl.gz not found.")
except Exception as e:
    st.write(f"Error loading similarity.pkl.gz: {e}")

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2709043dbfd211ccacce83a3e0f45ba6')
    data = response.json()
    return "https://image.tmdb.org/t/p/w185/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# Convert the movie dictionary to a DataFrame
movies = pd.DataFrame(movie_dict)

# Streamlit app
st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Choose a movie:', movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
