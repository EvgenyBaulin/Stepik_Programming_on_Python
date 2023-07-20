def process_results(results):
	teams = {}
	for result in results:
		team1, score1, team2, score2 = result.split(";")
		score1, score2 = int(score1), int(score2)

		if team1 not in teams:
			teams[team1] = {"games": 0, "wins": 0, "draws": 0, "losses": 0, "points": 0}

		if team2 not in teams:
			teams[team2] = {"games": 0, "wins": 0, "draws": 0, "losses": 0, "points": 0}

		teams[team1]["games"] += 1
		teams[team2]["games"] += 1

		if score1 > score2:
			teams[team1]["wins"] += 1
			teams[team1]["points"] += 3
			teams[team2]["losses"] += 1
		elif score1 < score2:
			teams[team2]["wins"] += 1
			teams[team2]["points"] += 3
			teams[team1]["losses"] += 1
		else:
			teams[team1]["draws"] += 1
			teams[team2]["draws"] += 1
			teams[team1]["points"] += 1
			teams[team2]["points"] += 1

	return teams


def print_summary_table(teams):
	for team, data in teams.items():
		print(f"{team}:{data['games']} {data['wins']} {data['draws']} {data['losses']} {data['points']}")


n = int(input())
results = []
for _ in range(n):
	results.append(input())

team_results = process_results(results)
print_summary_table(team_results)
