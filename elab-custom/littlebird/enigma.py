'''
Problem From: https://elabsheet.org/elab/taskpads/show/i6rgzpkdj1/
Code by: _ducky_way_
'''
def encode(ch, r1, r2, c):
    if 1 <= r1 <= 26:
        re = chr(ord(ch) + 1)
    else:
        re = chr(ord(ch) + 1)
    return re

def decode(ch, r1, r2, c):
    return ch

def main():
    roter_1, roter_2 = int(input("Roter 1: ")), int(input("Roter 2: "))
    mode = input("Encode or Decode: ")
    result = ''
    count = 0
    if mode == "Encode" or mode == "Decode":
    
        while True:
            ch = input(f"Char to {mode}: ")
            if ch == '':
                print(result)
                break
            elif ord('a') <= ord(ch) <= ord('z'):
                if mode == "Encode":
                    count += 1
                    result += encode(ch, roter_1, roter_2, count)
                elif mode == "Decode":
                    count += 1
                    result += decode(ch, roter_1, roter_2, count)
            
            else:
                print("Invalid Character.")
    else:
        print("Invalid mode.")
main()