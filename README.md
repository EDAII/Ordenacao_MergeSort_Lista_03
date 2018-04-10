# Ordenacao_MergeSort_Lista_3
Alunos: Iago Carvalho 15/0011849 | Eliseu Egewarth 12/0029693

Python 2.7

```
apt-get install python-tk
```

```
pip install numpy matplotlib
```

Opcional tool
```
pip install ipython ipdb
```


RUN:
```
python Lista_3.py
```
Para fazer a análise performática do algoritmo, altere as seguintes linhas:
```python
if __name__ == '__main__':
    main() # comente esta linha e descomente a linha abaixo.
    # performance()
```
Execute o script e aguarde que todos os casos sejam testados(Verifique se a sua máquina tem memória suficiente para testar o maior caso `1000000`)  
OBS: Caso a quantidade de elementos alocados em memória ultrapasse a capacidade da memória RAM da sua máquina, a área de `swap`, se existir, será utilizada e diminirá drasticamente a performance do algorítimo.
```
python Lista_3.py
```
O resultado será salvo no arquivo `valores.txt` (preveamente escrito, pode ser apagado). Execute o comando abaixo para gerar o gráfico:
```
python plot_result.py
```

O gráfico abaixo é resultado da execução do comando `python plot_result.py`.

![Gráfico de Performance](/img/performance_graph.png)