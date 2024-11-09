start=input("Enter a number: ")
finish=input("Enter a number: ")
start=int(start)
finish=int(finish)

result=""

for i in range(start,finish+1):
    for j in range(1,i+1):
        result += str(i)
    result += "\n"

print(result)