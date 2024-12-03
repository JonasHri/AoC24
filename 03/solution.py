# %%
def mul(a, b):
    return a * b

with open('input_03.txt', 'r') as f :
    text = ''.join(f.readlines())

sum = 0


while len(text) > 7:
    text = text[text.find('mul('):]
    end = text.find(')')+1
    instr = text[:end]
    text=text[1:]
    try:
        sum += eval(instr)
    except:
        pass

print(sum, text)