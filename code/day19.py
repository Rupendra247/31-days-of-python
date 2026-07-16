# Goal: Secure your data.

# Concept: Encapsulation hides the internal data of an object from the outside.

# _member: Protected (convention, don't touch).

# __member: Private (name mangled, harder to access).

# Day 19: Encapsulation
class SecretVault:
    def __init__(self, code):
        self.__code = code  # Private attribute (prefixed with __)

    def verify_code(self, guess):
        return self.__code == guess

vault = SecretVault(1234)
# print(vault.__code) # This would raise an AttributeError!
print(vault.verify_code(1234)) # Correct way to interact with private data