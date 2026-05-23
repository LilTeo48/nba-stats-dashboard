import streamlit as st
import pandas as pd
import plotly.express as px

team_logos = {
    "Miami Heat": "assets/logos/heat.png",
    "Boston Celtics": "assets/logos/celtics.png",
    "Golden State Warriors": "assets/logos/warriors.png",
    "Los Angeles Lakers": "assets/logos/lakers.png",
    "Denver Nuggets": "assets/logos/nuggets.png",
    "Chicago Bulls": "assets/logos/bulls.png",
    "New York Knicks": "assets/logos/knicks.png",
    "Dallas Mavericks": "assets/logos/mavericks.png",
    "Phoenix Suns": "assets/logos/suns.png",
    "Milwaukee Bucks": "assets/logos/bucks.png",
    "Atlanta Hawks": "assets/logos/hawks.png",
    "Brooklyn Nets": "assets/logos/nets.png",
    "Charlotte Hornets": "assets/logos/hornets.png",
    "Cleveland Cavaliers": "assets/logos/cavaliers.png",
    "Detroit Pistons": "assets/logos/pistons.png",
    "Houston Rockets": "assets/logos/rockets.png",
    "Indiana Pacers": "assets/logos/pacers.png",
    "Los Angeles Clippers": "assets/logos/clippers.png",
    "Memphis Grizzlies": "assets/logos/grizzlies.png",
    "Minnesota Timberwolves": "assets/logos/timberwolves.png",
    "New Orleans Pelicans": "assets/logos/pelicans.png",
    "Oklahoma City Thunder": "assets/logos/thunder.png",
    "Orlando Magic": "assets/logos/magic.png",
    "Philadelphia 76ers": "assets/logos/sixers.png",
    "Portland Trail Blazers": "assets/logos/blazers.png",
    "Sacramento Kings": "assets/logos/kings.png",
    "San Antonio Spurs": "assets/logos/spurs.png",
    "Toronto Raptors": "assets/logos/raptors.png",
    "Utah Jazz": "assets/logos/jazz.png",
    "Washington Wizards": "assets/logos/wizards.png",
}

team_colors = {
    "Atlanta Hawks": "#E03A3E",
    "Boston Celtics": "#007A33",
    "Brooklyn Nets": "#000000",
    "Charlotte Hornets": "#1D1160",
    "Chicago Bulls": "#CE1141",
    "Cleveland Cavaliers": "#860038",
    "Dallas Mavericks": "#00538C",
    "Denver Nuggets": "#0E2240",
    "Detroit Pistons": "#C8102E",
    "Golden State Warriors": "#1D428A",
    "Houston Rockets": "#CE1141",
    "Indiana Pacers": "#FDBB30",
    "Los Angeles Clippers": "#C8102E",
    "Los Angeles Lakers": "#552583",
    "Memphis Grizzlies": "#5D76A9",
    "Miami Heat": "#98002E",
    "Milwaukee Bucks": "#00471B",
    "Minnesota Timberwolves": "#0C2340",
    "New Orleans Pelicans": "#0C2340",
    "New York Knicks": "#F58426",
    "Oklahoma City Thunder": "#007AC1",
    "Orlando Magic": "#0077C0",
    "Philadelphia 76ers": "#006BB6",
    "Phoenix Suns": "#1D1160",
    "Portland Trail Blazers": "#E03A3E",
    "Sacramento Kings": "#5A2D81",
    "San Antonio Spurs": "#C4CED4",
    "Toronto Raptors": "#CE1141",
    "Utah Jazz": "#002B5C",
    "Washington Wizards": "#002B5C",
    "Seattle Expansion Team": "#2E8B57",
    "Las Vegas Expansion Team": "#B8860B",
    
}


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

