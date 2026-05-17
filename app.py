import streamlit as st
import pandas as pd

st.set_page_config(page_title="NBA Stats Dashboard", layout="wide")

st.title("NBA Stats Dashboard")
st.write("Interactive dashboard for analyzing NBA team performance metrics.")

data = {
    "Team": ["Miami Heat", "Boston Celtics", "Denver Nuggets", "Los Angeles Lakers", "Golden State Warriors"],
    "Wins": [46, 64, 57, 47, 46],
    "Losses": [36, 18, 25, 35, 36],
    "Points Per Game": [110.1, 120.6, 114.9, 118.0, 117.8],
    "Rebounds Per Game": [42.3, 46.3, 44.4, 43.1, 46.7],
    "Assists Per Game": [25.8, 26.9, 29.5, 28.5, 29.3],
}

df = pd.DataFrame(data)

st.subheader("Team Statistics")
st.dataframe(df)

selected_team = st.selectbox("Select a team", df["Team"])

team_data = df[df["Team"] == selected_team].iloc[0]

st.subheader(f"{selected_team} Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Wins", int(team_data["Wins"]))
col2.metric("Losses", int(team_data["Losses"]))
col3.metric("Points Per Game", team_data["Points Per Game"])

st.subheader("Points Per Game by Team")
st.bar_chart(df.set_index("Team")["Points Per Game"])

st.subheader("Wins by Team")
st.bar_chart(df.set_index("Team")["Wins"])