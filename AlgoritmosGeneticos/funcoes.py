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

def random_gen_passw(char_list):
    char = rd.choice(char_list)
    return char

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

def new_ind_passw(tampassw, char_list):
    """Gera um indivíduo válido.
    Args:
      tampassw: tamanho da senha.
      char_list: list de caracteres válidos.
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tampassw):
        candidato.append(random_gen_passw(char_list))

    return candidato

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

def new_pop_passw(tampop, tampassw, char_list, real_passw):
    """Gera uma nova população aleatória.
    Args
      tampop: tamanho da população.
      tampasw: tamanho da senha.
      char_list: lista de caracteres válidos.
      real_passw: senha verdadeira
    Returns:
      Um dicionário com tag, senha e fitness.
    """
    dicio_pop = {}
    for i in range(tampop):
        curr_ind = new_ind_passw(tampassw, char_list)
        dicio_pop[i+1] = { #Armazena o valor da função objetivo correspondente a cada indivíduo
            'tag': i+1,
            'ind': ''.join(curr_ind),
            'fitness': fitness_passw(curr_ind, real_passw)}
    return dicio_pop

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

def mutation_passw(ind, char_list, pm):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      ind: individuo a ser mutado
      char_list: lista de caracteres válidos
      pm: probabilidade de mutação
    Return:
      indivíduo mutado.
    """
    for i in range(len(ind['ind'])):
        mut = rd.random()
        if mut < pm:
            char_b = ind['ind'][i]
            char_a = random_gen_passw(char_list)
            ind['ind'] = list(ind['ind'])
            ind['ind'][i] = char_a
            ind['ind'] = ''.join(ind['ind'])
            print('Mutation in gen ', i+1, ' in [', ind['tag'], ' : ', ind['ind'], '] with mut= ', mut, f'. {char_b} to {char_a}', sep='')
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

def crossover_passw(p1, p2, pc):
    """Realiza o cruzamento entre 2 pais, respeitando o fator pc
    
    Args:
        p1: pai1
        p2: pai2
        pc: probabilidade de cruzamento
        
    Return:
        Lista contendo os 2 indivíduos filhos"""

    p1 = list(p1)
    p2 = list(p2)
    c1, c2 = p1.copy(), p2.copy()
    cross = rd.random()
    if cross < pc:
        cross_point = rd.randint(1, len(p1)-1)
        c1[:cross_point] = p1[:cross_point]
        c1[cross_point:] = p2[cross_point:]
        c2[:cross_point] = p2[:cross_point]
        c2[cross_point:] = p1[cross_point:]
        print('crossover between', ''.join(p1), 'and', ''.join(p2), 'done.')
    else:
        c1 = p1
        c2 = p2
        print('Crossover failed.')
    return [''.join(c1),''.join(c2)]

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


def tourn_sel_min(pop, real_passw, tamtourn=3):
    """Seleciona os indivíduos de uma população pelo método de torneio para problemas de minimização.

    Args:
        pop: dicionário com todos os indivíduos da população e seus valores da função objetivo
        tamtourn: quantidade de invidiuos no torneio
        real_passw: senha real
    Returns:
        Dicionário com a população dos indivíduos selecionados, a tag e seu valor de objetivo.
    """
    pop_tags = [pop[i]['tag'] for i in pop]

    sel_pop = []

    for _ in pop:
        fighters = rd.sample(pop_tags, tamtourn)

        min_fitness = float('inf')

        for ind_tag in fighters:
            ind = pop[ind_tag]['ind']
            fit = pop[ind_tag]['fitness']

            if fit < min_fitness:
                sel_ind = ind
                min_fitness = fit

        sel_pop.append(sel_ind)
        

    pop_dic = {}
    for i in range(len(sel_pop)):
        pop_dic[i+1] = {
                'tag': i+1,
                'ind': ''.join(sel_pop[i]),
                'fitness': fitness_passw(sel_ind, real_passw)}

    print('sel inds:', sel_pop)
    return pop_dic