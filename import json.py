import json

def load_game_data(filename):
     try:
         with open(filename, 'r', encoding='utf-8') as file:
             return json.load(file)

def get_player_choice(max_choice, game_data, current_location):
     valid_choices = list(range(1, max_choice + 1))

while True:
    try:
        print(f"\n{'='*50}")
        print(f" {game_data[current_location]['name']}")
        print(f"{'='*50}")
        print(f"\n{game_data[current_location]['text']}")
        
        if max_choice == 0:
            return None
        
        print(f"\nВаши действия (1-{max_choice}):")
        choices = {
            "1_2": ["Осмотреть дупло", "Идти на звук волков"],
            "2_2": ["Взять факел", "Идти вглубь пещеры"],
            "3_2": ["Поговорить с ведьмой", "Остаться в таверне"],
            "0_3": ["Идти в лес", "Войти в пещеру", "Пойти в деревню"]
        }
        
        action_key = f"{current_location}_{max_choice}"
        if action_key in choices:
            for i, action in enumerate(choices[action_key], 1):
                print(f"{i}. {action}")
        
        choice = int(input("\nВаш выбор: "))
        
        if choice in valid_choices:
            return choice - 1 
        else:
            print(f"Пожалуйста, введите число от 1 до {max_choice}")

def play_game(game_data, start_location="0"):
     if not game_data: return

current_location = start_location
step_count = 0

print("Ваша задача - найти сокровище и не проснуться!")

while current_location in game_data:
    step_count += 1
    next_locations = game_data[current_location].get('next_locations', [])
    
    if not next_locations:
        print(f"\n{'='*50}")
        print(f" {game_data[current_location]['name']}")
        print(f"{'='*50}")
        print(f"\n{game_data[current_location]['text']}")
        
        if "сокровище" in game_data[current_location]['name'].lower():
            print("\n ПОЗДРАВЛЯЕМ! ВЫ ВЫИГРАЛИ! ")
        else:
            print("\n Игра окончена. Вы проснулись!")
        
        print(f"\nКоличество сделанных шагов: {step_count}")
        break
    
    choice_index = get_player_choice(len(next_locations), game_data, current_location)
    
    if choice_index is None:
        break
    
    current_location = str(next_locations[choice_index])
def main():
     game_data = load_game_data('game_graph.json')
