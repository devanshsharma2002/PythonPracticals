Q = {"start", "accept", "reject"}  
Σ = {'a', 'b', 'c', ..., 'z'}      
q0 = "start"                       
F = {"accept"}                     

def δ(state, char):
    if state == "start":
        if char == 'a':
            return "accept"       
        else:
            return "reject"       
    elif state == "accept":
        if char == 'a':
            return "accept"       
        else:
            return "reject"       
    elif state == "reject":
        if char == 'a':
            return "accept"       
        else:
            return "reject"       
    return "reject"               

def is_accepted(string):
    current_state = q0  

    for char in string:
        current_state = δ(current_state, char)  

    return current_state in F

test_strings = ["apple", "banana", "aardvarka", "bat", "cata", "alphaa"]

for s in test_strings:
    result = is_accepted(s)
    print(f"The string '{s}' is {'accepted' if result else 'rejected'} by the DFA.")
