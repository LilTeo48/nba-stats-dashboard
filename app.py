import streamlit as st
import pandas as pd

st.set_page_config(page_title="NBA Stats Dashboard", layout="wide")

st.title("NBA Stats Dashboard")
st.write("Interactive dashboard for analyzing NBA team performance metrics.")

data = {
    "Team": [
        "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets",
        "Chicago Bulls", "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets",
        "Detroit Pistons", "Golden State Warriors", "Houston Rockets", "Indiana Pacers",
        "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat",
        "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans",
        "New York Knicks", "Oklahoma City Thunder", "Orlando Magic",
        "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers",
        "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors",
        "Utah Jazz", "Washington Wizards",
        "Seattle Expansion Team", "Las Vegas Expansion Team"
    ],
    "Wins": [
        36, 64, 32, 21, 39, 48, 50, 57,
        14, 46, 41, 47, 51, 47, 27, 46,
        49, 56, 49, 50, 57, 47,
        47, 49, 21, 46, 22, 25,
        31, 15,
        0, 0
    ],
    "Losses": [
        46, 18, 50, 61, 43, 34, 32, 25,
        68, 36, 41, 35, 31, 35, 55, 36,
        33, 26, 33, 32, 25, 35,
        35, 33, 61, 36, 60, 57,
        51, 67,
        0, 0
    ],
    "Points Per Game": [
        118.3, 120.6, 110.4, 106.6, 112.3, 112.6, 117.9, 114.9,
        109.9, 117.8, 114.3, 123.3, 115.6, 118.0, 105.8, 110.1,
        119.0, 113.0, 115.1, 112.8, 120.1, 110.5,
        114.6, 116.2, 106.4, 116.6, 112.1, 112.4,
        115.7, 113.7,
        0.0, 0.0
    ],
    "Rebounds Per Game": [
        44.7, 46.3, 44.1, 40.3, 43.8, 43.3, 42.9, 44.4,
        43.3, 46.7, 45.5, 41.5, 43.0, 43.1, 42.6, 42.3,
        44.2, 43.6, 44.0, 45.2, 42.0, 42.7,
        43.0, 44.1, 42.7, 44.0, 44.2, 43.7,
        45.5, 41.1,
        0.0, 0.0
    ],
    "Assists Per Game": [
        26.6, 26.9, 25.6, 24.8, 25.0, 28.0, 25.7, 29.5,
        25.5, 29.3, 24.8, 30.8, 25.6, 28.5, 24.7, 25.8,
        26.5, 26.6, 27.0, 24.4, 27.1, 24.7,
        24.9, 27.0, 23.1, 28.3, 29.9, 28.5,
        27.2, 27.9,
        0.0, 0.0
    ],
}

df = pd.DataFrame(data)

df["Win Percentage"] = df.apply(
    lambda row: round(row["Wins"] / (row["Wins"] + row["Losses"]), 3)
    if (row["Wins"] + row["Losses"]) > 0 else 0,
    axis=1
)

st.subheader("Team Statistics")
st.dataframe(df)

selected_team = st.selectbox("Select a team", df["Team"])

team_data = df[df["Team"] == selected_team].iloc[0]

st.subheader(f"{selected_team} Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Wins", int(team_data["Wins"]))
col2.metric("Losses", int(team_data["Losses"]))
col3.metric("Points Per Game", team_data["Points Per Game"])
col4.metric("Win Percentage", team_data["Win Percentage"])

st.subheader("Win Percentage by Team")
st.bar_chart(df.set_index("Team")["Win Percentage"])

st.subheader("Points Per Game by Team")
st.bar_chart(df.set_index("Team")["Points Per Game"])

st.subheader("Wins by Team")
st.bar_chart(df.set_index("Team")["Wins"])