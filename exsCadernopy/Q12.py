p1 = input('Informe a primeira palavra: ').lower.strip()
p2 = input('Informe a primeira palavra: ').lower.strip()
p3 = input('Informe a primeira palavra: ').lower.strip()
if p1 == 'vertebrado':
    if p2 == 'ave':
        if p3 == 'carnivoro':
            print('Águia')
        elif p3 == 'onivoro':
            print('Pomba')
        else:
             print('Animal não identificável')    
                    
    elif p2 == 'mamifero':
        if p3 == 'onivoro':
            print('Homem')
        elif p3 == 'herbivoro':
            print('Vaca')
        else:
             print('Animal não identificável')    
                    
    else:
        print('Animal não identificável')    
            
elif p1 == 'invertebrado':
    if p2 == 'inseto':
        if p3 == 'hematofago':
            print('pulga')
        elif p3 == 'herbivoro':
            print('Lagarta')    
    elif p2 == 'anelideo':
            if p3 == 'hematofago':
                print('Sanguessuga')
            elif p3 == 'onivoro':
                print('Minhoca')    
    else:
        print('Animal não identificável')    
            
else:
    print('Animal não identificável')    