historical_data = {
    "Season": ["2021-22", "2022-23", "2023-24", "2024-25"],
    "Atlanta Hawks": [43, 41, 36, 36],
    "Boston Celtics": [51, 57, 64, 61],
    "Brooklyn Nets": [44, 45, 32, 26], 
    "Charlotte Hornets": [43, 27, 21, 19],
    "Chicago Bulls": [46, 40, 39, 39], 
    "Cleveland Cavaliers": [44, 51, 48, 64],
    "Dallas Mavericks": [52, 38, 50, 39],
    "Denver Nuggets": [48, 53, 57, 50], 
    "Detroit Pistons": [23, 17, 14, 44],
    "Golden State Warriors": [53, 44, 46, 48],
    "Houston Rockets": [20, 22, 41, 52],
    "Indiana Pacers": [25, 35, 47, 50],
    "Los Angeles Clippers": [42, 44, 51, 50],
    "Los Angeles Lakers": [33, 43, 47, 50], 
    "Memphis Grizzlies": [56, 51, 27, 48], 
    "Miami Heat": [53, 44, 46, 37], 
    "Milwaukee Bucks": [51, 58, 49, 48],
    "Minnesota Timberwolves": [46, 42, 56, 49],
    "New Orleans Pelicans": [36, 42, 49, 21],
    "New York Knicks": [37, 47, 50, 51],
    "Oklahoma City Thunder": [24, 40, 57, 68],
    "Orlando Magic": [22, 34, 47, 41],
    "Philadelphia 76ers": [51, 54, 47, 24],
    "Phoenix Suns": [64, 45, 49, 36],
    "Portland Trail Blazers": [27, 33, 21, 36],
    "Sacramento Kings": [30, 48, 46, 40],
    "San Antonio Spurs": [34, 22, 22, 34],
    "Toronto Raptors": [48, 41, 25, 30],
    "Utah Jazz": [49, 37, 31, 17],
    "Washington Wizards": [35, 35, 15, 18],
    

}
historical_df = pd.DataFrame(historical_data)

team_conferences = {
"Atlanta Hawks" : "Eastern",
"Boston Celtics": "Eastern", 
"Brooklyn Nets": "Eastern", 
"Charlotte Hornets": "Eastern", 
"Chicago Bulls": "Eastern", 
"Cleveland Cavaliers": "Eastern", 
"Detroit Pistons": "Eastern", 
"Indiana Pacers": "Eastern", 
"Miami Heat": "Eastern", 
"Milwaukee Bucks": "Eastern", 
"New York Knicks": "Eastern", 
"Orlando Magic": "Eastern", 
"Philadelphia 76ers": "Eastern", 
"Toronto Raptors": "Eastern", 
"Washington Wizards": "Eastern", 


"Dallas Mavericks": "Western", 
"Denver Nuggets": "Western", 
"Golden State Warriors": "Western", 
"Houston Rockets": "Western", 
"Los Angeles Clippers": "Western", 
"Los Angeles Lakers": "Western", 
"Memphis Grizzlies": "Western", 
"Minnesota Timberwolves": "Western", 
"New Orleans Pelicans": "Western", 
"Oklahoma City Thunder": "Western", 
"Phoenix Suns": "Western", 
"Portland Trail Blazers": "Western", 
"Sacramento Kings": "Western", 
"San Antonio Spurs": "Western", 
"Utah Jazz": "Western", 

"Seattle Expansion Team": "Expansion", 
"Las Vegas Expansion Team": "Expansion",


}

df = pd.DataFrame(data)

df["Conference"] = df["Team"].map(team_conferences)

df["Win Percentage"] = df.apply(
    lambda row: round(row["Wins"] / (row["Wins"] + row["Losses"]), 3)
    if (row["Wins"] + row["Losses"]) > 0 else 0,
    axis=1
)

st.sidebar.header("Dashboard Filters")

team_search = st.sidebar.text_input("Search for a team")

filtered_teams = df[
    df["Team"].str.contains(team_search, case=False)
]["Team"].tolist()

if not filtered_teams:
    filtered_teams = df["Team"].tolist()

selected_team = st.sidebar.selectbox(
    "Select a team",
    filtered_teams
)


selected_metric = st.sidebar.selectbox(
    "Select a metric",
    ["Wins", "Losses", "Points Per Game", "Rebounds Per Game", "Assists Per Game", "Win Percentage"]
)

selected_conference = st.sidebar.selectbox(
    "Select conference", 
    ["All", "Eastern", "Western", "Expansion"]
)

