COLORS={'Olive':'#808000', 'Green':'#008000', 'Grey':'#808080', 'Aqua':'#00FFFF', 'Silver':'#C0C0C0' ,
        'Brown':'#C45824', 'Yellow':'#FFFF00', 'Blue':'#0000FF'}
FONT='Tumes 8'
STANDART=['Лес', 'Горы', 'Луг', 'Холм']
building_pr=['Ферма', 'Лесоруб', 'Карьер', 'Шахта', 'Рыбак', 'Ловцы жемчуга']
all_building={'Ферма':[STANDART, 'Добывает из клетки\n прирост еды', 1, 0, 0, 0, 0, 0], 'Лесоруб':[STANDART, 'Добывает из клетки\nприрост дерева', 1, 1, 1, 1, 1, 1], 'Карьер':[['Лес', 'Горы', 'Луг', 'Холм', 'Река'], 'Добывает из клетки прирост\nкамня и глины', 1, 3, 5, 1, 1, 1],
              'Шахта':[STANDART, 'Добывает из клетки руду,\n золото и самоцветы', 1, 1, 1, 1, 1, 1], 'Рыбак':['Река', 'Ловит в реке 4 единицы еды', 1, 1, 1, 1, 1, 1], 'Ловцы жемчуга':['Река', 'Добывает в реке прирост\nзолота и самоцветов', 1, 1, 1, 1, 1, 1],
              'Мельница':[STANDART, 'Добывает из клетки\n1,5 прироста еды', 1, 0, 0, 0, 0, 0], 'Лесопилка':[STANDART, 'Добывает из клетки\n1,5 прироста дерева', 1, 1, 1, 1, 1, 1], 'Каменоломня':[['Лес', 'Горы', 'Луг', 'Холм', 'Река'], 'Добывает из клетки\n1,5 прироста камня', 1, 3, 5, 1, 1, 1],
              'Прииск':[STANDART, 'Добывает из клетки 1,5\nприроста золота и самоцветов', 1, 1, 1, 1, 1, 1], 'Столяр':[STANDART, 'До 4 дерева -> до 4 досок', 1, 0, 0, 0, 0, 0], 'Печь для обжига':[STANDART, 'До 6 глины -> до 6 кирпичей', 1, 0, 0, 0, 0, 0],
              'Плавильня':[STANDART, 'До 3 дерева и 3 руды ->\nдо 3 металла', 1, 0, 0, 0, 0, 0], 'Монетный двор':[STANDART, 'До 3 золота -> до 15 монет', 1, 0, 0, 0, 0, 0], 'Мебельщик':[STANDART, 'До 4 досок -> до 2 мебели', 1, 0, 0, 0, 0, 0],
              'Гончар':[STANDART, 'До 3 глины -> до 6 керамики', 1, 0, 0, 0, 0, 0], 'Скульптор':[STANDART, '3 камня -> 1 скульптура', 1, 0, 0, 0, 0, 0], 'Кузнец':[STANDART, 'До 2 дерева и 4 металла ->\nдо 4 инструментов', 1, 0, 0, 0, 0, 0],
              'Ювелир':[STANDART, 'До 4 золота и 2 самоцветов ->\nдо 4 драгоценностей', 1, 0, 0, 0, 0, 0], 'Банк':['Крепость', 'ПО приносят каждые\n4 сохраненные монеты', 1, 0, 0, 0, 0, 0]}

all_res=['food', 'wood', 'clay', 'rock', 'ore', 'gold', 'gem', 'plank', 'brick', 'metal', 'furniture', 'ceramic', 'statue', 'instrument', 'jewel', 'money']