import re

rules = []


#  closure generator for pluralize re.match re.sub
def closureRules(rule, search, value):
    def genRule(string):
        return re.search(rule, string)

    def genApplyRule(string):
        return re.sub(search, value, string)

    return (genRule, genApplyRule)


patterns = [('[sxzo]$', '$', 'es'), ('[^aeioudgkprt]h$', '$', 'es'),
            ('[^aeiou]y$', 'y$', 'ies'), ('$', '$', 's')]


def init_rules_applyrule():
    global rules
    global patterns
    for pattern, search, value in patterns:
        (rulef, applyrule) = closureRules(pattern, search, value)
        rules.append((rulef, applyrule))

init_rules_applyrule()


def pluralizeFun(string):
    for rulef, applyrule in rules:
        if rulef(string):
            return applyrule(string)
