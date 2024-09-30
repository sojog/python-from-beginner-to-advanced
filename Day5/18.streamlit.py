import streamlit as st
import pandas as pd

# Sample data with teams, countries, trophies, and the year they won trophies
data = {
    'team': ['Barcelona', 'Man United', 'Inter', 'Chelsea', 'Nottm Forest', 
             'Benfica', 'Juventus', 'FC Porto', 'Man City', 'Dortmund'],
    'country': ['Spain', 'England', 'Italy', 'England', 'England', 
                'Portugal', 'Italy', 'Portugal', 'England', 'Germany'],
    'trophies': [5, 3, 3, 2, 2, 2, 2, 2, 1, 1],
    'year_won': [1992, 1999, 2010, 2012, 1980, 1961, 1996, 1987, 2021, 1997]
}

df = pd.DataFrame(data)

# Title
st.title("Football Teams Query App")

# User question input
user_input = st.text_input("Ask a question (e.g., 'How many trophies has Team X?', 'Who won in 1996?', 'Which team has more trophies than Team Y?', 'Show teams from Country Z', 'Which teams have less than 3 trophies?')")


# Text-based filtering and comparison
if user_input:
    user_input = user_input.lower()  # Normalize the user input to lowercase for easier matching
    
    # Check for "how many trophies" type of question
    if "how many trophies" in user_input:
        team = user_input.split("team")[-1].strip()  # Extract the team name
        result = df[df['team'].str.lower().str.contains(team)]
        if not result.empty:
            st.write(f"### {team.title()} has won {result['trophies'].values[0]} trophies.")
        else:
            st.write(f"### Team {team.title()} not found.")
    
    # Check for "who won in" type of question
    elif "who won in" in user_input:
        try:
            year = int(user_input.split("in")[-1].strip())  # Extract the year
            result = df[df['year_won'] == year]
            if not result.empty:
                st.write(f"### The team that won in {year} is {result['team'].values[0]}.")
            else:
                st.write(f"### No data found for the year {year}.")
        except ValueError:
            st.write("### Please provide a valid year.")
    
    # Check for "more trophies" or "less trophies" comparison
    elif "more trophies" in user_input or "less trophies" in user_input:
        parts = user_input.split("than")
        if len(parts) == 2:
            team_1 = parts[0].split("more trophies" if "more" in user_input else "less trophies")[-1].strip()
            team_2 = parts[1].strip()
            
            team_1_data = df[df['team'].str.lower().str.contains(team_1)]
            team_2_data = df[df['team'].str.lower().str.contains(team_2)]
            
            if not team_1_data.empty and not team_2_data.empty:
                trophies_1 = team_1_data['trophies'].values[0]
                trophies_2 = team_2_data['trophies'].values[0]
                
                if "more" in user_input:
                    if trophies_1 > trophies_2:
                        st.write(f"### {team_1.title()} has more trophies than {team_2.title()}.")
                    else:
                        st.write(f"### {team_1.title()} does not have more trophies than {team_2.title()}.")
                elif "less" in user_input:
                    if trophies_1 < trophies_2:
                        st.write(f"### {team_1.title()} has fewer trophies than {team_2.title()}.")
                    else:
                        st.write(f"### {team_1.title()} does not have fewer trophies than {team_2.title()}.")
            else:
                st.write("### One or both teams not found.")
    
    else:
        st.write("### Sorry, I don't understand that question.")
