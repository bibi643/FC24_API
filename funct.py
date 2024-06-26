
import streamlit as st
import plotly.express as px
import pandas as pd

# Select a Nation
#nation=st.selectbox('Choose a nation',list_nations)
def select_nation(df,nation:str):
    '''Return the dataframe of the Nation
    Return a graph with the stat choosen by the user
    Return The player oof this nation with his stats
    Return a grpah for the player and stst choosen by the user.
    Take in argument the nation'''
    
    df_nation= df[df['Nation']==nation]
    df_nation=df_nation.reset_index().drop(columns='index')
    #st.dataframe(df_nation)
    return df_nation




# Select a Player from a Specific nation

def select_player_nation(df_nation,nation_player):
    '''Return the player from a specifice nation
    Takes in argument the dataframe of the Nation selected previously'''
    players_nation=df_nation['Name'].unique()
    #player_nation=st.selectbox('Player from Nation',players_nation)
    df_player_nation=df_nation[df_nation['Name']==nation_player]
    df_player_nation=df_player_nation.reset_index().drop(columns='index')
    #st.dataframe(df_player_nation)
    return df_player_nation, nation_player




# Plot player stats from a specific nation

def plot_player_nation(dataframe_player_nation,player_nation,list_cat):
    '''plot the bar graph for a specific player of a specific nation
    Take in arguments a dataframe of a specific nation and a player name'''
    dataframe_player_nation=dataframe_player_nation.select_dtypes(include=int)
    dataframe_player_nation=dataframe_player_nation[list_cat]
    df_long=pd.melt(dataframe_player_nation,var_name='Stat_Name',value_name='Value')
    fig=px.bar(df_long,x='Stat_Name',y='Value',title=player_nation)
    fig.update_xaxes(tickangle=45)
    return fig



# def select_club(df,club:str):
#     '''Returns The club roster from the user selection
#     Takes in argument a club '''
#     df_club= df[df['Club']==club]
#     df_club=df_club.reset_index().drop(columns='index')
#     return df_club


def select_club(df,club:str,list_stat):
    '''Returns The club roster from the user selection
    Takes in argument a club '''
    df_club= df[df['Club']==club]
    df_club=df_club.reset_index().drop(columns='index')
    df_club2=df_club.select_dtypes(include=int)
    df_club2=df_club2[list_stat]
    df_club_median=df_club2.median(axis=0) # Axis is 0!!!
    df_club_median=df_club_median.to_frame()
    df_club_median=df_club_median.reset_index().rename(columns={'index':'Stat_Name',
                                                0:'Value'})
    fig = px.line_polar(df_club_median, r='Value', theta='Stat_Name', line_close=True)
    fig.update_traces(fill='toself')

    return df_club,fig




def select_club_player(df_club,club_player):
    '''Returns a dataframe for a specifici player of a speicifc club
    Takes in argument a dataframe for a specific club'''
    #players_club= df_club['Name'].unique()
    #player_club=st.selectbox('player from Club',players_club)
    df_player_club=df_club[df_club['Name']==club_player]
    df_player_club=df_player_club.reset_index().drop(columns='index')
    # st.dataframe(df_player_club)
    return df_player_club




def plot_player_club(dataframe_player_club,player_club,list_cat):
    '''plot the bar graph for a specific player of a specific club
    Take in arguments a dataframe of a specific club and a player name'''

    dataframe_player_club=dataframe_player_club.select_dtypes(include=int)
    dataframe_player_club=dataframe_player_club[list_cat]
    df_long=pd.melt(dataframe_player_club,var_name='Stat_Name',value_name='Value')
    fig=px.bar(df_long,x='Stat_Name',y='Value',title=player_club)
    fig.update_xaxes(tickangle=45)
    return fig




def player_radar(df,player_name,list_cat):
    '''Return a polar graph for a specific player and stats choosen by the user anbd the corresponding df
    Takes in argument a dateframe, a player, and list of stats'''
    df_player=df[df['Name']==player_name]
    df_player_cat=df_player[list_cat]
    df_player_long=pd.melt(df_player_cat,var_name='Stat_Name',value_name='Value')
    fig = px.line_polar(df_player_long, r='Value', theta='Stat_Name', line_close=True)
    fig.update_traces(fill='toself')
    return df_player,fig









def players_comp(df,player_list,list_cat):
    df_players_comp=df[df['Name'].isin(player_list)]
    list_cat.append('Name')
    df_players_comp=df_players_comp[list_cat]
    df_players_comp=df_players_comp.reset_index().drop(columns='index')
    #df_players_comp=df_players_comp.select_dtypes(include=int).columns
    melt_df=pd.melt(df_players_comp,id_vars=['Name'],value_vars=df_players_comp.select_dtypes(include=int).columns,var_name='Stats',value_name='Stats_value')
    fig=px.bar(melt_df,x='Stats',y='Stats_value',color='Name',barmode='group')
    fig2= px.line_polar(melt_df, r="Stats_value", theta="Stats", color="Name",line_close=True)
    fig2.update_traces(fill='toself')
    return fig,fig2




def club_comparison(df,clubs_list,list_cat):
    '''Return graphs to compare multiple clubs by the median of their stats
    Take in argument a df, a list of clubs and a list of stat categories'''
    df_clubs_comp=df[df['Club'].isin(clubs_list)]
    list_cat.append('Club')
    df_clubs_comp=df_clubs_comp[list_cat]
    df_clubs_comp=df_clubs_comp.groupby(['Club']).median().reset_index()
    melt_df=pd.melt(df_clubs_comp,id_vars=['Club'],value_vars=df_clubs_comp.select_dtypes(include=float).columns,var_name='Stats',value_name='Stats_value')
    fig=px.bar(melt_df,x='Stats',y='Stats_value',color='Club',barmode='group')
    fig2= px.line_polar(melt_df, r="Stats_value", theta="Stats", color="Club",line_close=True)
    fig2.update_traces(fill='toself')
    return fig,fig2