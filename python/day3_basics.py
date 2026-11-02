nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)                    # {1, 2, 3}

point = (10, 20)
# point[0] = 5                   # TypeError: tuple неизменяемый

user = {"name": "Влад", "age": 27}
user["email"] = "v@mail.com"
print(user)

nums = [1, -2, 3, -4, 5]
positive = [x for x in nums if x > 0]
doubled = [x * 2 for x in nums]
print(positive, doubled)

users = [{"name": "Влад", "age": 27}, {"name": "Даша", "age": 25}]
users.sort(key=lambda u: u["age"])
print(users)                     # Даша первой

def show(*args, **kwargs):
    print("позиционные:", args)
    print("именованные:", kwargs)

show(1, 2, name="Влад")
show("a", "b", color="red")