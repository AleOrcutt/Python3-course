## 2. Syntax Errors ##

def first_elts (input_lst):
    elts = []
    for each in input_lst:
        elts.append(each)
    return elts

animals = [["dog","cat","rabbit"],["turtle","snake"],["sloth","penguin","bird"]]
first_animal = first_elts(animals)
print(first_animal)

## 4. TypeError and ValueError ##



guardians = '42'
float (guardians)