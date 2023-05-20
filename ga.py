from agents import Agent
import numpy
import random

class GeneticAlgorithm:

    def __init__(self, environment: str, population: int, generation: int, target_str: str, mutation_tax: float, selection_tax: float):

        self.generation = generation
        self.environment = environment
        self.population = population
        self.target_str = target_str
        self.in_str = target_str
        self.mutation_tax = mutation_tax
        self.selection_tax = selection_tax
        self.in_str_len = len(self.in_str)
        self.agents = [Agent(self.in_str_len) for _ in range(population)]
        self.results = {
        "E1" : numpy.zeros(10),
        "E2" : numpy.zeros(10),
        }

    def get_fitness(self, string, target):

        points = sum(1 for expected, actual in zip(target, string) if expected == actual)
        return ((points*10)/self.in_str_len)

    def fitness(self):

        for agent in self.agents:
            agent.fitness = self.get_fitness(agent.string, self.in_str)

    def crossover(self):

        offspring = []
        for _ in range(int((self.population - len(self.agents) / 2))):
            pai1 = random.choice(self.agents)
            pai2 = random.choice(self.agents)
            filho1 = Agent(self.in_str_len)
            filho2 = Agent(self.in_str_len)
            split = random.randint(0, self.in_str_len)
            filho1.string = pai1.string[0:split] + pai2.string[split:self.in_str_len]
            filho2.string = pai2.string[0:split] + pai1.string[split:self.in_str_len]
            offspring.append(filho1)
            offspring.append(filho2)

        self.agents.extend(offspring)

    def mutacao(self):

        for agent in self.agents:
            for idx, param in enumerate(agent.string):
                if random.uniform(0.0, 1.0) <= self.mutation_tax:
                    agent.string = agent.string[0:idx] + random.choice(self.environment) + agent.string[idx+1:self.in_str_len]

    def selecao(self):

        agents = sorted(self.agents, key=lambda agent: agent.fitness, reverse=True)
        self.agents = agents[:int(self.selection_tax * len(agents))]

    def execute(self):

        for geracao in range(self.generation):

            self.fitness()
            self.selecao()
            self.crossover()
            self.mutacao()

            if any(agent.fitness >= 10.0 for agent in self.agents):
                print('Solução encontrada')
                return geracao
            
        return self.generation
