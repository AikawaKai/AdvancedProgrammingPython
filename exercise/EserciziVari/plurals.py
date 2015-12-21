import re


def match_sxz(noun):
    return re.search('[sxz]$', noun)


def apply_sxz(noun):
    return re.sub('$', 'es', noun)


def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)


def apply_h(noun):
    return re.sub('$', 'es', noun)


def match_y(noun):
    return re.search('[^aeiou]y$', noun)


def apply_y(noun):
    return re.sub('y$', 'ies', noun)


def match_default(noun):
    return True


def apply_default(noun):
    return noun + 's'

rules = [(match_sxz, apply_sxz), (match_h, apply_h), (match_y, apply_y),
         (match_default, apply_default)]

patterns = [('[sxz]$', '$', 'es'), ('[^aeioudgkprt]h$', '$', 'es'),
            ('[^aeiou]y$', 'y$', 'ies'), ('$', '$', 's')]


def build_match_and_apply(pattern, search, replace):
    def match(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (match, apply_rule)

rulez = [build_match_and_apply(pattern, search, replace)
         for (pattern, search, replace) in patterns]


def plural(noun):
    for matches_rule, apply_rule in rulez:
        if matches_rule(noun):
            return apply_rule(noun)


if __name__ == '__main__':
    print(plural('home'), plural('cat'), plural('mathematica'),
          plural('history'))
