import copy


class State:
    # example: V -> V • NP [0,1]
    def __init__(self, begin, end, dot_index, position, debug):
        self.debug = debug
        self.begin = begin         # V
        self.end = end             # ['V', 'NP']
        self.dot_index = dot_index  # 1
        self.position = position   # (0, 1)

    def is_complete(self):
        return len(self.end) == self.dot_index

    def next_rule(self, rules):
        for rule in rules:
            if rule.begin == self.end[self.dot_index]:
                return rule

    def predictor(self, rules):
        # apply state to current entry
        states = []
        applicable_rule = self.next_rule(rules)
        for end in applicable_rule.ends:
            state = State(applicable_rule.begin, end, 0,
                          (self.position[1], self.position[1]), self.debug)
            states.append(state)
        return states

    def scanner(self, rules, sentence):
        # apply state to next entry
        applicable_rule = self.next_rule(rules)
        for end in applicable_rule.ends:
            end_word = end[0]
            if self.debug:
                print(f'end_word: {end_word}')
            for i in range(self.position[0], self.position[1]+1):
                if self.debug:
                    print(f'sentence: {sentence}')
                if end_word == sentence[i]:
                    return State(applicable_rule.begin, [end_word], 1, (self.position[0], self.position[1] + 1), self.debug)

    def completer(self, rules, states):
        # apply states to next entry
        # self must already be is_complete()
        new_states = []
        for state in states:
            if not state.is_complete():
                if state.end[state.dot_index] == self.begin:
                    new_states.append(State(state.begin, state.end, state.dot_index + 1,
                                            (state.position[0], self.position[1]), self.debug))
        return new_states

    def __str__(self):
        end_array = copy.deepcopy(self.end)
        end_array.insert(self.dot_index, '•')
        end_str = ' '.join(word for word in end_array)
        return f'{self.begin} -> {end_str} {list(self.position)}'

    def __eq__(self, other):
        return self.begin == other.begin and self.end == other.end and self.dot_index == other.dot_index and self.position == other.position

    def __ne__(self, other):
        return self.begin != other.begin or self.end != other.end or self.dot_index != other.dot_index or self.position != other.position
