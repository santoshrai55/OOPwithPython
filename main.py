class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'santosh')
user_2 = User('002', 'rai')
user_1.follow(user_2)
print(f'user 1 has {user_1.followers} followers')
print(f'{user_1.following} users are following user 1')
print(f'user 2 has {user_2.followers} followers')
print(f'{user_2.following} users are following user 2')
