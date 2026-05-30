# ## **Завдання 1: Клас “Квестова Кімната”**

# Створи клас **QuestRoom**, який моделює квестову кімнату.
# У кімнаті є:

# * **назва кімнати**
# * **рівень складності** (1–5)
# * **ліміт гравців**
# * **список гравців, що увійшли**

# ### 🔧 Вимоги до класу:

# 1. **Конструктор** має приймати:

#    * назву
#    * рівень складності
#    * ліміт гравців



class QuestRoom:
   def __init__(self, room_name, difficulty, max_player):
        self.room_name = room_name
        if 1<= difficulty <=5:
            self.difficulty = difficulty
        else: 
           self.difficulty = 1
        self.max_player = max_player
        self.players=[]
        self.is_active=False
        self.status="waiting"
        self.events_log=[]

   def add_player(self, name):
      if len(self.players) < self.max_player:
         self.players.append(name)
         self.events_log.append(f"Player {name} joined")
         return (f"Player {name} joined '{self.room_name}'")
      else: 
          return ("No free slots!")

   def start(self):
      if len(self.players)==0:
         return ("Room is empty!")
      else: 
         self.is_active=True
         self.status="active"
         self.events_log.append(f"Quest started")
         return f"Quest '{self.room_name}' difficulty '{self.difficulty}' started with {len(self.players)} players!"

   
   def __str__(self):
      return f"QuestRoom: {self.room_name} | Difficulty: {self.difficulty} | Players: {self.max_player}"
   
   def remove_player(self, name):
      if name in self.players:
         self.players.remove(name)
         self.events_log.append(f"Player {name} left")
         return f"Player {name} was removed"
      else:
         return "Player not found!"
   
   def is_full(self):
      if len(self.players) < self.max_player:
         return False
      else: 
         return True
      
   def free_slots(self):
      return f"{self.room_name}: {self.max_player-len(self.players)} free slots"
   
   def reset_room(self):
         self.active="finished"
         self.players.clear()
         self.active="waiting"
         self.events_log.append(f"Room reset")
         return f"Room reset!"
   
   def players_list(self):
      if len(self.players)==0:
         return "No players in the room"
      return self.players
   
   def show_log(self):
        return self.events_log

   

      
room1=QuestRoom("room1", 3, 3)
room1.add_player("Viki")
room1.add_player("Даша")
room1.add_player("Nat")
room1.add_player("Viking")
room1.add_player("Vally")
room1.add_player("Ibra")
print (room1.start())
print(room1)

print ("-----------------------------------------------")
room2=QuestRoom("room2", 3, 3)
room2.add_player("Viki")
room2.add_player("Даша")
room2.add_player("Nat")
room2.add_player("Viking")
room2.add_player("Vally")
room2.add_player("Ibra")
print (room2.start())
print(room2)
print(room2.is_full())
print(room2.remove_player("Даша"))
print(room2.is_full())
print(room2.free_slots())
room2.add_player("Ibra")
print(room2.reset_room())
print(room2)
print(room2.free_slots())
print(room2.players_list())
print(room2.show_log())









# 2. Створити метод **add_player(name)**

#    * додає гравця до кімнати
#    * якщо місць немає — повертає повідомлення `"No free slots!"`

# 3. Створити метод **start()**

#    * якщо кімната пуста → `"Room is empty!"`
#    * інакше → `"Quest '<назва>' started with <кількість гравців> players!"`

# 4. Метод **\_\_str\_\_**()** для красивого виводу:

#    ```
#    QuestRoom: <name> | Difficulty: <level> | Players: <players_count>/<limit>
#    ```
# ### 📝 Приклад очікуваної роботи програми:

# ```python
# room = QuestRoom("Піратський острів", 3, 4)

# print(room)  
# room.add_player("Олег")
# room.add_player("Даша")
# print(room.start())
# print(room)

# ## **Завдання 2: Доповнення для класу QuestRoom**

# ### ➕ **Нові можливості та методи**

# #### **1. Метод `remove_player(name)`**

# * Видаляє гравця зі списку.
# * Якщо такого гравця немає — повертає повідомлення `"Player not found!"`.
# #### **2. Метод `is_full()`**

# * Повертає **True**, якщо кімната заповнена.
# * Інакше — **False**.
# #### **3. Метод `free_slots()`**

# * Повертає кількість вільних місць у кімнаті.
# #### **4. Метод `reset_room()`**

# * Очищає список гравців, ніби почали нову гру.
# * Повертає повідомлення `"Room reset!"`.
# #### **5. Метод `players_list()`**

# * Повертає список імен гравців.
# * Якщо список порожній — `"No players in the room"`.
# #### **6. Додатковий стан кімнати**

# Додати поле **status**:

# * `"waiting"` — до старту,
# * `"active"` — під час гри,
# * `"finished"` — після скиду.

# Метод **start()** тепер:

# * перевіряє, чи кімната не пуста;
# * переводить стан у `"active"`.

# Метод **reset_room()**:

# * змінює стан на `"finished"` → очищає гравців → ставить `"waiting"`.
# #### **7. Лог подій (історія)**

# Додати поле **events_log** (список рядків):

# * При додаванні гравця записувати `"Player <name> joined"`
# * При видаленні — `"Player <name> left"`
# * При старті — `"Quest started"`
# * При рестарті — `"Room reset"`

# Метод **show_log()**:

# * повертає історію всіх подій.