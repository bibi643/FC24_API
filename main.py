
# Librairies

import pandas as pd
import streamlit as st
import plotly.express as px
from funct import select_nation, select_player_nation, plot_player_nation, select_club, select_club_player, plot_player_club, player_radar, players_comp,club_comparison


# Import data and preparation
########################################################################################
df= pd.read_csv('male_players.csv')
df= df.drop(labels=['Unnamed: 0','URL','Gender'],axis=1)
df['GK']=df['GK'].fillna(0)
df['Weak foot']=df['Weak foot']*20
df['Skill moves']=df['Skill moves']*20
df['GK']=df['GK'].astype(int)

list_nations=df['Nation'].unique()
list_club=df['Club'].unique()
list_player=df['Name'].unique()
#########################################################################################

# Title
st.title('Fifa 24 - Male Players Roster -')
st.sidebar.title('Menu')
st.sidebar.header('Select/Comparison Mode')
mode=st.sidebar.radio('Selection Mode',['Selection', 'Comparison'])

if mode=='Comparison':
    comp_radio=st.sidebar.radio('What do you want to compare?',['Clubs','Players'],captions=['France, Spain, England...','Paris SG, Brentford...','Lionel Messi...'])
    
    if comp_radio =='Clubs':
        club_comp= st.multiselect('Choose the Clubs to compare.',list_club)
        list_cat_club= st.multiselect('Choose the Stats to compare.',df.select_dtypes(include=int).columns)
        fig,fig2=club_comparison(df,club_comp,list_cat_club)
        st.plotly_chart(fig)
        st.plotly_chart(fig2)

    if comp_radio=='Players':
        play_list=st.multiselect('Choose the Players to compare.',list_player)
        list_cat= st.multiselect('Choose the Stats to compare.',df.select_dtypes(include=int).columns)
        # list_cat.append('Name')
        fig,fig2=players_comp(df,play_list,list_cat)
        st.plotly_chart(fig)
        st.plotly_chart(fig2)


   


    

else:
    #st.sidebar.header('Comparison Mode')
    sel_radio=st.sidebar.radio('What do you search?',['Nation','Club','Player'],captions=['France, Spain, England...','Paris SG, Brentford...','Lionel Messi...'])
    if sel_radio=='Nation':

        nation=st.selectbox('Choose a nation',list_nations)
        df_nation=select_nation(df,nation)
        st.dataframe(df_nation)

        
        
        # df_nation_sel=df[df['Nation']==nation]

        # st.dataframe(df_nation_sel)
        player_from_nation=df_nation['Name'].unique()
        #player_from_nation= df_nation_sel['Name'].unique()
        nation_player=st.selectbox('Choose a player from nation',player_from_nation)
        df_player_nation,player_nation=select_player_nation(df_nation,nation_player)
        st.dataframe(df_player_nation)

        # df_nation_player=df_nation_sel[df_nation_sel['Name']==nation_player]
        # st.dataframe(df_nation_player)



        list_cat=st.multiselect('Choose the categories to see',df.select_dtypes(include=int).columns)
        fig=plot_player_nation(df_player_nation,player_nation,list_cat)
        st.plotly_chart(fig)
        # df_nation_player=df_nation_player[list_cat]
        # st.dataframe(df_nation_player)
        # fig=px.bar(df_nation_player)
        # st.plotly_chart(fig)
        


    if sel_radio=='Club':
        club=st.selectbox('Choose a Club',list_club)
        list_cat_club=st.multiselect('Choose the categories to see',df.select_dtypes(include=int).columns)
        
        df_club,fig=select_club(df,club,list_cat_club)
        st.dataframe(df_club)
        st.plotly_chart(fig)

        # df_club_sel=df[df['Club']==club]
        # st.dataframe(df_club_sel)

        player_from_club=df_club['Name'].unique()
        club_player=st.selectbox('Choose a player from club.',player_from_club)
        df_player_club=select_club_player(df_club,club_player)
        st.dataframe(df_player_club)
        # df_club_player= df_club_sel[df_club_sel['Name']==club_player]
        # st.dataframe(df_club_player)

        #list_cat=st.multiselect('Choose the categories to see',df.select_dtypes(include=int).columns)
        fig=plot_player_club(df_player_club,club_player,list_cat_club)
        st.plotly_chart(fig)


    if sel_radio=='Player':
        player_name=st.selectbox('Choose a Player',list_player)
        list_cat=st.multiselect('Choose the categories to see',df.select_dtypes(include=int).columns)
        # df_player_sel=df[df['Name']==option3]
        df_player, fig=player_radar(df,player_name,list_cat)
        
        st.dataframe(df_player)
        st.plotly_chart(fig)



    

