ringno=int(input("No of rings"))
def move(ring,og,inte,tar):
    if ring==1:
        print(f"Ring {ring} from tower {og} to {tar}\n")
    else:
        move(ring-1,og,tar,inte)
        print(f"Ring {ring} from tower {og} to {tar}\n")
        move(ring-1,inte,og,tar)

move(ringno,"A","C","B")
