import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Md Arman Hossen')

st.info('PhD Student, University of Luxembourg')

icon_size = 20

#st_button('youtube', 'https://youtube.com/dataprofessor', 'Data Professor YouTube channel', icon_size)
#st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
st_button('medium', 'https://armanruet.medium.com/', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/arman_5227', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/armanruet/', 'Follow me on LinkedIn', icon_size)
#st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
#st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
#st_button('GoogleScholar', 'https://scholar.google.com/citations?user=LN-2sIoAAAAJ&hl=en', 'visit my Google scholar page', icon_size)
#st_button('github', 'https://github.com/armanruet', 'Github', icon_size)
