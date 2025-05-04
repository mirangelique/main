#найти все реверсивные палиндромы длиной в 4-12 символов в заданной ДНК

def rfasta(f):
    with open(f, 'r') as f:
        lines=f.readlines()
    header = lines[0].strip() #первая строка- заголовок
    d=''.join(line.strip()  for line in lines [1:]) #остальные последовательность, join объединяет элементы в одну строку
    return header, d
f='AF017449.fasta'
header, d=rfasta(f)
print('Заголовок', header)
print('днк', d)

def rev_compl(d):#вернуть обратную комплементарную строку ДНК
    c={'A':'T', 'T':'A', 'C':'G', 'G':'C'} # словарь с комплементарными нуклеотидами
    return ''.join(c[b] for b in reversed(d))
 
def fpal(d): #найти позицию и длину реверсивной днк(выход списка кортежей)
    pal=[] #инициализация списка 
    for length in range(4,12): 
        for i in range(len(d)-length + 1):  #перебор начальных позиций подстроки в днк
            s=d[i:1 + length] #извлечение заданной длины подстроки
            if s==rev_compl(s): #если строка комплементарна==рев.палиндром
                pal.append((i+1, length)) #кортеж добавляется в список
pal=fpal(d)   #возврат списка кортежей