#treasure island project
print("Welcome to the treasure island, your mission is to find the treasure that the princess has sent you to recover.")
step1 = input("You start your journey and you come to a cross road, choose Left or Right: ").lower()
if step1 == 'left':
    step2 = input("You come across a stream, will you swim across or wait: ").lower()
    if step2 == 'wait':
        step3 = input("A boat passes by and they help you get across, you get into an island with three doors, a red door, a blue door and a yellow door, which door will you open: ").lower()
        if step3 == 'yellow':
            print("You win. You found the treasure")
        elif step3 == 'red':
            print("You got burn't by fire. You loose.")
        elif step3 == 'blue':
            print("You were eaten by beasts. You loose.")
        else:
            print("GAME OVER!")
    else:
        print("You were attacked by a trout. You loose.")
else:
    print("You fell into a hole. Game over.")