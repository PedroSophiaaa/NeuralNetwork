import random as rd

######### Auxiliar

def backpack_values(ind, objects, obj_order):
    """Encontra os valores relevantes para uma mochila

    Args:
      ind: Indivíduo válido (lista binária)
      objects: Dicionário com os objetos e seus valores
      obj_order: Lista com a ordem dos objetos

    Returns:
      total_p: preço total
      total_w: peso total
    """

    total_p = 0
    total_w = 0
    
    for pegou_o_item_ou_nao, nome_do_item in zip(ind, obj_order):
        if pegou_o_item_ou_nao == 1:
            item_p = objects[nome_do_item]["valor"]
            item_w = objects[nome_do_item]["peso"]
            
            total_p = total_p + item_p
            total_w = total_w + item_w

    return total_p, total_w


def euclidian_distance(a, b):
    """Calcula a distância Euclidiana de dois pontos

    Args:
      a: x1, y1
      b: x2, y2

    Returns:
      Distância entre os pontos `a` e `b`
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1-x2)**2 + (y1-y2) ** 2)**(1/2)

    return dist

def new_cities(n):
    """cria cidades com coordenadas (x,y).

    Args:
      n: número de cidades

    Return:
      Dicionário com as cidade e as coordenadas
    """

    cities = {}

    for i in range(n):
        cities[f"City {i+1}"] = (rd.random(), rd.random())

    return cities


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


def fitness_passw_size(ind, real_passw):
    """Computa o score de um indivíduo em comparação com a senha real.
    Args:
        ind: lista contendo as letras da senha
        real_passw: a senha real
    
    Returns:
        O score entre as duas senhas (input e real), medida letra por letra.
    """
    diff = 0
    real_size = len(real_passw)
    ind_size = len(ind)

    diff_size = abs(real_size - ind_size)

    for l_input, l_real in zip(ind, real_passw):
        diff += abs(ord(l_input) - ord(l_real))

    if diff == 0 and diff_size != 0:
        print('The password is in the string.')
        return 5*diff_size

    return (diff + 10*diff_size)

def fitness_cv(ind, cities):
    """Computa o score de um individuo no problema do caixeiro viajante.

    Args:
      ind: Lista com a ordem das cidades
      cities: Dicionário com as cidades e suas coordenadas

    Return: A distancia percorrida.
    """

    dist = 0

    for i in range(len(ind) - 1):
        
        start = cities[ind[i]]
        end = cities[ind[i + 1]]
        
        route = euclidian_distance(start, end)
        dist = dist + route
               
    start = cities[ind[-1]]
    end = cities[ind[0]]

    route = euclidian_distance(start, end)
    dist = dist + route
    
    return dist

def fitness_mochila(ind, objects, lim, obj_order):
    """Computa o score de um individuo no problema da mochila

    Args:
      ind: Indivíduo válido (uma lista binária)
      objects: Dicionário com os objetos e seus valores
      lim: Int: Limite de peso da mochila
      obj_order: Lista com a ordem dos objetos

    Returns: Valor dos itens da mochila ou penalidade para indivíduos inválidos.
    """
    
    valor_mochila, peso_mochila = backpack_values(ind, objects, obj_order)
    
    if peso_mochila > lim:
        return 0.001
    else:
        return valor_mochila

def fitness_pop_mochila(pop, objects, lim, obj_order):
    """Computa o score de uma população no problema da mochila

    Args:
      pop: lista com os indivíduos da população
      objects: Dicionário com objetos
      lim: Int: Limite de peso da mochila
      obj_order: Lista com a ordem dos objetos

    Returns: Lista com os valores dos itens de cada indivíduo
    """

    res = []
    for ind in pop:
        res.append(
            fitness_mochila(
                ind, objects, lim, obj_order
            )
        )

    return res


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

def new_ind_passw_size(char_list, mini, maxi):
    """Gera um indivíduo válido.
    Args:
      char_list: list de caracteres válidos.
      mini: Tamanho mínimo da senha
      maxi: Tamanho máximo da senha
    Return:
      Lista com n letras
    """

    tampassw = rd.randint(mini, maxi)

    candidato = []

    for n in range(tampassw):
        candidato.append(random_gen_passw(char_list))

    return candidato


def new_ind_cv(cities):
    """Gera um possível caminho no problema do caixeiro viajante

    Args:
      cities: dicionário com as cidades e coordenadas

    Return: lista de cidades com caminho aleatório
    """
    cities_list = list(cities.keys())
    rd.shuffle(cities_list)
    return cities_list


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


def new_pop_passw_size(tampop, char_list, real_passw, mini, maxi):
    """Gera uma nova população aleatória.
    Args
      tampop: tamanho da população.
      char_list: lista de caracteres válidos.
      real_passw: senha verdadeira
      mini: menor tamanho da senha
      maxi: maior tamanho da senha
    Returns:
      Um dicionário com tag, senha e fitness.
    """
    dicio_pop = {}
    for i in range(tampop):
        curr_ind = new_ind_passw_size(char_list, mini, maxi)
        dicio_pop[i+1] = { #Armazena o valor da função objetivo correspondente a cada indivíduo
            'tag': i+1,
            'ind': ''.join(curr_ind),
            'fitness': fitness_passw_size(curr_ind, real_passw)}
    return dicio_pop


def new_pop_cv(tampop, cities):
    """Gera uma nova população aleatória.
    Args
      tampop: tamanho da população.
      cities: dicionário com as cidades e as coordenadas.
    Returns:
      Um dicionário com tag, senha e fitness.
    """

    dicio_pop = {}

    for i in range(tampop):
        curr_ind = new_ind_cv(cities)
        dicio_pop[i+1] = { #Armazena o valor da função objetivo correspondente a cada indivíduo
            'tag': i+1,
            'ind': curr_ind,
            'fitness': fitness_cv(curr_ind, cities)}
    return dicio_pop
    #eduardaveigac

def new_pop_mochila(tam_pop, n):
    """Cria uma nova população aleatório para o problema da mochila.

    Args:
      tam_pop: tamanho da população
      n: número de genes

    Returns: Uma lista com indivíduos de n genes
    """
    pop = []
    for _ in range(tam_pop):
        pop.append(new_ind_cb(n))
    return pop


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

def mutation_mochila(ind, pm):
    """Realiza a mutação em toda a bitstring de um indivíduo, respeitando o fator pm
    
    Args:
        ind: indivíduo a ser mutado
        pm: probabilidade de mutação
        
    Returns:
        indivíduo mutado"""
    for i in range(len(ind)):
        mut = rd.random()
        if mut < pm:
            ind[i] = 1 - ind[i] # Troca o valor de 0 para 1 e vice-versa.
            #print('Mutation in gen', i+1, 'in', ind, 'with mut=', mut)
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


def mutation_size(ind, pm, char_list):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      ind: individuo a ser mutado
      pm: probabilidade de mutação
      char_list: possíveis caracteres
    Return:
      indivíduo mutado.
    """
    mut = rd.random()
    pre_mut_ind = ind["ind"]
    ind_size = len(ind["ind"])
    if mut < pm:
        crosspoint_1 = rd.randint(0, 100)
        crosspoint_2 = rd.randint(0, 100)

        while abs(crosspoint_1 - crosspoint_2) < 3:
            crosspoint_2 = rd.randint(0, 100)
        
        if crosspoint_1 > ind_size:
            diff_size = crosspoint_1 - ind_size
            gens = [random_gen_passw(char_list) for _ in range(diff_size)]
            ind["ind"] = ind["ind"] + ''.join(gens)
        elif crosspoint_2 > ind_size:
            diff_size = crosspoint_2 - ind_size
            gens = [random_gen_passw(char_list) for _ in range(diff_size)]
            ind["ind"] = ind["ind"] + ''.join(gens)
        else:
            if crosspoint_1 > crosspoint_2:
                ind["ind"] = ind["ind"][crosspoint_2:crosspoint_1]
            elif crosspoint_2 > crosspoint_1:
                ind["ind"] = ind["ind"][crosspoint_1:crosspoint_2]
            else:
                return ind
        print('Size mutation in [', ind['tag'], ' : ', pre_mut_ind, '] with mut= ', mut, f'. {ind_size} to {len(ind["ind"])}', sep='')
    return ind
    

