if __name__ == '__main__':
    lst = []
    N = int(input())
    for _ in range(N):
        command = input().split()
        cmd = command[0]
        match cmd:
            case "insert":
                lst.insert(int(command[1]), int(command[2]))
            case "remove":
                lst.remove(int(command[1]))
            case "append":
                lst.append(int(command[1]))
            case "sort":
                lst.sort()
            case "pop":
                lst.pop()
            case "reverse":
                lst.sort(reverse = True) 
            case "print":
                print(lst)
    
    