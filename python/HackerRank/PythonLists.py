if __name__ == '__main__':
    N = int(input())
    myList = []
    
    for _ in range(N):
        command = input().split()
        action = command[0]

        if action == 'insert i e':
            myList.insert(command[1], command[2])
        elif action == 'print':
            print(myList)
        elif action == 'remove e':
            myList.remove(command[1], command[2])
        elif action == 'append e':
            myList.append(command[1])
        elif action == 'sort':
            myList.sort()
        elif action == 'pop':
            myList.pop(command[1])
        elif action == 'reverse':
            myList.reverse()
        
        