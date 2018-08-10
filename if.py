count=1
while count <=10:
    print(count);
    count+=1
'''
while True:
stuff=input("String to capitalize[type q to quit]:");
if stuff=="q":
    break;
    print(stuff.capitalize());
'''

while True:
    
    value = input("Integer, please [q to quit]:");
    if value == "q":
        break;
    number = int(value);
    if number % 2 == 0:
        continue
    print(number, "squared is", number * number);

numbers=[1,3,5];
