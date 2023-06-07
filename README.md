Agradeça a Deus pelo pd.NA! Vou te mostrar neste vídeo como lidar com "Not a Number"

As vantagens de usar "pd.NA" em vez de "NaN" (Not a Number) ou "None" para representar valores ausentes são:

Compatibilidade: O "pd.NA" é uma nova opção de representação de valores ausentes introduzida no Pandas 1.0, que é compatível com as operações existentes do Pandas. Ele foi projetado para funcionar de forma consistente com os outros valores nos objetos do Pandas, permitindo operações eficientes em dados ausentes.

Tipagem: O "pd.NA" possui um tipo específico chamado "pd._libs.missing.NAType". Isso permite que o Pandas faça inferências de tipos adequados para colunas que contenham "pd.NA". Por exemplo, se uma coluna contiver apenas "pd.NA", o Pandas pode inferir o tipo "float" para essa coluna.

Semântica clara: O "pd.NA" é projetado para fornecer uma semântica clara para representar valores ausentes. Ele é tratado como um valor distinto, permitindo que você identifique facilmente onde existem valores ausentes em seus dados e execute operações específicas para lidar com eles.

Compatibilidade com operações: O "pd.NA" é compatível com várias operações do Pandas. Você pode usar métodos como "isna()", "fillna()" e "dropna()" para manipular e filtrar dados ausentes. Além disso, "pd.NA" se comporta adequadamente em operações aritméticas e lógicas, retornando "pd.NA" quando combinado com outros valores

[![YT](https://i.ytimg.com/vi/T0aK09lMtV8/maxresdefault.jpg)](https://www.youtube.com/watch?v=T0aK09lMtV8)
[https://www.youtube.com/watch?v=T0aK09lMtV8]()
