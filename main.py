import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Ardit Sulce')
    content = '''
    raspberry pi
    '''
    st.info(content)

content2 = ''' 
Blow you can find some of the apps I have built in Python. Feel to contact me!
'''

st.write(content2)