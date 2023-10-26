# I don't know why I made this

import random
length = int(input("Please enter the length of password: "))
content="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(content,length ))
print(p,"\n\n^^^and thats your password")
