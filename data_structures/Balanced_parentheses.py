import array as arr
try:
    class stack:

        def __init__(self):
            self.array = arr.array('u',)
            self.count = 0

        def push(self):
            ''' Function to push the opening parenthses to the stack'''
            self.array.append('(')
            self.count +=1

        def string_traversal(self,string):
            ''' Function to traverse the string and check for parentheses'''
            for i in string:
                if( i == '('):
                    new.push()

                elif(i == ')'):
                    new.pop()

                if (i == (len(string) - 1 )):
                    if self.count == 0:
                        print("True")
                    else:
                        print("False")

        def isEmpty(self):
            ''' Function to check whethre the stack is empty'''
            if (len(self.array) == 0):
                return True
            else:
                return False
        
        def pop(self):
            ''' Function to remove the parentheses from the stack'''
            self.array.remove('(')
            self.count -= 1 
            #print(self.array)

        def peek(self):
            ''' Function to get the first element of the array'''
            return self.array[0]
        
        def Size(self):
            ''' Function to get the length of the array'''
            return len(self.array)

    # Driver function
    if __name__ == "__main__":
        new = stack()
        string = str(input("Enter the string to check for balanced parantheses:   "))
        new.string_traversal(string)

        print("Is the arithmetic expression balanced: ", new.isEmpty())

except ValueError:
    print("\n Wrong input, Try Again!!!")