def swap_mutation(ind):
    """Inverte o valor de dois genes.

    Args:
      individuo: indivíduo a ser mutado

    Return:
      indivíduo mutado
    """

    index = list(range(len(ind['ind'])))
    index_sample = rd.sample(index, k=2)
    index1 = index_sample[0]
    index2 = index_sample[1]

    ind["ind"][index1], ind["ind"][index2] = ind["ind"][index2], ind["ind"][index1]

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
        #print('crossover between', p1, 'and', p2, 'done.')
    else:
        c1 = p1
        c2 = p2
        #print('Crossover failed.')
    return [c1,c2]


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


def crossover_passw_size(p1, p2, pc):
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
        if len(p1) > len(p2):
            cross_point = rd.randint(1, len(p2)-1)
        elif len(p2) > len(p1):
            cross_point = rd.randint(1, len(p1)-1)
        if len(p1) == len(p2):
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


def crossover_cv(p1, p2, pc):
    """Aplica o método de cruzamento ordenano entre p1 e p2

    Args:
      p1: pai1
      p2: pai2
      pc: probabilidade de cruzamento

    Return: Duas listas, filho1 e filho2
    """
    co1 = rd.randint(0, len(p1) - 2)
    co2 = rd.randint(co1 + 1, len(p1) - 1)
    
    c1 = p1[co1:co2]
    for gen in p2:
        if gen not in c1:
            c1.append(gen)
            
    c2 = p2[co1:co2]
    for gen in p1:
        if gen not in c2:
            c2.append(gen)
            
    return [c1, c2]


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

def roull_sel_max_mochila(pop, fitness):
    """Seleciona os individuos de uma população pelo método da roleta para problemas de maximização.
    
    Args:
      pop: lista com todos os individuos da população
      fitness: lista com os scores dos individuos da população

    Returns:
      População dos indivíduos selecionados
    """
    sel_pop = rd.choices(
        pop, weights=fitness, k=len(pop)
    )
    return sel_pop


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


def tourn_sel_min_cv(pop, cities, tamtourn=3):
    """Seleciona os indivíduos de uma população pelo método de torneio para problemas de minimização.

    Args:
        pop: dicionário com todos os indivíduos da população e seus valores da função objetivo
        cities: dicionário com as cidades
        tamtourn: quantidade de invidiuos no torneio
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
                'ind': (sel_pop[i]),
                'fitness': fitness_cv(sel_ind, cities)}

    print('sel inds:', sel_pop)
    return pop_dic