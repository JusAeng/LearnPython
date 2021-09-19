post={"name":"jus","grade":4}
post["fav"]="football"
# try:
#     print(post["fav"])
# except KeyError:
#     print("magi")
fav=post.get("fac","eiei")
print(fav)
for key in post.keys():
    print(key)