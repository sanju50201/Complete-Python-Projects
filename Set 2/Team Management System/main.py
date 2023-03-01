import json


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)
            print(f"{member} has been removed from {self.name}")
        else:
            print(f"{member} is not a member of {self.name}")

    def edit_member_name(self, old_name, new_name):
        if old_name in self.members:
            self.members[self.members.index(old_name)] = new_name
            print(f"{old_name} has been renamed to {new_name}")
        else:
            print(f"{old_name} is not a member of {self.name}")


class TeamManagementSystem:
    def __init__(self):
        self.teams = {}

    def create_team(self, team_name):
        if team_name in self.teams:
            print(f"{team_name} already exists")
        else:
            self.teams[team_name] = Team(team_name)
            print(f"{team_name} has been created")

    def rename_team(self, old_name, new_name):
        if old_name in self.teams:
            if new_name in self.teams:
                print(f"{new_name} already exists")
            else:
                team = self.teams.pop(old_name)
                team.name = new_name
                self.teams[new_name] = team
                print(f"{old_name} has been renamed to {new_name}")
        else:
            print(f"{old_name} does not exist")

    def remove_team(self, team_name):
        if team_name in self.teams:
            self.teams.pop(team_name)
            print(f"{team_name} has been removed")
        else:
            print(f"{team_name} does not exist")

    def add_member_to_team(self, team_name, member):
        if team_name in self.teams:
            team = self.teams[team_name]
            team.add_member(member)
            print(f"{member} has been added to {team_name}")
        else:
            print(f"{team_name} does not exist")

    def remove_member_from_team(self, team_name, member):
        if team_name in self.teams:
            team = self.teams[team_name]
            team.remove_member(member)
        else:
            print(f"{team_name} does not exist")

    def edit_member_name_in_team(self, team_name, old_name, new_name):
        if team_name in self.teams:
            team = self.teams[team_name]
            team.edit_member_name(old_name, new_name)
        else:
            print(f"{team_name} does not exist")

    def find_team(self, team_name):
        if team_name in self.teams:
            team = self.teams[team_name]
            print(f"{team.name}:")
            if team.members:
                for member in team.members:
                    print(f"- {member}")
            else:
                print("- No members")
        else:
            print(f"{team_name} does not exist")

    def display_all_teams(self):
        if self.teams:
            for team_name, team in sorted(self.teams.items()):
                print(f"{team_name}:")
                if team.members:
                    for member in team.members:
                        print(f"- {member}")
                else:
                    print("- No members")
        else:
            print("No teams exist")

    def load_data(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            for team_name, members in data.items():
                team = Team(team_name)
                for member in members:
                    team.add_member(member)
                self.teams[team_name] = team
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"Error: {filename} not found")

    def save_data(self, filename):
        with open(filename, "w") as f:
            data = {}
            for team_name, team in self.teams.items():
                data[team_name] = team.members
            json.dump(data, f)
        print(f"Data saved to {filename}")

    def display_average_members_per_team(self):
        if self.teams:
            num_teams = len(self.teams)
            total_members = sum(len(team.members)
                                for team in self.teams.values())
            print(f"Average members per team: {total_members/num_teams:.2f}")
        else:
            print("No teams exist")


if __name__ == "__main__":
    team = TeamManagementSystem()

while True:
    print("\nWhat would you like to do?")
    print("1. Create a team")
    print("2. Rename a team")
    print("3. Remove a team")
    print("4. Add a member to a team")
    print("5. Remove a member from a team")
    print("6. Edit a member's name in a team")
    print("7. Find a team")
    print("8. Display all teams")
    print("9. Load data from a file")
    print("10. Save data to a file")
    print("11. Display average members per team")
    print("0. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        team_name = input("Enter the name of the team: ")
        team.create_team(team_name)
    elif choice == "2":
        old_name = input("Enter the name of the team to rename: ")
        new_name = input("Enter the new name for the team: ")
        team.rename_team(old_name, new_name)
    elif choice == "3":
        team_name = input("Enter the name of the team to remove: ")
        team.remove_team(team_name)
    elif choice == "4":
        team_name = input("Enter the name of the team: ")
        member = input("Enter the name of the member to add: ")
        team.add_member_to_team(team_name, member)
    elif choice == "5":
        team_name = input("Enter the name of the team: ")
        member = input("Enter the name of the member to remove: ")
        team.remove_member_from_team(team_name, member)
    elif choice == "6":
        team_name = input("Enter the name of the team: ")
        old_name = input("Enter the current name of the member: ")
        new_name = input("Enter the new name for the member: ")
        team.edit_member_name_in_team(team_name, old_name, new_name)
    elif choice == "7":
        team_name = input("Enter the name of the team: ")
        team.find_team(team_name)
    elif choice == "8":
        team.display_all_teams()
    elif choice == "9":
        filename = input("Enter the filename to load data from: ")
        team.load_data(filename)
    elif choice == "10":
        filename = input("Enter the filename to save data to: ")
        team.save_data(filename)
    elif choice == "11":
        team.display_average_members_per_team()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

# Save data before exiting
team.save_data("team_data.json")
