
def dobra (lst):
    pos = 0 
    
    while pos < len(lst) : 
        lst[pos] *=2
        pos += 1
        
    print(lst)
        

dobra([10,2,2,1])

lista = [32,23,1,44,3,4,5,2,43]

dobra(lista)