filtered_df = df.copy()

if selected_conference != "All": 
    filtered_df = filtered_df[filtered_df["Conference"] == selected_conference]

selected_historical_teams = st.sidebar.multiselect(
    "Historical teams",
    list(historical_df.columns[1:]),
    default=["Boston Celtics", "Miami Heat", "Denver Nuggets"]
)

selected_seasons = st.sidebar.multiselect(
    "Historical seasons",
    historical_df["Season"],
    default=list(historical_df["Season"])
)

overview_tab, comparison_tab, historical_tab = st.tabs(
    ["Overview", "Team Comparison", "Historical Trends"]
)

with overview_tab:
    st.subheader("Team Statistics")
    st.dataframe(filtered_df)

    st.subheader("Standings")
    # standings code
    # top teams code
    # selected team summary code
    # win percentage chart
    # PPG chart
    # wins chart
    # selected metric chart

with comparison_tab:
    st.subheader("Team Comparison Mode")
    # team comparison dropdowns
    # comparison table
    # comparison chart

with historical_tab:
    st.subheader("Historical Season Wins Comparison")
    # filtered_historical_df code
    # historical line chart

st.subheader("Team Statistics")

def highlight_conference(row): 
    if row["Conference"] == "Eastern": 
        return ["background-color: rgba(0, 122, 51, 0.18)"] * len(row)
    elif row["Conference"] == "Western":
        return ["background-color: rgba(29, 66, 138, 0.18)"] * len(row)
    elif row["Conference"] == "Expansion": 
        return ["background-color: rgba(180, 180, 180, 0.18)"] * len(row)  
    return [""] * len(row)



st.dataframe(filtered_df)

st.subheader("Standings")

if selected_conference == "All":
    standings_title = "Overall NBA Standings"
elif selected_conference == "Expansion": 
    standings_title = "Expansion Team Standings"
else: 
    standings_title = f"{selected_conference} Conference Standings" 

st.markdown(f'### {standings_title}')

standings_df = filtered_df.sort_values(
    by = ["Win Percentage", "Wins"], 
    ascending = False 
).reset_index(drop=True)

standings_df.index += 1
standings_df.index.name = "Rank"

def get_seed_status(rank):
    if rank <= 6:
        return "🟢 Playoffs"
    elif rank <= 10:
        return "🟡 Play-In"
    else:
        return "🔴 Lottery"

standings_df["Seed Status"] = [
    get_seed_status(rank)
    for rank in standings_df.index
]               

styled_standings = standings_df[
    ["Team", "Conference", "Wins", "Losses", "Win Percentage", "Seed Status"]
].style.apply(highlight_conference, axis=1)

st.dataframe(styled_standings)


team_data = df[df["Team"] == selected_team].iloc[0]

st.subheader("Top Teams")

top_team = standings_df.iloc[0]

best_offense = filtered_df.loc[
    filtered_df["Points Per Game"].idxmax()
]

best_assists = filtered_df.loc[
    filtered_df["Assists Per Game"].idxmax()
]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Best Record",
    top_team["Team"], 
    f'{top_team["Wins"]}-{top_team["Losses"]}'
)

col2.metric(
    "Highest Scoring Team", 
    best_offense["Team"],
    f'{best_offense["Points Per Game"]} PPG'
)
col3.metric(
    "Best Passing Team",
    best_assists["Team"],
    f'{best_assists["Assists Per Game"]} APG'
)


st.subheader("Team Comparison Mode")

team_a, team_b = st.columns(2)

with team_a: 
    compare_team_1 = st.selectbox(
        "Select first team",
        df["Team"],
        index=0
    )

with team_b: 
    compare_team_2 = st.selectbox(
        "Select second team", 
        df["Team"],
        index=1
    )
team_1_data = df[df["Team"] == compare_team_1].iloc[0]
team_2_data = df[df["Team"] == compare_team_2].iloc[0]

