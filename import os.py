import os
from random import randint

def game():
    plaer_name = input("введите имя:")
    plaer_hp = 100
    plaer_money = 10
    plaer_xp = 0
    plaer_level = 1
    visit_rock(plaer_hp, plaer_money, plaer_name, plaer_xp, plaer_level)
game()

def visit_rock(plaer_hp, plaer_money, plaer_name, plaer_xp, plaer_level):
    os.system('cls') # ОЧИЩАЕТ КАРТУ
    show_plaer(plaer_hp, plaer_money, plaer_name, plaer_xp, plaer_level)
    print('----------------------------')
    print('1 - пойти в казино ')
    print('2 - начать битву')
    print('3 - пойти в магазин')
    print('0 - уйти')
    print('----------------------------')
    option = input('введите номер варианта и нажмите ENTER:')
    if option == '1':
        visit_casino(plaer_hp, plaer_money, plaer_name, plaer_xp, plaer_level)
    elif option == '2':
        visit_combat(plaer_hp, plaer_money, plaer_name, plaer_xp, plaer_level)
    elif option == '3':
        visit_shop(plaer_hp, plaer_money, plaer_name, plaer_xp, plaer_level)
    elif option == '0':
        print(plaer_name, 'ушел')       
def show_plaer(plaer_hp, plaer_money, plaer_name, plaer_xp, plaer_level):
    print('имя', plaer_name)
    print('жизни', plaer_hp)
    print('деньги', plaer_money)
    print('опыт', plaer_xp) 
    print('уровень', plaer_level)