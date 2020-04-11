print("welcome to Yes/No Questions")
print("Are you ready to answer the following  Questions")
score=0
total_score =3
ans = input("Enter Y/N\n")
if ans.lower() == 'y':
    ans=input("Who is CEO of SpaceX?")
    if ans.lower() == "elon musk":
        score+=1
    ans=input("Where Covid 19 is originated?")
    if ans.lower() == 'china':
        score+=1
    ans=input("India Nuclear Submarine Name?")
    if ans.lower()== 'arihant':
        score+=1
    if score == total_score:
        print("You won")
    else:
        print("You Loose")
else:
    print("Good Bye")