

# definir una clase
class User:
    id = 0
    email = 'user@gmail.com'
    password = ''
    avatar = ''
    bio = ''


# crear un objeto
# esto es una variable, pero en vez de ser tipo str, bool, int, float es de tipo User
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
