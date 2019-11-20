from state import State
from configuration import Configuration

config = Configuration()

# test State
print('test State.completer()')
states_to_be_completed = [State('VP', ['Verb', 'NP'], 1, (0,1), config.args.debug), State('VP', ['Verb', 'NP', 'PP'], 1, (0,1), config.args.debug)]
completion = State('NP', ['Det', 'N'], 2, (1,3), config.args.debug)
completed_states = (completion.completer(config.rules, states_to_be_completed))
if config.args.debug: print(*completed_states, sep = "\n")
assert(completed_states == [State('VP', ['Verb', 'NP',], 2, (0,3), config.args.debug), State('VP', ['Verb', 'NP', 'PP'], 2, (0,3), config.args.debug)])
print()

print('test State.scanner()')
scan_with_state = State('VP', ['Verb', 'NP'], 0, (0,0), False)
state_created_by_scanning = scan_with_state.scanner(config.rules, config.args.sentence)
if config.args.debug: print(state_created_by_scanning)
assert(state_created_by_scanning == State('Verb', ['book'], 1, (0,1), False))
print()

print('test State.predictor()')
start_predictor = State('S', ['VP'], 0, (0,0), False)
predicted_states = start_predictor.predictor(config.rules)
if config.args.debug: print(*predicted_states, sep = "\n")
print()
