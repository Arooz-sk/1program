def sort(s, n):
    for i in range(1, n):
        temp = s[i]
 
        # Insert s[j] at its correct position
        j = i - 1
        while j >= 0 and len(temp) < len(s[j]):
            s[j + 1] = s[j]
            j -= 1
 
        s[j + 1] = temp
def printArraystring(string, n):
    for i in range(n):
        print(string[i], end = ",")
    print()
    print(string[0])
n =int(input())
if (n > 0):
  word = list(input().split(','))
  sort(word,n)
  printArraystring(word,n)
else:
  print("Invalid Input")