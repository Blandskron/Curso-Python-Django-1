# 41) Modelo "usuario -> amigos" usando dict + set
red_social = {
    "alice": {"bob", "carol"},
    "bob": {"alice", "dave"},
    "carol": {"alice", "eve"},
}

amigos_en_comun = red_social["alice"] & red_social["bob"]
print(amigos_en_comun)
