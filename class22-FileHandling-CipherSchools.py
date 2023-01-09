#FILE ACCESS MODE w,r,a
#TEXT 
file=open("random.txt",'w')
file.write("balh blah blah")
file.close()
#writing
file=open("random2.txt","w")
file.write("Python is not nEw NOw")
n=['priyansh','jatin','katiyal','jah']
file.writelines(n)
for x in n:
    file.write(x)
#read
file=open('sample.txt','r')
file.read()#once read cant be re read
print(file.read())
#streams: iterable which ca iterated in single direction
# NO STRT & END POSITION

#smarter way of open
#context programming : 
with open("random.txt","r") as file:
    print(file.read())

class A:
    def __enter__(self):
        print("Entered")
        return 1
    def __exit__(self,*args):
        print("Exitted")
        print(args)
        return True

with A() as x:
    print(x)
    print("inside context")
    raise Exception

print("outside context")

#JSON: DICT TYPE 

# <html>
# <body>
# Hello World
# </body>
# </html>

# JSON 
# (
#     "html":(
#         "body":"HELLO WORLD"
#     )
# )

# Json Rules
# -keys can only be stringd & numbers
# - values can only be array, json,null, strings, number, booleans

a={
    "name":"Jatin",
    "marks":100,
    "languages":("C++","PYTHON","JS","CSS")

}
print(type(a))
import json
a=json.dumps(a)
print(type(a))
print(a)
