__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"

# Mother class Homeowners
class Homeowner:
    def __init__(self, f_name, l_name, address, needs):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address
        self.needs = needs


# Mother class Specialists
class Specialist:
    def __init__(self, name, profession, price):
        self.name = name
        self.profession = profession
        self.price = price

# Daughter class Specialist
class Electrician(Specialist):
  pass

# Daughter class Specialist
class Painter(Specialist):
  pass

# Daughter class Specialist
class Plumber(Specialist):
  pass

def contracts(homeowner):
    contracts = []
    for need in homeowner.needs:
      if need == "electrician":
        contracts.append(alice.name)
      elif need == "painter":
        contracts.append(bob.name)
      elif need == "plumber":
        contracts.append(craig.name)
    return f"{homeowner.f_name}'s contracts: {contracts}"


alfred = Homeowner('Alfred', 'Alfredson', 'Alfredslane 123', ['painter', 'plumber'])
bert = Homeowner('Bert', 'Bertson', 'Bertslane 231', ['plumber'])
candice = Homeowner('Candice', 'Candicedottir', 'Candicelane 321', ['electrician', 'painter'])


alice = Electrician('Alice Aliceville', 'electrician', 80)
bob = Painter('Bob Bobsville', 'painter', 60)
craig = Plumber('Craig Craigsville', 'plumber', 70)


print(contracts(alfred))
print(contracts(bert))
print(contracts(candice))