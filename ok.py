from random import shuffle
spisog = ['colb', 'mazik', 'kortoshka']

triks = input('vvedite ingridient (horosh - stop):')
while triks != 'horosh':
    if triks in spisog:
        print('etot engridient uze estb!')

    else:
        spisog.append(triks)
    
    triks = input('vvedite ingridient (horosh - stop):')

spisog_blender = []
nums = int(input('skolbko mesim ingr:'))
for i in range(nums):
    shuffle(spisog)
    spisog_blender.append(spisog[0])
    spisog.remove(spisog[0])

print('prigotovb cheto iz')
for i in range(nums):
    print(spisog_blender[i])

