# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:58:23 2023

@author: hp
"""

import pickle
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title = "Book Recommendation System", layout = "wide") 


st.title("Book Recommendation system..!")


model = pickle.load(open('model.pkl', 'rb'))
book_name = pickle.load(open('book_name.pkl', 'rb'))
final_ratings = pickle.load(open('final_ratings.pkl', 'rb'))
books_pivot = pickle.load(open('books_pivot.pkl', 'rb'))
popular_book_img = pickle.load(open('popular_book_img.pkl', 'rb'))
no_of_times_rated_book_img = pickle.load(open('no_of_times_rated_book_img.pkl', 'rb'))
books_with_ratings = pickle.load(open('books_with_ratings.pkl', 'rb'))
age_with_books = pickle.load(open('age_with_books.pkl', 'rb'))



tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Recommending Books", "Popular Book", "More Rated Books", "Authors", "Age", "Country"])


# Recommendation of books
with tab1:
    
    def fetch_poster(suggestion):
        book_name = []
        ids_index = []
        poster_url = []
    
        for book_id in suggestion:
            book_name.append(books_pivot.index[book_id])
        
        for name in book_name[0]:
            ids = np.where(final_ratings['title'] == name)[0][0]
            ids_index.append(ids)
        
        for idx in ids_index:
            url = final_ratings.iloc[idx]['img_url']
            poster_url.append(url)
        
        return poster_url


    def recommend_book(book_name):
        book_list = []
        book_id = np.where(books_pivot.index == book_name)[0][0]
        distance, suggestion = model.kneighbors(books_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=11)
    
        poster_url = fetch_poster(suggestion)
    
        for i in range(len(suggestion)):
            books = books_pivot.index[suggestion[i]]
            for j in books:
                book_list.append(j)
            
        return book_list, poster_url

    selected_books = st.selectbox(
        'Type or Select Book-Title',
        book_name
    )


    
    
    if st.button('Show Recommendation'):
        tab1.subheader(f'Recommending Books based on " {selected_books} "')
        recommendation_book, poster_url = recommend_book(selected_books)
            
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with st.container():
             
            with col1:
                st.text(recommendation_book[1])
                st.image(poster_url[1])
        
            with col2:
                st.text(recommendation_book[2])
                st.image(poster_url[2])
            
            with col3:
                st.text(recommendation_book[3])
                st.image(poster_url[3])
            
            with col4:
                st.text(recommendation_book[4])
                st.image(poster_url[4])
            
            with col5:
                st.text(recommendation_book[5])
                st.image(poster_url[5])
        
        col1, col2, col3, col4, col5 =st.columns(5)
        with st.container():
            with col1:
                st.text(recommendation_book[6])
                st.image(poster_url[6])
        
            with col2:
                st.text(recommendation_book[7])
                st.image(poster_url[7])
        
            with col3:
                st.text(recommendation_book[8])
                st.image(poster_url[8])
              
            with col4:
                st.text(recommendation_book[9])
                st.image(poster_url[9])
     
            with col5:
                st.text(recommendation_book[10])
                st.image(poster_url[10])
                
                
#--------------------------------------------------------------------------------------------------------------------------
# ----------------------- [TAB 2] -----------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

with tab2:
    tab2.header("Popular Books")
    st.subheader('Top Rated Books ')
    
    
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 =st.columns(10)    
    with st.container(): 
        
        with col1:
            st.text(popular_book_img.iloc[0][0])
            st.image(popular_book_img.iloc[0][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[0][2],2)}')
            
        with col2:
            st.text(popular_book_img.iloc[1][0])
            st.image(popular_book_img.iloc[1][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[1][2],2)}')
                
        with col3:
            st.text(popular_book_img.iloc[2][0])
            st.image(popular_book_img.iloc[2][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[2][2],2)}')
            
        with col4:
            st.text(popular_book_img.iloc[3][0])
            st.image(popular_book_img.iloc[3][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[3][2],2)}')
           
        with col5:
            st.text(popular_book_img.iloc[4][0])
            st.image(popular_book_img.iloc[4][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[4][2],2)}')
            
        with col6:
            st.text(popular_book_img.iloc[5][0])
            st.image(popular_book_img.iloc[5][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[5][2],2)}')
    
        with col7:
            st.text(popular_book_img.iloc[6][0])
            st.image(popular_book_img.iloc[6][3]) 
            st.text(f'Rating:{np.round(popular_book_img.iloc[6][2],2)}')
            
        with col8:
            st.text(popular_book_img.iloc[7][0])
            st.image(popular_book_img.iloc[7][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[0][2],2)}')
       
        with col9:
            st.text(popular_book_img.iloc[8][0])
            st.image(popular_book_img.iloc[8][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[8][2],2)}')
    
        with col10:
            st.text(popular_book_img.iloc[9][0])
            st.image(popular_book_img.iloc[9][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[9][2],2)}')
    
    
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 =st.columns(10)
    with st.container():
        
        with col1:
            st.text(popular_book_img.iloc[10][0])
            st.image(popular_book_img.iloc[10][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[10][2],2)}')
            
        with col2:
            st.text(popular_book_img.iloc[11][0])
            st.image(popular_book_img.iloc[11][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[11][2],2)}')
                
        with col3:
            st.text(popular_book_img.iloc[12][0])
            st.image(popular_book_img.iloc[12][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[12][2],2)}')
            
        with col4:
            st.text(popular_book_img.iloc[13][0])
            st.image(popular_book_img.iloc[13][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[13][2],2)}')
           
        with col5:
            st.text(popular_book_img.iloc[14][0])
            st.image(popular_book_img.iloc[14][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[14][2],2)}')
            
        with col6:
            st.text(popular_book_img.iloc[15][0])
            st.image(popular_book_img.iloc[15][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[15][2],2)}')
    
        with col7:
            st.text(popular_book_img.iloc[16][0])
            st.image(popular_book_img.iloc[16][3]) 
            st.text(f'Rating:{np.round(popular_book_img.iloc[16][2],2)}')
            
        with col8:
            st.text(popular_book_img.iloc[17][0])
            st.image(popular_book_img.iloc[17][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[17][2],2)}')
       
        with col9:
            st.text(popular_book_img.iloc[18][0])
            st.image(popular_book_img.iloc[18][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[18][2],2)}')
    
        with col10:
            st.text(popular_book_img.iloc[19][0])
            st.image(popular_book_img.iloc[19][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[19][2],2)}')
    
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 =st.columns(10)
    with st.container():
        
        with col1:
            st.text(popular_book_img.iloc[20][0])
            st.image(popular_book_img.iloc[20][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[20][2],2)}')
            
        with col2:
            st.text(popular_book_img.iloc[21][0])
            st.image(popular_book_img.iloc[21][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[21][2],2)}')
                
        with col3:
            st.text(popular_book_img.iloc[22][0])
            st.image(popular_book_img.iloc[22][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[22][2],2)}')
            
        with col4:
            st.text(popular_book_img.iloc[23][0])
            st.image(popular_book_img.iloc[23][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[23][2],2)}')
           
        with col5:
            st.text(popular_book_img.iloc[24][0])
            st.image(popular_book_img.iloc[24][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[24][2],2)}')
            
        with col6:
            st.text(popular_book_img.iloc[25][0])
            st.image(popular_book_img.iloc[25][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[25][2],2)}')
    
        with col7:
            st.text(popular_book_img.iloc[26][0])
            st.image(popular_book_img.iloc[26][3]) 
            st.text(f'Ratings:{np.round(popular_book_img.iloc[26][2],2)}')
            
        with col8:
            st.text(popular_book_img.iloc[27][0])
            st.image(popular_book_img.iloc[27][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[27][2],2)}')
       
        with col9:
            st.text(popular_book_img.iloc[28][0])
            st.image(popular_book_img.iloc[28][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[28][2],2)}')
    
        with col10:
            st.text(popular_book_img.iloc[29][0])
            st.image(popular_book_img.iloc[29][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[29][2],2)}')

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 =st.columns(10)            
    with st.container():
        
        with col1:
            st.text(popular_book_img.iloc[30][0])
            st.image(popular_book_img.iloc[30][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[30][2],2)}')

            
        with col2:
            st.text(popular_book_img.iloc[31][0])
            st.image(popular_book_img.iloc[31][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[31][2],2)}')
                
        with col3:
            st.text(popular_book_img.iloc[32][0])
            st.image(popular_book_img.iloc[32][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[32][2],2)}')
            
        with col4:
            st.text(popular_book_img.iloc[33][0])
            st.image(popular_book_img.iloc[33][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[33][2],2)}')
           
        with col5:
            st.text(popular_book_img.iloc[34][0])
            st.image(popular_book_img.iloc[34][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[34][2],2)}')
            
        with col6:
            st.text(popular_book_img.iloc[35][0])
            st.image(popular_book_img.iloc[35][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[35][2],2)}')
    
        with col7:
            st.text(popular_book_img.iloc[36][0])
            st.image(popular_book_img.iloc[36][3]) 
            st.text(f'Rating:{np.round(popular_book_img.iloc[36][2],2)}')
            
        with col8:
            st.text(popular_book_img.iloc[37][0])
            st.image(popular_book_img.iloc[37][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[37][2],2)}')
       
        with col9:
            st.text(popular_book_img.iloc[38][0])
            st.image(popular_book_img.iloc[38][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[38][2],2)}')
    
        with col10:
            st.text(popular_book_img.iloc[39][0])
            st.image(popular_book_img.iloc[39][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[39][2],2)}')
                
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 =st.columns(10)            
    with st.container():
        
        with col1:
            st.text(popular_book_img.iloc[40][0])
            st.image(popular_book_img.iloc[40][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[40][2],2)}')
            
        with col2:
            st.text(popular_book_img.iloc[41][0])
            st.image(popular_book_img.iloc[41][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[41][2],2)}')
                
        with col3:
            st.text(popular_book_img.iloc[42][0])
            st.image(popular_book_img.iloc[42][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[42][2],2)}')
            
        with col4:
            st.text(popular_book_img.iloc[43][0])
            st.image(popular_book_img.iloc[43][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[43][2],2)}')    
           
        with col5:
            st.text(popular_book_img.iloc[44][0])
            st.image(popular_book_img.iloc[44][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[44][2],2)}')    
            
        with col6:
            st.text(popular_book_img.iloc[45][0])
            st.image(popular_book_img.iloc[45][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[45][2],2)}')
    
        with col7:
            st.text(popular_book_img.iloc[46][0])
            st.image(popular_book_img.iloc[46][3]) 
            st.text(f'Rating:{np.round(popular_book_img.iloc[46][2],2)}')
            
        with col8:
            st.text(popular_book_img.iloc[47][0])
            st.image(popular_book_img.iloc[47][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[47][2],2)}')
       
        with col9:
            st.text(popular_book_img.iloc[48][0])
            st.image(popular_book_img.iloc[48][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[48][2],2)}')
    
        with col10:
            st.text(popular_book_img.iloc[49][0])
            st.image(popular_book_img.iloc[49][3])
            st.text(f'Rating:{np.round(popular_book_img.iloc[49][2],2)}')
    
    
#--------------------------------------------------------------------------------------------------------------------------------
# ----------------------- [TAB 3] -----------------------------------------------------------------------------------------------           
#--------------------------------------------------------------------------------------------------------------------------------
with tab3:
    tab3.header("Most Rated Books")
    st.subheader("More Number of Time Rated Books")
    
    
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 =st.columns(10)  
    with st.container():   
        
        with col1:
            st.text(no_of_times_rated_book_img.iloc[0][0])
            st.image(no_of_times_rated_book_img.iloc[0][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[0][1]}')
            
        with col2:
            st.text(no_of_times_rated_book_img.iloc[1][0])
            st.image(no_of_times_rated_book_img.iloc[1][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[1][1]}')
                
        with col3:
            st.text(no_of_times_rated_book_img.iloc[2][0])
            st.image(no_of_times_rated_book_img.iloc[2][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[2][1]}')
            
        with col4:
            st.text(no_of_times_rated_book_img.iloc[3][0])
            st.image(no_of_times_rated_book_img.iloc[3][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[3][1]}')
           
        with col5:
            st.text(no_of_times_rated_book_img.iloc[4][0])
            st.image(no_of_times_rated_book_img.iloc[4][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[4][1]}')
            
        with col6:
            st.text(no_of_times_rated_book_img.iloc[5][0])
            st.image(no_of_times_rated_book_img.iloc[5][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[5][1]}')
    
        with col7:
            st.text(no_of_times_rated_book_img.iloc[6][0])
            st.image(no_of_times_rated_book_img.iloc[6][3]) 
            st.text(f'Count:{no_of_times_rated_book_img.iloc[6][1]}')
            
        with col8:
            st.text(no_of_times_rated_book_img.iloc[7][0])
            st.image(no_of_times_rated_book_img.iloc[7][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[7][1]}')
       
        with col9:
            st.text(no_of_times_rated_book_img.iloc[8][0])
            st.image(no_of_times_rated_book_img.iloc[8][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[8][1]}')
    
        with col10:
            st.text(no_of_times_rated_book_img.iloc[9][0])
            st.image(no_of_times_rated_book_img.iloc[9][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[9][1]}')
    
    
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 =st.columns(10)
    with st.container():
        
        with col1:
            st.text(no_of_times_rated_book_img.iloc[10][0])
            st.image(no_of_times_rated_book_img.iloc[10][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[10][1]}')
            
        with col2:
            st.text(no_of_times_rated_book_img.iloc[11][0])
            st.image(no_of_times_rated_book_img.iloc[11][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[11][1]}')
                
        with col3:
            st.text(no_of_times_rated_book_img.iloc[12][0])
            st.image(no_of_times_rated_book_img.iloc[12][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[12][1]}')
            
        with col4:
            st.text(no_of_times_rated_book_img.iloc[13][0])
            st.image(no_of_times_rated_book_img.iloc[13][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[13][1]}')
           
        with col5:
            st.text(no_of_times_rated_book_img.iloc[14][0])
            st.image(no_of_times_rated_book_img.iloc[14][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[14][1]}')
            
        with col6:
            st.text(no_of_times_rated_book_img.iloc[15][0])
            st.image(no_of_times_rated_book_img.iloc[15][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[15][1]}')
    
        with col7:
            st.text(no_of_times_rated_book_img.iloc[16][0])
            st.image(no_of_times_rated_book_img.iloc[16][3]) 
            st.text(f'Count:{no_of_times_rated_book_img.iloc[16][1]}')
            
        with col8:
            st.text(no_of_times_rated_book_img.iloc[17][0])
            st.image(no_of_times_rated_book_img.iloc[17][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[17][1]}')
       
        with col9:
            st.text(no_of_times_rated_book_img.iloc[18][0])
            st.image(no_of_times_rated_book_img.iloc[18][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[18][1]}')
    
        with col10:
            st.text(no_of_times_rated_book_img.iloc[19][0])
            st.image(no_of_times_rated_book_img.iloc[19][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[19][1]}')
    
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 =st.columns(10)
    with st.container():
        
        with col1:
            st.text(no_of_times_rated_book_img.iloc[20][0])
            st.image(no_of_times_rated_book_img.iloc[20][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[20][1]}')
            
        with col2:
            st.text(no_of_times_rated_book_img.iloc[21][0])
            st.image(no_of_times_rated_book_img.iloc[21][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[21][1]}')
                
        with col3:
            st.text(no_of_times_rated_book_img.iloc[22][0])
            st.image(no_of_times_rated_book_img.iloc[22][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[22][1]}')
            
        with col4:
            st.text(no_of_times_rated_book_img.iloc[23][0])
            st.image(no_of_times_rated_book_img.iloc[23][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[23][1]}')
           
        with col5:
            st.text(no_of_times_rated_book_img.iloc[24][0])
            st.image(no_of_times_rated_book_img.iloc[24][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[24][1]}')
            
        with col6:
            st.text(no_of_times_rated_book_img.iloc[25][0])
            st.image(no_of_times_rated_book_img.iloc[25][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[25][1]}')
    
        with col7:
            st.text(no_of_times_rated_book_img.iloc[26][0])
            st.image(no_of_times_rated_book_img.iloc[26][3]) 
            st.text(f'Count:{no_of_times_rated_book_img.iloc[26][1]}')
            
        with col8:
            st.text(no_of_times_rated_book_img.iloc[27][0])
            st.image(no_of_times_rated_book_img.iloc[27][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[27][1]}')
       
        with col9:
            st.text(no_of_times_rated_book_img.iloc[28][0])
            st.image(no_of_times_rated_book_img.iloc[28][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[28][1]}')
    
        with col10:
            st.text(no_of_times_rated_book_img.iloc[29][0])
            st.image(no_of_times_rated_book_img.iloc[29][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[29][1]}')

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 =st.columns(10)        
    with st.container():
        
        with col1:
            st.text(no_of_times_rated_book_img.iloc[30][0])
            st.image(no_of_times_rated_book_img.iloc[30][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[30][1]}')
            
        with col2:
            st.text(no_of_times_rated_book_img.iloc[31][0])
            st.image(no_of_times_rated_book_img.iloc[31][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[31][1]}')
                
        with col3:
            st.text(no_of_times_rated_book_img.iloc[32][0])
            st.image(no_of_times_rated_book_img.iloc[32][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[32][1]}')
            
        with col4:
            st.text(no_of_times_rated_book_img.iloc[33][0])
            st.image(no_of_times_rated_book_img.iloc[33][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[33][1]}')
           
        with col5:
            st.text(no_of_times_rated_book_img.iloc[34][0])
            st.image(no_of_times_rated_book_img.iloc[34][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[34][1]}')
            
        with col6:
            st.text(no_of_times_rated_book_img.iloc[35][0])
            st.image(no_of_times_rated_book_img.iloc[35][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[35][1]}')
    
        with col7:
            st.text(no_of_times_rated_book_img.iloc[36][0])
            st.image(no_of_times_rated_book_img.iloc[36][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[36][1]}')
            
        with col8:
            st.text(no_of_times_rated_book_img.iloc[37][0])
            st.image(no_of_times_rated_book_img.iloc[37][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[37][1]}')
       
        with col9:
            st.text(no_of_times_rated_book_img.iloc[38][0])
            st.image(no_of_times_rated_book_img.iloc[38][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[38][1]}')
    
        with col10:
            st.text(no_of_times_rated_book_img.iloc[39][0])
            st.image(no_of_times_rated_book_img.iloc[39][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[39][1]}')
                
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 =st.columns(10)            
    with st.container():
        
        with col1:
            st.text(no_of_times_rated_book_img.iloc[40][0])
            st.image(no_of_times_rated_book_img.iloc[40][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[40][1]}')
            
        with col2:
            st.text(no_of_times_rated_book_img.iloc[41][0])
            st.image(no_of_times_rated_book_img.iloc[41][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[41][1]}')
                
        with col3:
            st.text(no_of_times_rated_book_img.iloc[42][0])
            st.image(no_of_times_rated_book_img.iloc[42][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[42][1]}')
            
        with col4:
            st.text(no_of_times_rated_book_img.iloc[43][0])
            st.image(no_of_times_rated_book_img.iloc[43][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[40][1]}')
           
        with col5:
            st.text(no_of_times_rated_book_img.iloc[44][0])
            st.image(no_of_times_rated_book_img.iloc[44][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[44][1]}')
            
        with col6:
            st.text(no_of_times_rated_book_img.iloc[45][0])
            st.image(no_of_times_rated_book_img.iloc[45][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[45][1]}')
    
        with col7:
            st.text(no_of_times_rated_book_img.iloc[46][0])
            st.image(no_of_times_rated_book_img.iloc[46][3]) 
            st.text(f'Count:{no_of_times_rated_book_img.iloc[46][1]}')
            
        with col8:
            st.text(no_of_times_rated_book_img.iloc[47][0])
            st.image(no_of_times_rated_book_img.iloc[47][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[40][1]}')
       
        with col9:
            st.text(no_of_times_rated_book_img.iloc[48][0])
            st.image(no_of_times_rated_book_img.iloc[48][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[48][1]}')
    
        with col10:
            st.text(no_of_times_rated_book_img.iloc[49][0])
            st.image(no_of_times_rated_book_img.iloc[49][3])
            st.text(f'Count:{no_of_times_rated_book_img.iloc[49][1]}')

with tab4:
    tab4.header("Author Books")
    
    authors_name = books_with_ratings['author'].value_counts().index
    
    selected_author = st.selectbox(
        'Type or Select Book-Title', authors_name
     
    )
    
    def get_books_author(author_name):
        author_books = books_with_ratings[books_with_ratings['author']==author_name][['title', 'Avg_Rating']]
        author_books = author_books.sort_values(by='Avg_Rating',ascending=False)
        return author_books
    
    if st.button('Show Author Books'):
        tab4.subheader(f"Books Written by  ' {selected_author} '")
        books = get_books_author(selected_author)
        st.dataframe(books, width=5000, height=5000)
       
    
with tab5:
    age = st.slider('How old are you?', 0)
    
    
    
    if st.button('Show Books'):
        st.write("You are ", age, 'years old')        
        def get_books_by_age(age):
            if age < 25:
                books = age_with_books[age_with_books.Cluster == 2]
                books = books.sort_values(by='Avg_Rating',ascending=False)
                return books
    
            elif ((age >= 25) & (age <33)):
                books = age_with_books[age_with_books.Cluster == 3]
                books = books.sort_values(by='Avg_Rating',ascending=False)
                return books
    
            elif ((age >= 33) & (age <43)):
                books = age_with_books[age_with_books.Cluster == 0]
                books = books.sort_values(by='Avg_Rating',ascending=False)
                return books
    
            elif ((age >= 43) & (age <56)):
                books = age_with_books[age_with_books.Cluster == 1]
                books = books.sort_values(by='Avg_Rating',ascending=False)
                return books
    
            else:
                books = age_with_books[age_with_books.Cluster == 4]
                books = books.sort_values(by='Avg_Rating',ascending=False)
                return books
        
        age_books = get_books_by_age(age)
        st.dataframe(age_books[['title', 'author', 'Avg_Rating']], width=2000, height=5000)

     
    
with tab6:
    selected_country = st.selectbox(
        'Select Country Name', age_with_books.country.sort_values().unique())
     
    if st.button('Show country Books'):
        books = age_with_books[age_with_books.country == selected_country]
        books = books.sort_values(by=['Avg_Rating'],ascending=False) 
        st.dataframe(books[['title', 'author', 'publisher', 'Avg_Rating']], width = 2000, height = 5000)
