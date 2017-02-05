#######################
# Soctopus Prediction #
#######################

# Define our default variables
teams = []
winningTeam = ""
winningTeamLength = 0

# Ask the user to input team names until we have the required amount of teams
while len(teams) < 2:
    teams.append(input("Team " + str(len(teams) + 1) + ": "))

# Loop through our teams and find a winner
for team in teams:
    # Get the teams length
    teamLength = len(team)
    # Check the teams length against the current winning team
    if teamLength > winningTeamLength:
        # This team is currently winning!
        winningTeam = team
        winningTeamLength = teamLength
    elif winningTeamLength == teamLength:
        # Looks like a draw \o/
        winningTeam = "Draw"

# Print the winning teams name
print(winningTeam)
