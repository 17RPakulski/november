sorted_list = [11,12,18,22,25,46,88]

def sort(sorted_list):
    pivot = sorted_list[-1]
    
    left_list = []
    middle_list = []
    right_list = []

    for item in sorted_list:
        if item < pivot:
            left_list.append(item)
        elif item == pivot:
            middle_list.append(item)
        else:
            right_list.append(item)
            
    








'''
def recursive(l):   
    if len(l) < 1:
        return l
    
    else:
        return(recursive(l - 1))
    



listt = [2,3,5,1]
recursive(listt)

'''

