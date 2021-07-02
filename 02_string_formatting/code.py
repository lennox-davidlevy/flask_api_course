# f string
name = "Bob"
greeting = f"hello, {name}"
print(greeting)

# with .format()

name = "David"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

#with .format() longer template

longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("David", "Friday")

print(formatted)