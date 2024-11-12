country = input()  
equipment = input() 

scores = {
    "Russia": {
        "ribbon": {"difficulty": 9.100, "execution": 9.400},
        "hoop": {"difficulty": 9.300, "execution": 9.800},
        "rope": {"difficulty": 9.600, "execution": 9.000}
    },
    "Bulgaria": {
        "ribbon": {"difficulty": 9.600, "execution": 9.400},
        "hoop": {"difficulty": 9.550, "execution": 9.750},
        "rope": {"difficulty": 9.500, "execution": 9.400}
    },
    "Italy": {
        "ribbon": {"difficulty": 9.200, "execution": 9.500},
        "hoop": {"difficulty": 9.450, "execution": 9.350},
        "rope": {"difficulty": 9.700, "execution": 9.150}
    }
}

difficulty = scores[country][equipment]["difficulty"]
execution = scores[country][equipment]["execution"]

total_score = difficulty + execution

missing_percentage = ((20 - total_score) / 20) * 100

print(f"The team of {country} get {total_score:.3f} on {equipment}.")
print(f"{missing_percentage:.2f}%")
