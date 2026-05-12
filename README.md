# game_son_of_treasure
game developers:



import json

def load_game_data(filename):
    """Загружает данные игры из JSON-файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден!")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка: файл {filename} содержит некорректный JSON!")
        return None

def get_player_choice(max_choice, game_data, current_location):
    """Получает выбор игрока"""
    valid_choices = list(range(1, max_choice + 1))
    
    while True:
        try:
            print(f"\n{'='*50}")
            print(f"📍 {game_data[current_location]['name']}")
            print(f"{'='*50}")
            print(f"\n{game_data[current_location]['text']}")
            
            if max_choice == 0:
                return None
            
            print(f"\nВаши действия (1-{max_choice}):")
            # Здесь можно добавить описания действий
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
                return choice - 1  # Возвращаем индекс для массива
            else:
                print(f"Пожалуйста, введите число от 1 до {max_choice}")
        
        except ValueError:
            print("Пожалуйста, введите корректное число!")
        except KeyboardInterrupt:
            print("\n\nИгра прервана. До свидания!")
            return None

def play_game(game_data, start_location="0"):
    """Основная функция игры"""
    if not game_data:
        return
    
    current_location = start_location
    step_count = 0
    
    print("\n🎮 ДОБРО ПОЖАЛОВАТЬ В ТЕКСТОВЫЙ КВЕСТ! 🎮")
    print("Ваша задача - найти сокровище и не проснуться!")
    
    while current_location in game_data:
        step_count += 1
        next_locations = game_data[current_location].get('next_locations', [])
        
        # Проверяем, не конечная ли это локация
        if not next_locations:
            # Выводим финальный текст
            print(f"\n{'='*50}")
            print(f"📍 {game_data[current_location]['name']}")
            print(f"{'='*50}")
            print(f"\n{game_data[current_location]['text']}")
            
            # Определяем исход игры
            if "сокровище" in game_data[current_location]['name'].lower():
                print("\n🎉 ПОЗДРАВЛЯЕМ! ВЫ ВЫИГРАЛИ! 🎉")
            else:
                print("\n😴 Игра окончена. Вы проснулись!")
            
            print(f"\nКоличество сделанных шагов: {step_count}")
            break
        
        # Получаем выбор игрока
        choice_index = get_player_choice(len(next_locations), game_data, current_location)
        
        if choice_index is None:
            break
        
        # Переходим к следующей локации
        current_location = str(next_locations[choice_index])

def main():
    """Главная функция"""
    game_data = load_game_data('game_graph.json')
    
    if game_data:
        print("Граф игры успешно загружен!")
        print(f"Количество локаций: {len(game_data)}")
        print(f"Начальная локация: {game_data['0']['name']}")
        
        # Показываем доступные локации
        print("\nДоступные локации:")
        for loc_id, loc_data in game_data.items():
            endings = "✅ Успешная концовка" if "сокровище" in loc_data['name'].lower() else "❌ Неудачная концовка" if not loc_data['next_locations'] else "📍 Промежуточная"
            print(f"  {loc_id}: {loc_data['name']} - {endings}")
input("\nНажмите Enter, чтобы начать игру...")
        play_game(game_data)
    
    print("\nСпасибо за игру!")

if name == "__main__":
    main()         
