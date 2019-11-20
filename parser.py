# Earley Parser

from configuration import Configuration
from chart import Chart

def main():
    config = Configuration()
    if config.args.debug: print(config.rules[0])
    chart = Chart(config.args.sentence, config.rules, config.args.debug)
    print(chart)

if __name__ == "__main__":
    main()







# # string_representation: ex.: NP
# class Piece:
#     def __init__(self, string_representation, terminal):
#         self.string_representation = string_representation
#         self.terminal = terminal