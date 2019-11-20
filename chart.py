from state import State

class Chart:
    def __init__(self, sentence, rules, debug):
        self.debug = debug
        self.entries = [[] for i in range(len(sentence)+1)]
        self.produce_chart(sentence, rules)

    def produce_chart(self, sentence, rules):
        self.entries[0] = self.get_initial_states(rules)
        for i in range(0, len(sentence)+1):  # produce next iteration of the chart
            # incomplete_state_exists = False
            for state in self.entries[i]:
                if self.debug:
                    print("entry index: ", i)
                # if self.debug: print(state)
                if not state.is_complete():
                    # incomplete_state_exists = True
                    if not state.next_rule(rules).part_of_speech:
                        if self.debug:
                            print(
                                f'state where next rule is not part of speech: {state}')
                        new_states = state.predictor(rules)
                        if self.debug:
                            print(f'\tpredicted states for this state: ')
                        for new_state in new_states:
                            if self.debug:
                                print(
                                    f'\t\t{new_state} of type {type(new_state)}')
                            if new_state not in self.entries[i]:
                                self.entries[i].append(new_state)
                    else:
                        if self.debug:
                            print(
                                f'state where next rule is part of speech: {state}')
                        new_state = state.scanner(rules, sentence)
                        if new_state is not None:
                            # self.create_entry_if_not_exists(i+1)
                            if new_state not in self.entries[i+1]:
                                if self.debug:
                                    print(f'new_state.end: {new_state.end}')
                                    print(f'{new_state} of type {type(new_state)}')
                                self.entries[i+1].append(new_state)
                else:
                    if self.debug:
                        print(f'completed state: {state}')
                    new_states = state.completer(rules, self.entries[i])
                    if new_states:
                        # self.create_entry_if_not_exists(i+1)
                        for new_state in new_states:
                            print(f'newly completed state: {state}')
                            if new_state not in self.entries[i+1]:
                                self.entries[i+1].extend(new_states)
            # if not incomplete_state_exists:
            #     break
            # if len(self.entries) >= i + 2:
                # i += 1

    def get_initial_states(self, rules):
        states = []
        for rule in rules:
            if rule.begin == 'S':
                for end in rule.ends:
                    state = State(rule.begin, end, 0, (0, 0), self.debug)
                    print(state)
                    states.append(state)
        return states

    def create_entry_if_not_exists(self, entry_index):
        # if self.debug: print('entry index:', entry_index)
        # if self.debug: print('length of entries', len(self.entries))
        if entry_index + 1 > len(self.entries):
            self.entries.append([])
        # if self.debug: print('entry index:', entry_index)
        # if self.debug: print('length of entries', len(self.entries))

    def __str__(self):
        output = '\nChart:\n'
        for i in range(len(self.entries)):
            output += (f'\tentry index {i}\n')
            for state in self.entries[i]:
                output += '\t\t' + str(state) + '\n'
        return output
