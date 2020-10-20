def check(expression): 
      
    open_tup = tuple('({[') 
    close_tup = tuple(')}]') 
    map = dict(zip(open_tup, close_tup)) 
    queue = [] 
    
    print(map)
    
    for i in expression: 
        if i in open_tup: 
            queue.append(map[i]) 
        elif i in close_tup: 
            if not queue or i != queue.pop(): 
                return "Unbalanced"
        print('queue', queue)
    if not queue: 
        return "Balanced"
    else: 
        return "Unbalanced"
  
# Driver code 
string = "{[]{()}}"
print(string, "-", check(string)) 
print('========================================================')
string = "((()"
print(string,"-",check(string)) 
print('========================================================')
string = "{([)]()}"
print(string,"-",check(string)) 
print('========================================================')
string = "(()()()())"
print(string,"-",check(string)) 
print('========================================================')
string = "(((())))"
print(string,"-",check(string)) 
print('========================================================')
string = "(()((())()))"
print(string,"-",check(string)) 
print('========================================================')
string = "((((((())"
print(string,"-",check(string)) 
print('========================================================')
string = "()))"
print(string,"-",check(string)) 
print('========================================================')
string = "(()()(()"
print(string,"-",check(string)) 
print('========================================================')

#https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
#https://www.educative.io/edpresso/balanced-brackets-in-python
#https://runestone.academy/runestone/books/published/pythonds/BasicDS/SimpleBalancedParentheses.html    <<<<-----
#https://bradfieldcs.com/algos/stacks/balanced-parentheses/                                             <<<<-----
#https://www.tutorialspoint.com/check-for-balanced-parentheses-in-python

#https://codereview.stackexchange.com/questions/180567/checking-for-balanced-brackets-in-python
#https://stackoverflow.com/questions/38833819/python-program-to-check-matching-of-simple-parentheses

#https://medium.com/@goutomroy/checking-balanced-brackets-39326265894f

