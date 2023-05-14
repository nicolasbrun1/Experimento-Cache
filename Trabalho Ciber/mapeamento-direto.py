
def inicializar_cache(tamanho_cache):

    global cache 
    cache = {}
    for x in range(tamanho_cache):
        cache[x] = -1
        print(cache[x])
    
    return cache

inicializar_cache(tamanho_cache=10)

def imprimir_cache(cache):
    print(f'Tamanho da cache: {len(cache)}')
    for key, value in cache.items():
        print(f'Local:{key: < 5}| Uso:{value: < 0}')

imprimir_cache(cache)

def mapeamento_direto(tamanho_cache, pos_memoria):

    inicializar_cache(tamanho_cache)

    imprimir_cache(cache)

    miss = 0
    hit = 0
    pos_memoria
    loop = 0
    for x,pos in enumerate(pos_memoria):

        loop += 1
        
        if cache[pos % tamanho_cache] == pos:
            hit += 1
            print('STATUS: Hit')
        else:
            miss += 1
            print('STATUS: Miss')
            cache[pos % tamanho_cache] = pos

        print('-----------------')
        imprimir_cache(cache)
        print(f'Total de Hits:{hit}')
        print(f'Total de Miss:{miss}')
    print(f'Total de posições acessadas:{loop}')
    print(f'Taxa de hits:{(hit%miss + hit) * 100}')

posicoes_memoria_acessar = [33,33,5,5]
tamanho_cache = 5
mapeamento_direto(tamanho_cache, posicoes_memoria_acessar)