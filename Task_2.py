from collections import deque

def check_palindrome(string):
    # Видаляємо пробіли та переводимо рядок в нижній регістр
    formatted_string = string.lower().strip()
    
    # Двостороння черга (deque)
    char_deque = deque(formatted_string)
    
    # Додаємо символи рядка до черги
    for char in formatted_string:
        char_deque.append(char)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False 
    return True 

input_string = "Козак з казок"
print(check_palindrome(input_string))