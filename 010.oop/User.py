

# definir una clase
class User:
    id = 0
    email = 'user@gmail.com'
    password = ''
    avatar = ''
    bio = ''


# crear un objeto
user1 = User()
user1.id = 1
user1.email = 'paco@gmail.com'

print(user1.id)
print(user1.email)


## crear otro objeto
user2 = User()
user2.id = 2
user2.email = 'maria@gmail.com'
print(user2.id)
print(user2.email)
