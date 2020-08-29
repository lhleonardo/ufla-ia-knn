# KNN - Implementação

## Introdução

Implementação do algoritmo KNN para classificação aplicado à técnicas de Inteligência Artificial, sob orientação do Prof. Dr. Ahmed Ali Abdalla Esmin.

Os arquivos principais da execução do código estão presentes na pasta `src`, sendo definidos como:

- `main.py`: contém a execução principal do programa, contendo o intervalo de valores _k_ que serão utilizados na execução e o arquivo que será usado para análise;
- `knn.py`: contém a implementação do KNN e todas as operações necessárias para realização do processo;
- `analytics.py`: contém todo processo de análise da corretude das predições realizadas pelo KNN, construindo a matriz de confusão e verificação de acurrácia para as predições;

## Formato de apresentação

Para sua execução é necessário apenas o comando:

```
python3 main.py
```

O formato de saída da aplicação é dado por:

```
NUMERO_K
MATRIZ_CONFUSAO

ACURACIA_ACERTOS
ACURACIA_FALHAS
```

Uma execução para o spambase é definida logo abaixo:

```
k=1
[[265  70]
 [101 493]]
81.59311087190528
18.40688912809472

k=3
[[272  72]
 [ 89 471]]
82.19026548672566
17.809734513274336

k=5
[[293  72]
 [ 83 454]]
82.8159645232816
17.184035476718407

k=7
[[256  93]
 [110 471]]
78.17204301075269
21.827956989247312
```

## Resultados e análises

### Spambase

Para a base de dados spamBase foi demonstrado uma melhor acurácia para valores de k mais baixos como 1, porém essa taxa pode variar uma vez que os dados de teste e treinamento estão sendo escolhidos de forma randômica.

### IrisBase

Para a base de dados irisBase foi demonstrado uma melhor acurácia para valores de k mais altos como 5 e 7, porém assim como na spamBase os dados de teste e treinamento também estão sendo escolhidos de forma randômica podendo ocorrer variâncias na acurácia para determinado k.

Pode-se observar que o KNN é um algoritmo simples e bastante eficaz, demonstrando uma boa precisão na maioria dos casos aplicados.

## Autores

Repositório criado com intuito em obtenção de nota para o trabalho final de Inteligência Artificial. Turma ministrada em 2020/1.

| [<img src="https://avatars0.githubusercontent.com/u/11544276?v=4&s=450" width=115><br><sub>@lhleonardo</sub>](https://github.com/lhleonardo) <br><sub>Leonardo Braz</sub> | [<img src="https://avatars0.githubusercontent.com/u/37846911?s=460&v=4" width=115><br><sub>@gbochikubo</sub>](https://github.com/gbochikubo) <br><sub>Guilherme Ochikubo</sub> |
| :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |

