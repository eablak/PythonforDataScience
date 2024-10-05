ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "Turkey!")
ft_set.remove("tutu!")
ft_set.add("İstanbul!")
ft_dict["Hello"] = "42İstanbul!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)


"""# ordered and unchangeable
ft_tuple = ("Hello",)
print(type(ft_tuple))
print(ft_tuple[0])
ft_tuple = ("Hello", "Hello", "Turkey!")
print(ft_tuple)

# unordered, unchangeable*(remove,add), unindexed
ft_set = {"Hello", "Hello", "İstanbul!"}

# as of python version 3.7, dicts are ordered. 3.6 and earlier unordered"""