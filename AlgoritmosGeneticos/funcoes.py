import random as rd


######### Fitness

def fitness(ind):
    """Utilizada para comparar individuos.
    
    Args:
        ind: indivíduo
        
    Return:
        A soma dos valores de cada caixa"""
    return sum(ind)

def fitness_passw(ind, real_passw):
    """Computa o score de um indivíduo em comparação com a senha real.

    Args:
        ind: lista contendo as letras da senha
        real_passw: a senha real
    
    Returns:
        O score entre as duas senhas (input e real), medida letra por letra.
    """
    diff = 0

    for l_input, l_real in zip(ind, real_passw):
        diff += abs(ord(l_input) - ord(l_real))

    return diff

######### Gen

def random_gen_cb():
    """Gera um gene aleatório válido para o problema das caixas binárias.
    
    Return:
        0 ou 1."""
    return rd.randint(0,1)


def random_gen_cnb(max):
    """Gera um gene aleatório válido para o problema das caixas não binárias.
    
    Args:
        max: valor máximo para o gene

    Return:
        0 ou 1."""
    return rd.randint(0,max)

######### Ind

def new_ind_cb(n):
    """Gera um indivíduo válido.
    
    Args:
        n: número de genes
    
    Return:
        Uma lista com n genes, representando um indivíduo"""
    ind = []
    for _ in range(n):
        ind.append(random_gen_cb())
    return ind


def new_ind_cnb(n, max):
    """Gera um indivíduo válido.
    
    Args:
        n: número de genes
        max: valor máximo para o gene
    
    Return:
        Uma lista com n genes, representando um indivíduo"""
    ind = []
    for _ in range(n):
        ind.append(random_gen_cnb(max))
    return ind

######### Pop

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
            'sum': fitness(curr_ind)}
    return dicio_obj


def new_pop_cnb(tampop, tamcromo, max):
    """Gera uma nova população aleatória.

    Args:
        tampop: tamanho da população
        tamcromo: tamanho do cromossomo
        max: valor máximo para o gene

    Return:
        Um dicionário com tag, indivíduo e soma.
    """
    dicio_obj = {} #Define o dicionário contendo os indivíduos
    for i in range(tampop):
        curr_ind = new_ind_cnb(tamcromo, max)
        dicio_obj[i+1] = { #Armazena o valor da função objetivo correspondente a cada indivíduo
            'tag': i+1,
            'ind': curr_ind,
            'sum': fitness(curr_ind)}
    return dicio_obj

######### Mutation

def mutation_cb(ind, pm):
    """Realiza a mutação em toda a bitstring de um indivíduo, respeitando o fator pm
    
    Args:
        ind: indivíduo a ser mutado
        pm: probabilidade de mutação
        
    Returns:
        indivíduo mutado"""
    for i in range(len(ind['ind'])):
        mut = rd.random()
        if mut < pm:
            ind['ind'][i] = 1 - ind['ind'][i] # Troca o valor de 0 para 1 e vice-versa.
            print('Mutation in gen', i+1, 'in', ind['tag'], 'with mut=', mut)
    return ind


def mutation_cnb(ind, pm, max):
    """Realiza a mutação em toda a bitstring de um indivíduo, respeitando o fator pm
    
    Args:
        ind: indivíduo a ser mutado
        pm: probabilidade de mutação
        max: número maximo do gene
        
    Returns:
        indivíduo mutado"""
    for i in range(len(ind['ind'])):
        mut = rd.random()
        if mut < pm:
            ind['ind'][i] = random_gen_cnb(max)
            print('Mutation in gen', i+1, 'in', ind['tag'], 'with mut=', mut)
    return ind

######### Crossover

def crossover(p1, p2, pc):
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

######### Selection

def roull_sel_max(pop):
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
            'ind': populacao_selecionada[i]}
    print('sel inds:', populacao_selecionada)
    return pop_dic