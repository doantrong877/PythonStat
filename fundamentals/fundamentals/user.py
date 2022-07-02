class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print("User's Name: " + self.first_name + " " + self.last_name)
        print("User's Email: " + self.email)
        print("User's age: " + str(self.age))
        print("Reward Member: " + str(self.is_rewards_member))
        print("Card point: " + str(self.gold_card_points))
        return self
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print(f" Hey {self.first_name} You dont have enough point")
        return self

    def member_checker(self):
        if self.is_rewards_member == True:
            print("User already a member")
            return False
        return True



ethan = User("Ethan","Doan","ethan@gmail", 24)


ethan.enroll().spend_points(80).display_info()
