from time import sleep

lines = [
    ("I'll imagine we fell in love", 0.08),  
    ("I'll nap under moonlight skies with you", 0.1),
    ("I think I'll picture us, you with the waves", 0.09),
    ("The ocean's colors on your face", 0.08),
    ("I'll leave my heart with your air", 0.1),
    ("So let me fly with you", 0.09),
    ("Will you be forever with me?", 0.1),
]

line_delays = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 10]

for i, (line, char_delay) in enumerate(lines):
    for char in line:
        print(f"{char}", end="", flush=True)
        sleep(char_delay)
    sleep(line_delays[i])
    print("") 
