sklep_dict = {
    "piekarnia": ["chleb", "paczek", "bulka"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
x = 0
print("Lista zakupow")
for i in sklep_dict:
    a = sklep_dict.get(i)
    x += len(a)
    print("Ide do " + i.title() + " kupuje tu nastepujace rzeczy: " + str(a).title())
print("W sumie kupuje " + str(x) + " produktow, dla Pana Jacka.")