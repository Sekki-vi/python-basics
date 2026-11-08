# Dictionaries are unordered, mutable, and indexed by keys.
usernames = {
    "John": "john123",
    "Jane": "jane123",
    "Jim": "jim123",
}
print(usernames)

print(usernames["John"])

print(usernames.keys())

for key in usernames.keys():
    print(key +" - " + usernames[key])

print(usernames.values())

print(usernames.items())

# how to change values
usernames["John"] = "john456"
print(usernames)

# how to add new values
usernames["John"] = "john789"
print(usernames)

# how to remove values
usernames.pop("John")
print(usernames)

usernames.update({"John": "john789"})
print(usernames)

del usernames["John"]
print(usernames)

# to remove the last item
usernames.popitem()
print(usernames)

# to get a value by key. Only works if the key exists. Otherwise, it returns the default value.
print(usernames.get("John", "No John found"))