comparison_df = pd.DataFrame({
    "Metric": [
        "Wins",
        "Losses",
        "Points Per Game",
        "Rebounds Per Game",
        "Assists Per Game",
        "Win Percentage"
    ],
    compare_team_1: [
        team_1_data["Wins"],
        team_1_data["Losses"],
        team_1_data["Points Per Game"],
        team_1_data["Rebounds Per Game"],
        team_1_data["Assists Per Game"],
        team_1_data["Win Percentage"]
    ],
    compare_team_2: [
        team_2_data["Wins"],
        team_2_data["Losses"],
        team_2_data["Points Per Game"],
        team_2_data["Rebounds Per Game"],
        team_2_data["Assists Per Game"],
        team_2_data["Win Percentage"]
    ]
})

st.dataframe(comparison_df)

comparison_long_df = comparison_df.melt(
    id_vars="Metric",
    var_name="Team",
    value_name="Value"
)

fig_comparison = px.bar(
    comparison_long_df,
    x="Metric",
    y="Value",
    color="Team",
    barmode="group",
    color_discrete_map=team_colors,
    title=f"{compare_team_1} vs {compare_team_2}"
)

fig_comparison.update_layout(
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    font=dict(color="white")
)

st.plotly_chart(fig_comparison, use_container_width=True)    

st.subheader(f"{selected_team} Summary")

if selected_team in team_logos:
    st.image(team_logos[selected_team], width=150)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Wins", int(team_data["Wins"]))
col2.metric("Losses", int(team_data["Losses"]))
col3.metric("Points Per Game", team_data["Points Per Game"])
col4.metric("Win Percentage", team_data["Win Percentage"])

st.subheader("Win Percentage by Team")

fig_win_pct = px.bar(
    filtered_df.sort_values(by="Win Percentage", ascending=False),
    x="Team",
    y="Win Percentage",
    color="Team",
    color_discrete_map=team_colors,
    hover_data=["Wins", "Losses", "Points Per Game"],
    title="NBA Team Win Percentage"
)
fig_win_pct.update_layout(
    showlegend=False,
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    font=dict(color="white")
    
)

st.plotly_chart(fig_win_pct, use_container_width=True)

st.subheader("Points Per Game by Team")

fig_ppg = px.bar( 
    filtered_df.sort_values(by="Points Per Game", ascending=False),
    x="Team", 
    y="Points Per Game", 
    color="Team",
    color_discrete_map=team_colors,
    hover_data=["Wins", "Losses", "Win Percentage"],
    title="NBA Team Points Per Game"
)
fig_ppg.update_layout(
    showlegend=False,
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    font=dict(color="white")
    
)


st.plotly_chart(fig_ppg, use_container_width=True)

st.subheader("Wins by Team")

fig_wins = px.bar(
    filtered_df.sort_values(by="Wins", ascending=False),
    x="Team",
    y="Wins",
    color="Team",
    color_discrete_map=team_colors,
    hover_data=["Losses", "Win Percentage", "Points Per Game"],
    title="NBA Team Wins"
)
fig_wins.update_layout(
    showlegend=False,
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    font=dict(color="white")
    
)

st.plotly_chart(fig_wins, use_container_width=True)

st.subheader(f"{selected_metric} by Team")

fig_selected_metric = px.bar(
    filtered_df.sort_values(by=selected_metric, ascending=False),
    x="Team",
    y=selected_metric,
    color="Team",
    color_discrete_map=team_colors,
    hover_data=["Wins", "Losses", "Points Per Game", "Win Percentage"],
    title=f"NBA Team {selected_metric}"
)

fig_selected_metric.update_layout(
    showlegend=False,
    template="plotly_dark",
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    font=dict(color="white")
)

st.plotly_chart(fig_selected_metric, use_container_width=True)

st.subheader("Historical Season Wins Comparison")

filtered_historical_df = historical_df[
    historical_df["Season"].isin(selected_seasons)
]

if selected_historical_teams:
    fig_history = px.line(
        filtered_historical_df,
        x="Season",
        y=selected_historical_teams,
        markers=True,
        title="Historical Wins by Season"
    )

    fig_history.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#0E1117",
        font=dict(color="white")
    )

    st.plotly_chart(fig_history, use_container_width=True)