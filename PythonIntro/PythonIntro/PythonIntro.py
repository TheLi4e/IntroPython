##Task 1
#def Task1(a, b):
#    if a*a == b:
#        return ('a is quad b');
#    elif b*b==a:
#        return ('b is quad a');
#    else:
#        return ('a is not quad b')
    
#print(Task1(1,2));

##Task2
#def Task2(*args):
#    return max(*args);


#print(Task2([1,2,10,13,22]));

##Task3
#def Task3(l):
#    a = range(-l,l+1);
#    val = [];
#    for i in a:
#        val.append(i);
#    return val;

#l = 5;
#print(Task3(l));

##Task4

#def Task4(a):
#    return int((a * 10) % 10)


#print(Task4(2.45454))

##Task5

#def Task5(a):
#    if (a%5 or a%10 or a%15) and (a%30 != 0):
#        return True;
#    else:
#        return False;

  
#print(Task5(150))

##Task6
#def Task6(a):
#    days = {
#        1: "Monday",
#        2: "Tuesday",
#        3: "Wednesday",
#        4: "Thursday",
#        5: "Friday",
#        6: "Saturday",
#        7: "Sunday"
#        }
#    output = 0;
#    if int(a)>5:
#        output = f'{days.get(a)} Holiday';
#    else:
#        output = f'{days.get(a)} Workday';
    
#    return output;

#print(Task6(7))