# introdução a biblioteca pandas

import pandas as pd

data = {
    "nome" : ["josé", "maria", "joão"],
    "idade": [10, 40, 39],
    "cpf": ["0123345345", "0989009908", "1239454345"]
}


print(pd.DataFrame(data))
