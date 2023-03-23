import random as rd

def fitness_cb(ind):
    """Utilizada para comparar individuos.
    
    Args:
        ind: indivíduo
        
    Return:
        A soma dos valores de cada caixa"""
    return sum(ind)


def random_gen_cb():
    """Gera um gene aleatório válido para o problema.
    
    Return:
        0 ou 1."""
    return rd.randint(0,1)


def new_ind_cb(n):
    """Gera um indivíduo válido.
    
    Args:
        n: número de genes
    
    Return:
        Uma lista com n genes, representando um indivíduo"""
    ind = []
    for i in range(n):
        ind.append(random_gen_cb())
    return ind


def new_pop_cb(tampop, tamcromo):
    """Gera uma nova população aleatória.

    Args:
        tampop: tamanho da população
        tamcromo: tamanho do cromossomo

    Return:
        Um dicionário com tag, indivíduo e soma.
    """
    dicio_obj = {} #Define o dicionário contendo os indivíduos
    for i in range(tampop):
        curr_ind = new_ind_cb(tamcromo)
        dicio_obj[i+1] = { #Armazena o valor da função objetivo correspondente a cada indivíduo
            'tag': i+1,
            'ind': curr_ind,
            'sum': fitness_cb(curr_ind)}
    return dicio_obj


def mutation_cb(ind, pm):
    """Realiza a mutação em toda a bitstring de um indivíduo, respeitando o fator pm
    
    Args:
        ind: indivíduo a ser mutado
        pm: probabilidade de mutação"""
    for i in range(len(ind['ind'])):
        mut = rd.random()
        if mut < pm:
            ind['ind'][i] = 1 - ind['ind'][i] # Troca o valor de 0 para 1 e vice-versa.
            print('Mutation in gen', i+1, 'in', ind['tag'], 'with mut=', mut)
    return ind


def crossover_cb(p1, p2, pc):
    """Realiza o cruzamento entre 2 pais, respeitando o fator pc
    
    Args:
        p1: pai1
        p2: pai2
        pc: probabilidade de cruzamento
        
    Return:
        Lista contendo os 2 indivíduos filhos"""
    c1, c2 = p1.copy(), p2.copy()
    cross = rd.random()
    if cross < pc:
        cross_point = rd.randint(1, len(p1)-1)
        c1[:cross_point] = p1[:cross_point]
        c1[cross_point:] = p2[cross_point:]
        c2[:cross_point] = p2[:cross_point]
        c2[cross_point:] = p1[cross_point:]
        print('crossover between', p1, 'and', p2, 'done.')
    else:
        c1 = p1
        c2 = p2
        print('Crossover failed.')
    return [c1,c2]


def roull_sel_max_cb(pop):
    """Seleciona os individuos de uma população pelo método da roleta para problemas de maximização.
    
    Args:
      pop: dicionário com todos os individuos da população e seus valores da funcao objetivo
    
    Return:
      Dicionário com a população dos indivíduos selecionados, a tag e a soma.
    """
    fitness = [pop[i]['sum'] for i in pop]
    all_zero = True
    for i in fitness:
        if i != 0:
            all_zero = False
            break
    if all_zero == True:
        for i in range(len(fitness)):
            fitness[i] = 1
    pop_list = [pop[j]['ind'] for j in pop]
    populacao_selecionada = rd.choices(pop_list, weights=fitness, k=len(pop_list))
    pop_dic = {}
    for i in range(len(populacao_selecionada)):
        pop_dic[i+1] = {
            'tag': i+1,
            'ind': populacao_selecionada[i],
            'sum': fitness_cb(populacao_selecionada[i])}
    print('sel inds:', populacao_selecionada)
    return pop_dic