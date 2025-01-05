# creating the class
class User:
    # setting up the attributes 
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    # defind the display method 
    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
    # defind the enroll method
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
    # defind the spend method   
    def spend_points(self, amount):
    # Check if there are enough points to spend
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"{amount} points spent. Remaining points: {self.gold_card_points}")
        else:
            print(f"Not enough points. You only have {self.gold_card_points} points.")


user_jamal = User("Jamal", "Mohammad", "jamal.mohammad@1234.com", 34)
user_jamal.display_info()
user_jamal.enroll()
user_jamal.display_info()

print("\n")

user_joe = User("joe", "nick", "joe.nick@1234.com", 54)
user_joe.display_info()
user_joe.enroll()
user_joe.display_info()
user_joe.spend_points(50)

print("\n")

user_jane = User("jane", "jay", "jane.jay@1234.com", 25)
user_jane.display_info()
user_jane.enroll()
user_jane.display_info()
user_jane.spend_points(80)
