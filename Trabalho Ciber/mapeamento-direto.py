
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
    pos_memoria = range(cache)
    tamanho_cache
    pos_cache = pos_memoria % tamanho_cache
