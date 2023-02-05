import random
import os
from art import LOGO
from art import VS
from game_data import DATA


def pr(score):
    os.system('cls')
    print(LOGO)
    print(f"You're right, current score: {score}.")
    

def play(B,score):
    A = B
    B = random.choice(DATA)
    while A == B:
       B = random.choice(DATA)
       
    dic={
        'a' : A,
        'b' : B
    }
    
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}. ")
    print(VS)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}. ")
    if A['follower_count'] > B['follower_count']:
        more = A
    else:
        more = B
    ch = input("Who has more followers? Type 'A' or 'B': ").lower()
    while ch == '' or (ch != 'a' and ch != 'b'):
        ch = input()
    if (dic[ch[0]] == more):
        score += 1
        pr(score)
        play(B,score)
    else:
        os.system('cls')
        print(LOGO)
        print(f"Sorry, that's wrong, final score: {score}. ")
        ch2 = input("Press '1' to play again")
        if ch2 == '1':
            os.system('cls')
            print(LOGO)
            play(random.choice(DATA),0)
        else:
            return
    
print(LOGO)
play(random.choice(DATA),0)