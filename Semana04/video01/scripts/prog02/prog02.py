'''
Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022
'''

print('Hello world')

message = 'Hello World'
print(message)

message = 'Bobby\'s World'
print(message)

message = "Bobby's World"
print(message)


message = """Bobby's World was a good
          #cartoon in the 1990s"""
print(message)

message = 'Hello World'
print(len(message))

message = 'Hello World'
print(message[10])

message = 'Hello World'
print(message[:5])

message = 'Hello World'
print(message.lower())

message = 'Hello World'
print(message.upper())

message = 'Hello World'
print(message.count('Hello'))

message = 'Hello World'
print(message.find('Hello'))

message = 'Hello World'
new_message = message.replace('World','Universe')
print(new_message)

greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome!'
print(message)

greeting = 'Hello'
name = 'Michael'
message = '{}, {}. Welcome!'.format(greeting,name)
print(message)

greeting = 'Hello'
name = 'Michael'
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

greeting = 'Hello'
name = 'hericles'
print(dir(name))

"""greeting = 'Hello'
name = 'Michael'
print(help(str.lower))

print(help(str.upper)) """