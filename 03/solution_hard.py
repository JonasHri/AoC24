# %%
def mul(a, b):
    return a * b

with open('input_hard.txt', 'r') as f :
    text = ''.join(f.readlines())

sum = 0
exe = True

text.find('sdlkfjhsdklfh')
# %%
last_len = 0
while len(text) > 7:
    next_mul = text.find('mul(') if text.find('mul(') >= 0 else len(text)
    do = text.find('do()') if text.find('do()') >= 0 else len(text)
    dont = text.find('don\'t()') if text.find('don\'t()') >= 0 else len(text)
    if last_len == len(text):
        print(next_mul, do, dont, text)
        break

    last_len = len(text)
    if next_mul < do and next_mul < dont:
        text = text[next_mul:]
        end = text.find(')')+1
        instr = text[:end]
        text=text[1:]
        if exe:
            try:
                sum += eval(instr)
            except:
                pass
    elif do < dont:
        exe = True
        text = text[do+1:]
    else:
        exe = False
        text = text[dont+1:]

print(sum, text)