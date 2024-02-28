name = input("enter your name: ")
print('''
      __
      .'`  `'.
     /        \ _
    ;      __.'` `'.
    |   .'`  `'.    /
    ;  / HAPPY  \    ;
     \; BIRTHDAY!;   |
      |          |   ;   _
      \  ()_()  ;-./-_-` '-.
      /\ (*_*) /_(;'/ `\()  '.
     ;  '.__  .'\|| '    |     '.
     |      ),\| |/      \()    (|
     ;        \ \|/   __/    ()   \  __
      \        \||\.~'_ `'.;-.___.~'` _'~.
       '.__  _/|/|/{ (_`.'         '.`_) }
           `)/`\||| \ .'   0    0   '. /     .,_
                 \/| } -.'   (_)   '.- {    _{   `|
                  \|{_ / '.___|___.' \  }  //`._   |
                /`    \     |   |     }  }:'-.  ```'"--..==,
               {      ,}    \-"-/   .'  } {,`-'.       //>`\\
              {`   _./|\._.  '-'  ._ .~` /`    ;'.    //>  ||
              {     {///(  `-.-.-`  ) _.'     /   '. ||>   //
               \     \|\);--`( )`--`(`       }      `\\>_.'/
                ;  _/`/(__.'/`-'.,__/`,    .`         `"""`
               .-'`     ;-.(     \_(;  \ .'     .--,
              (`-._   ./   `       '.   `-._..~` /o||
               `'-;/``.              `;-"`:     |oo||
          .--._ _.' .  \      o       ;  .      |  /|
         /.-.  `     .  '._        _.'  '       \_//
         ||oo\        `.   `'-----`  _.~`--..__,..'
         |\o  |       .~`'--......--'
          \'._/   _.~`
           `.__.-'
           ''')
print(f"happy birthday {name}")
choice1 = int(input("Here is your gift! pick up any box among the 1,2:"))
if choice1 == 2:
    choice2 = input("\there are two boxes in that room pick up anyone amoung(Blue,red,green)\n").lower()
    if choice2 == 'blue':
     print("Here is your anna doll as your birthday gift.")
    elif choice2 == 'green':
        choice3 = input("\There are two ballons close your eyes pick up anyone {1,2,3}: \n")
        if choice3 == 1:
            print("You got choclate box, happy birthday\n")
        elif choice3 == 2:
            print("You got 1 month disney subcription, congratulations!")
        else:
            print("You got your new vehicle! here is your Keys.Have a safe rides, Happy birthday.")
    else:
        print("Here is your new dress gift, Happy birthday (^.^)")
else:
    print("Here is your $10 dollors gift, Happy birthday (^.^)")
