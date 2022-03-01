import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3b153a99189b897fa01cb470cb1ab68f&language=en-US'.format(movie_id))
     data = response.json()
     return "http://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     dist = similarity[movie_index]
     movies_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[0:6]

     recomended_movies= []
     recom_movie_poster=[]
     for i in movies_list:
          movie_id = movies.iloc[i[0]].movie_id
          recomended_movies.append(movies.iloc[i[0]].title)
          recom_movie_poster.append(fetch_poster(movie_id))
     return recomended_movies, recom_movie_poster

movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

option = st.selectbox(
     'Which movie did you watch?',
     (movies['title'].values))

if st.button('Recommend'):
    names, posters = recommend(option)

    col1, col2, col3, col4, col5, col6 = st.columns(6)

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

    with col6:
        st.text(names[5])
        st.image(posters[5])
