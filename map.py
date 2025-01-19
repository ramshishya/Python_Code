# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

print(users.keys())
print(users.values())

for key in users.keys():
    print("user: "+key,end="=")
print(users.values())


# Create a sample collection
sample_users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy:  Iterate over a copy

for s_user,status in sample_users.copy().items() :
    if status=='inactive':
        del(sample_users[status])
# Strategy:  Create a new collection
active_user={}
for user,status in sample_users.items():
    if(status=='active'):
        active_user[user]=status


dict_of_users={''}
dict_of_users[user]=True