COLORS={'Olive':'#808000', 'Green':'#008000', 'Grey':'#808080', 'Aqua':'#00FFFF', 'Silver':'#C0C0C0' ,
        'Brown':'#C45824', 'Scarlet':'#FF0000', 'Blue':'#4b0082', 'White':'#FFFFFF', 'S_field':'#F08080', 'B_field':'#87CEEB'}
COLORS_READ={'Scarlet':'Алый', 'Blue':'Синий', 'White':'Нейтральный'}
FONT='Tumes 8'
STANDART=['Лес', 'Горы', 'Луг', 'Холм']
all_building={'Ферма':[STANDART, 'Добывает из клетки\n прирост еды', 3, 0, 0, 0, 0, 0], 'Лесоруб':[STANDART, 'Добывает из клетки\nприрост дерева', 2, 0, 0, 0, 0, 2], 'Карьер':[['Лес', 'Горы', 'Луг', 'Холм', 'Река'], 'Добывает из клетки прирост\nкамня и глины', 2, 0, 0, 0, 0, 4],
              'Шахта':[STANDART, 'Добывает из клетки руду,\n золото и самоцветы', 2, 2, 0, 0, 0, 2], 'Рыбак':['Река', 'Ловит в реке 4 единицы еды', 1, 0, 2, 0, 0, 3], 'Ловцы жемчуга':['Река', 'Добывает в реке прирост\nзолота и самоцветов', 1, 0, 3, 0, 0, 4],
              'Мельница':[STANDART, 'Добывает из клетки\n1,5 прироста еды', 0, 0, 2, 4, 1, 4], 'Лесопилка':[STANDART, 'Добывает из клетки\n1,5 прироста дерева', 0, 2, 4, 4, 1, 2], 'Каменоломня':[['Лес', 'Горы', 'Луг', 'Холм', 'Река'], 'Добывает из клетки\n1,5 прироста камня', 0, 1, 2, 2, 2, 2],
              'Прииск':[STANDART, 'Добывает из клетки 1,5\nприроста золота и самоцветов', 0, 0, 1, 2, 4, 0], 'Столяр':[STANDART, 'До 4 дерева -> до 4 досок', 4, 2, 0, 0, 0, 2], 'Печь для обжига':[STANDART, 'До 4 глины -> до 4 кирпичей', 0, 4, 2, 0, 0, 0],
              'Плавильня':[STANDART, 'До 2 дерева и 4 руды ->\nдо 4 металла', 0, 4, 2, 0, 0, 4], 'Монетный двор':[STANDART, 'До 3 золота -> до 12 монет', 0, 2, 2, 2, 0, 0], 'Мебельщик':[STANDART, 'До 4 досок -> до 2 мебели', 0, 2, 4, 2, 0, 4],
              'Гончар':[STANDART, 'До 3 глины -> до 3 керамики', 0, 2, 2, 4, 0, 2], 'Скульптор':[STANDART, '3 камня -> 1 статуя', 0, 4, 2, 2, 1, 4], 'Кузнец':[STANDART, 'До 2 дерева и 4 металла ->\nдо 4 инструментов', 0, 4, 0, 4, 1, 2],
              'Ювелир':[STANDART, 'До 4 золота и 2 самоцветов ->\nдо 4 драгоценностей', 0, 4, 2, 4, 2, 0], 'Банк':['Крепость', 'ПО приносят каждые 4,\nа не 5 сохраненных монет', 0, 0, 0, 4, 2, 10],
              'Архитектор':['Крепость', 'Получите доп ПО, за свои\nулучш. здания, если их больше', 2, 2, 2, 2, 2, 0], 'Коллекционер':['Крепость', 'ПО за каждый сет Мебели,\nКерамики и Статуи', 0, 0, 2, 4, 2, 0]}

all_res=['food', 'wood', 'clay', 'rock', 'ore', 'gold', 'gem', 'plank', 'brick', 'metal', 'furniture', 'ceramic', 'statue', 'instrument', 'jewel', 'money']