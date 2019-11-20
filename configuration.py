import argparse
import json

from rule import Rule

class Configuration:
    def __init__(self):
        self.args = self.get_cmd_line_args()
        self.rules = self.get_rules_from_json(self.args.filename)

    def get_cmd_line_args(self):
        # create parser
        parser = argparse.ArgumentParser(description = "Parse arguments for Earley Parser")

        # add arguments to parser
        parser.add_argument("--sentence", "-s", help="the string to be parsed", required=True)
        parser.add_argument("--filename", "-f", help="the json file in which the rules which define the grammar are stored", required=True)
        parser.add_argument("--debug", "-d", action='store_true', help="whether or not to parse", required=True)

        # split sentence argument into array of words
        args = parser.parse_args()
        args.sentence = args.sentence.split(' ')
        return args
    
    def get_rules_from_json(self, filename):
        rules = []
        with open(filename) as fp:
            data = json.load(fp)
            for datum in data:
                rule = Rule(datum, data[datum]['ends'], data[datum]['terminal'], data[datum]['part_of_speech'])
                rules.append(rule)
        return rules
