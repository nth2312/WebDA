import os

Basicpath = "./static/detail/"
def Get():
    output = []
    for i in range(11, 21):
        path = os.path.join(Basicpath, f'{i}/description.txt')
        with open(path, 'r', encoding='utf-8') as f:
            output.append(f.read())

    with open('description.txt', 'w', encoding='utf-8') as f:
        for data in output:
            f.write(str(data))
            f.write('\n')
        f.close()

def Replace():
    with open('short.txt', 'r', encoding='utf-8') as f:
        input = f.read().split('\n')

    idx = 0
    for i in range(11, 21):
        path = os.path.join(Basicpath, f'{i}/shortDes.txt')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(input[idx])
        idx+=1
        f.close()
    
# Get()
# Replace()