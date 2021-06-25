score = input("Enter Score between 0 and 1: ")
s = float(score)
if s<0 :
    print("Please enter a valid score")
elif s>1 :
    print("Please enter a valid score")
elif s>=0.9 :
    print("A")
elif s>=0.8 :
    print("B")
elif s>=0.7 :
    print("C")
elif s>=0.6 :
    print("D")
elif s<0.6 :
    print("F")
