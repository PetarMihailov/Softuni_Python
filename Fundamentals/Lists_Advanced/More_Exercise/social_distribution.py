def social_distribution(population, min_wealth):
    total_wealth = sum(population)

    # Check if redistribution is possible
    if total_wealth < len(population) * min_wealth:
        return "No equal distribution possible"

    # Redistribution process
    while any(person < min_wealth for person in population):
        # Find the wealthiest and poorest indices
        poorest_index = population.index(min(population))
        wealthiest_index = population.index(max(population))

        # Amount needed by the poorest person
        needed = min_wealth - population[poorest_index]

        # Amount to give (cannot exceed what the wealthiest has minus minimum wealth)
        available = population[wealthiest_index] - min_wealth
        to_give = min(needed, available)

        # Update the wealth distribution
        population[poorest_index] += to_give
        population[wealthiest_index] -= to_give

    return population


# Input
population = list(map(int, input().split(", ")))
min_wealth = int(input())

# Output
result = social_distribution(population, min_wealth)
print(result)
