# I'm sorry

# This breaks the string literal rule, but has the same effect as a direct import, so I'm not concerned

import io
import sys

old_stdout = sys.stdout
sys.stdout = io.StringIO()


### Bad code warning ----------------------------------------

line_gen = (lambda t, r: map(lambda line: chr(32).join(line), list(
    (lambda tran, text:
        (lambda derot:
            (lambda lines:
                list([(yield (lambda words:
                    r.sample(list(map(lambda word: word.strip(derot[63] + derot[855]), words)), len(words))
                )(line.split())) for line in lines[1:]])
            )(derot.splitlines())
        )(text.translate(tran))
    )(str.maketrans(t.d), t.s))[1:])
)(__import__("this"), __import__("random"))

### Bad code over -------------------------------------------


sys.stdout = old_stdout

for l in line_gen:
    print(l)
