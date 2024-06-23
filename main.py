
# Librairies

import pandas as pd
import streamlit as st


# Import data and preparatior

df= pd.read_csv('male_players.csv')
df= df.drop(labels=['Unnamed: 0','URL','Gender'],axis=1)
df['GK']=df['GK'].fillna(0)
df['Weak foot']=df['Weak foot']*20
df['Skill moves']=df['Skill moves']*20

list_nations=df['Nation'].unique()
list_club=df['Club'].unique()
list_player=df['Name'].unique()


# Title
st.title('Fifa 24 - Male Players Roster -')
st.sidebar.title('Menu')
st.sidebar.header('Select/Comparison Mode')
mode=st.sidebar.radio('Selection Mode',['Selection', 'Comparison'])

if mode=='Comparison':
    comp_radio=st.sidebar.radio('What do you want to compare?',['Nations','Clubs','Players'],captions=['France, Spain, England...','Paris SG, Brentford...','Lionel Messi...'])
    if comp_radio=='Nations':
        nat_comp= st.multiselect('Choose the Nations to compare.',list_nations)



    if comp_radio =='Clubs':
        club_comp= st.multiselect('Choose the Clubs to compare.',list_club)


    if comp_radio=='Players':
        play_comp=st.multiselect('Choose the Players to compare.',list_player)



   


    

else:
    #st.sidebar.header('Comparison Mode')
    sel_radio=st.sidebar.radio('What do you search?',['Nation','Club','Player'],captions=['France, Spain, England...','Paris SG, Brentford...','Lionel Messi...'])
    if sel_radio=='Nation':
        option=st.selectbox('Choose a nation',list_nations)
        df_nation_sel=df[df['Nation']==option]
        st.dataframe(df_nation_sel)

    if sel_radio=='Club':
        option2=st.selectbox('Choose a Club',list_club)
        df_club_sel=df[df['Club']==option2]
        st.dataframe(df_club_sel)

    if sel_radio=='Player':
        option3=st.selectbox('Choose a Player',list_player)
        df_player_sel=df[df['Name']==option3]
        st.dataframe(df_player_sel)



    

