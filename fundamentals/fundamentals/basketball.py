class Player:
    team_list = []
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    @classmethod
    def get_team(cls,team_list):
        cls.team_list = team_list
        return cls.team_list
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

arr = [kevin,jason,kyrie]
    
# Create your Player instances here!
player_jason = Player(jason)
new_team=[]
for i in range(len(arr)):
    new_team.append(Player(arr[i]))

for i in range(len(new_team)):
    print(f"name: {new_team[i].name}\nage: {new_team[i].age}\nposition: {new_team[i].position}\nteam: {new_team[i].team}\n")
