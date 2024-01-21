from random import choice



class Generator:
    #args: length=int, combination=str 
    def __init__(self, length, combination):
        self.length = length
        self.combination = combination
        self.combination_state = {}
        self.set_combination_state()

    def set_combination_state(self):
        #l: [l]owercase, u: [u]ppercase, n: [n]umbers, s:[s]pecial
        allowed_types = {'l': {'allowed': False, 'f': lambda: self.generate_letter('l')},
                         'u': {'allowed': False, 'f': lambda: self.generate_letter('u')},
                         'n': {'allowed': False, 'f': self.generate_number},
                         's': {'allowed': False, 'f': self.generate_special}}
        try:
            for modifier in [*self.combination]:
                allowed_types[modifier]['allowed'] = True
            self.combination_state = allowed_types
            return True
        except:
            return False


    #uppercase by default
    def generate_letter(self, case):
        charset="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        charset = charset if case == 'u' else charset.lower()
        return choice(charset)
        
    def generate_number(self):
        charset = "0123456789"
        return choice(charset)

    def generate_special(self):
        charset = "~`!@#$%^&*()-_=+[{]}\\|;:\"',<.>/?"
        return choice(charset)

    def new_password(self):
        password_characters = []
        #run per password length or default to 8 if evaluated to false
        for character in range(self.length or 8):
            #list with functions of allowed modifiers
            allowed_functions_list = [] 
            for d in self.combination_state:
                if self.combination_state[d]["allowed"] == True:
                    allowed_functions_list.append(self.combination_state[d]["f"])
            random_allowed_function = choice(allowed_functions_list)
            password_characters.append(random_allowed_function())

        return "".join(password_characters)
