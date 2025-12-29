from z16 import *

while True:
    prompt = "Enter your name:"
    prompt += "\n(Enter 'q' at any stage to quit) "
    add_usern = input(prompt)
    if add_usern == 'q':
        break
    add_musn = input("Enter musician name: ")
    if add_musn == 'q':
        break
    add_aln = input("Enter album name: ")
    if add_aln == 'q':
        break
    print("\nHere your list:")
    make_album(add_usern, add_musn, add_aln) 
    
    repeat = input("Ask next user? (yes/no) ")
    if repeat == 'no':
        break


