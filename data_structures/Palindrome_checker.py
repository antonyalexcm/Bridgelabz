import collections

def dequ(string):
    ''' Function to create a deque and to check if palindrome'''
    #creating a deque with the given string    
    deq = collections.deque(string)
    #creating an empty deque to store the reverse of the string
    deq_rev = collections.deque()
    #Iteration to append the value to the reverse function
    for i in range(len(deq)-1,-1,-1):
        deq_rev.append(deq[i])
    if(deq == deq_rev):
        return True
    else:
        return False

if __name__=="__main__":
    string = str(input("Enter thr string to check whether Palindrome or not : "))
    result = dequ(string)
    print(result)


