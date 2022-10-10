from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())

# unique_koala_facts: takes an integer as an argument and returns that number of unique koala facts in a list. 

def unique_koala_facts(number):
    koala_facts = []
    loops = 0
    while loops < 1000 and len(koala_facts) < number:
        fact = random_koala_fact()
        loops += 1
        if fact not in koala_facts:
            koala_facts.append(fact)
    return koala_facts


# print(unique_koala_facts(6))
# print(unique_koala_facts(60))

# num_joey_facts: young marsupials are called 'joeys'. How many unique facts mentioning this term are in our facts dataset?

def num_joey_facts():
    count = 0
    facts_10_times = []
    joey_facts = []
    
    while count < 10:
        fact = random_koala_fact()
        facts_10_times.append(fact)
        if fact not in facts_10_times:
            facts_10_times.append(fact)
        elif facts_10_times[0] == fact:
            count += 1
    
        for facts in facts_10_times:
            if "joey" in facts:
                if facts not in joey_facts:
                    joey_facts.append(facts)

    return len(joey_facts) 

  
# print(num_joey_facts())

# koala_weight: somewhere in the data is a fact about how heavy a koala is. This function should return that weight in kilogram (kg) as an integer

def koala_weight():
    loops = 0
    weight_fact = ""
    
    while loops < 1000:
        fact = random_koala_fact()
        loops += 1
        
        if "kg." in fact:
            weight_fact = fact
  
    return int(weight_fact[-5:-3])


# print(koala_weight())
