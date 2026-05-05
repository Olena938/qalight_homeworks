from homework_11 import *
import pytest

#  Тести конструктора
# Чи правильно зберігаються:

# назва
# складність
# ліміт гравців
# початковий список гравців пустий
# статус "waiting"
# лог пустий


# @pytest.mark.parametrize("a, expected", [
#     ("aaa", True),
#     ("ab", False),
# ])

# def test_is_palindrome(a, expected):
#     # TODO: додай тести для функції is_palindrome
#     assert is_palindrome(a) == expected

@pytest.mark.parametrize("room_name, difficulty, max_player", [
    ("room3", 3, 4),
    ("room4", 3, 5),
    ("room4", 4, 5),
])


def test_init(room_name, difficulty, max_player):
    room = QuestRoom(room_name, difficulty, max_player)

    assert room.room_name == room_name
    assert room.difficulty == difficulty
    assert room.max_player == max_player

    assert room.players == []
    assert room.status == "waiting"
    assert room.events_log == []



@pytest.mark.parametrize("players", [
    ["Viki"],
    ["Viki", "Dasha"],
    ["Viki", "Dasha", "Ivan"]
])

def test_add_player(players):
    room = QuestRoom("room3", 3, 4)
    for p in players:
        room.add_player(p)
    assert room.players == players

def test_add_player_limit_reached():
    room = QuestRoom("room1", 3, 1)

    room.add_player("Viki")          # заполняем лимит
    result = room.add_player("Dasha")  # пытаемся превысить лимит

    assert result == "No free slots!"
    assert room.players == ["Viki"]

def test_add_player_same_name():
    room = QuestRoom("room1", 3, 3)
    room.add_player("Viki")          
    result = room.add_player("Viki")  
    assert room.players == ["Viki", "Viki"]
    assert "Player Viki joined" in room.events_log

def test_remove_player(): 
    room = QuestRoom("room1", 3, 3)
    room.add_player("Viki")          
    room.add_player("Vika")
    room.remove_player("Vika")
    assert room.players == ["Viki"]

def test_remove_player():
    room = QuestRoom("room1", 3, 3)
    room.add_player("Viki")          
    room.add_player("Vika")
    result=room.remove_player("Vik")
    assert room.players == ["Viki", "Vika"]
    assert result == "Player not found!"

# . Перевірка заповненості (is_full, free_slots)
# Якщо гравців менше ліміту → не повна.
# Якщо рівно ліміт → повна.
# Кількість вільних місць обчислюється правильно при різних значеннях.

# def is_full(self):
#     if len(self.players) < self.max_player:
#         return False
#     else: 
#         return True
    
def test_is_full():
    room = QuestRoom("room1", 3, 3)
    room.add_player("Viki")          
    room.add_player("Vika")
    result=room.is_full()
    assert result == False

def test_is_full_true():
    room = QuestRoom("room1", 3, 3)
    room.add_player("Viki")          
    room.add_player("Vika")
    room.add_player("Vik")
    result=room.is_full()
    assert result == True   
    

def free_slots(self):
      return f"{self.room_name}: {self.max_player-len(self.players)} free slots"

def test_free_slots():
    room=QuestRoom("room1", 3, 3)
    room.add_player("Viki")          
    room.add_player("Vika")
    result=room.free_slots()
    assert result == "room1: 1 free slots"  

def test_start_empty():
    room=QuestRoom("room1", 3, 3)
    result=room.start()
    assert result ==  ("Room is empty!")


def test_start():
    room=QuestRoom("room1", 3, 3)
    room.add_player("Viki") 
    result=room.start() 
    assert result ==  "Quest 'room1' difficulty '3' started with 1 players!"
    assert "Quest started" in room.events_log
    assert room.status=="active"

def reset_room(self):
         self.active="finished"
         self.players.clear()
         self.active="waiting"
         self.events_log.append(f"Room reset")
         return f"Room reset!"

def test_reset_room():
    room=QuestRoom("room1", 3, 3)
    room.add_player("Viki") 
    room.start() 
    result = room.reset_room()

    assert room.active =="waiting"
    assert room.players==[]
    assert "Room reset" in room.events_log
    assert result ==  "Room reset!"

def test_players_list():
    room=QuestRoom("room1", 3, 3)
    result=room.players_list()
    assert result=="No players in the room"
    room.add_player("Viki") 
    assert room.players==["Viki"]
    

def test_show_log():
    room2=QuestRoom("room2", 3, 3)
    room2.add_player("Viki")
    room2.add_player("Даша")
    room2.add_player("Nat")
    room2.add_player("Viking")
    room2.add_player("Vally")
    room2.add_player("Ibra")
    room2.start()
    room2.remove_player("Даша")
    room2.add_player("Ibra")
    room2.reset_room()
    room2.free_slots()
    result=room2.show_log()
    assert result==['Player Viki joined', 'Player Даша joined', 'Player Nat joined', 'Quest started', 'Player Даша left', 'Player Ibra joined', 'Room reset']