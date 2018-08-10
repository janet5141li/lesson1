def do_nothing():
    pass;

do_nothing();

def make_a_sound():
    print("quack");
    
make_a_sound();

def agree():
    return True;

print(agree());

def echo(anything):
    return anything+''+anything;

print(echo('Rumplestiltskin'));

def commentary(color):
    if color == 'red':
        return "it's a tomato."
    elif color == 'green':
        return "It's a green pepper.";
    elif color == "bee purple":
        return "I don't know what it is";
    else:
        return "I've never heard of the color\n" + color + ".";
    
comment = commentary('blue');
print(comment);

#None
thing=None;

if thing:
    print("Its's some thing");
else:
    print("It's no thing");
    
if thing is None:
    print("It's nothing");
else:
    print("It's something");
    
