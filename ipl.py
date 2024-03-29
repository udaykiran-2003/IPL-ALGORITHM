
class Team:
    def __init__(self):
        self.name = ""  # Team name
        self.total_matches = 0  # Total matches played by the team
        self.wins = 0  # Total wins by the team
        self.losses = 0  # Total losses by the team
        self.ties = 0  # Total ties by the team
        self.total_points = 0  # Total points earned by the team
        self.probability = 0.0  # Probability of winning
        self.wins_count = 0  # Count of wins in simulations
        self.Nrr = 0.0  # Net Run Rate of the team

    def set_details(self, name, total_matches, wins, losses, ties, Nrr):
        self.name = name
        self.total_matches = total_matches
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.total_points = wins * 2 + ties
        self.wins_count = 0
        self.Nrr = Nrr


# Create a list to store team objects
teams_list = [Team() for _ in range(10)]

# Dictionary to map team name to index in teams_list
team_index_map = {}

# Input team details
print("Enter the points table with feilds team_name, total_matches, wins, losses, ties, Nrr")
for i in range(10):
    name, total_matches, wins, losses, ties, Nrr = input().split()
    total_matches, wins, losses, ties = int(total_matches), int(wins), int(losses), int(ties)
    Nrr = float(Nrr)
    team_index_map[name] = i
    teams_list[i].set_details(name, total_matches, wins, losses, ties, Nrr)

# Calculate the number of remaining matches
remaining_matches_count = 0
for i in range(10):
    remaining_matches_count += (14 - teams_list[i].total_matches)
remaining_matches_count //= 2  # Since each match involves 2 teams

remaining_matches = []
print(f"There are {remaining_matches_count} remaining_matches. Please enter the details of them")
# Input remaining match details
for i in range(remaining_matches_count):
    first_team, second_team = input().split()
    remaining_matches.append((first_team, second_team))

# Calculate total number of permutations of match outcomes
total_permutations = 1 << remaining_matches_count

# Simulate all possible match outcomes
for permutation in range(total_permutations):
    points = {}  # Dictionary to store points for each team
    team_rankings = []  # List to store team rankings based on points and Nrr

    # Initialize points for each team
    for i in range(10):
        points[teams_list[i].name] = teams_list[i].total_points

    # Simulate outcomes of remaining matches
    for i in range(remaining_matches_count):
        if (1 << i) & permutation:  # If the i-th bit of permutation is set
            # (1 << i) & permutation: This part checks if the ith bit of permutation is set to 1. It does so by using the bitwise 
            # left shift operator (<<) to create a bitmask with a single 1 at position i and then performs a bitwise AND operation (&) 
            # with permutation. If the ith bit of permutationis set, then the condition (1 << i) & permutation evaluates to true, indicating 
            # that the outcome of the ith match is represented as "Team 2 wins".
            points[remaining_matches[i][1]] += 2  # Team 2 wins
        else:
            points[remaining_matches[i][0]] += 2  # Team 1 wins

    # Populate team rankings based on points and Nrr
    for i in range(10):
        team_rankings.append((teams_list[i].name, (points[teams_list[i].name], teams_list[i].Nrr)))
    team_rankings.sort(key=lambda x: (-x[1][0], -x[1][1]))  # Sort teams based on points and Nrr

    # Update wins count for top 4 teams
    for i in range(4):
        teams_list[team_index_map[team_rankings[i][0]]].wins_count += 1

# Calculate probability of winning for each team
for i in range(10):
    teams_list[i].probability = (teams_list[i].wins_count * 100) / total_permutations

# Print probabilities for each team
print("These are the final percentage of probabilities of winning the IPL Trophy of each team")
for i in range(10):
    print(teams_list[i].name, teams_list[i].probability, "\n")


# EXAMPLE INPUT
# a 14 10 4 20 0.316
# b 14 9 5 18 0.298
# c 14 9 5 18 0.251
# d 13 7 7 14 -0.253
# e 13 7 7 14 0.204
# f 14 7 7 14 0.216
# g 14 6 8 12 0.416
# h 14 6 8 12 -0.325
# i 14 4 10 8 -0.325
# j 14 4 10 8 -0.256
