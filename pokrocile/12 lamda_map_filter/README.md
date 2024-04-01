Lambda Funkce v Pythonu
======================

Lambda funkce v Pythonu jsou anonymní funkce definované pomocí klíčového slova `lambda`. Tyto funkce jsou obvykle krátké a jednoduché, vhodné pro použití na jednom místě.

Příklad Lambda Funkce
---------------------

Následující kód ukazuje příklad lambda funkce, která zdvojnásobí vstupní číslo:

```python
multiply_by_two = lambda x: x * 2

# Použití lambda funkce
result = multiply_by_two(5)
print(result)  # Vytiskne: 10
```


Funkce map() v Pythonu
======================

Funkce map() v Pythonu umožňuje aplikovat danou funkci na každý prvek v iterovatelném objektu (seznamu, tuple nebo řetězci). Níže je popis a příklad použití map():

```python
map(function, iterable, ...) 
```

* function: Funkce, která má být aplikována na každý prvek iterovatelného objektu.
* iterable: Jedno nebo více iterovatelných objektů, na které má být funkce aplikována.

```python
# Seznam čísel
numbers = [1, 2, 3, 4, 5]

# Lambda funkce pro zdvojnásobení čísel
multiply_by_two = lambda x: x * 2

# Použití map s lambda funkcí k zdvojnásobení každého čísla
doubled_numbers = map(multiply_by_two, numbers)

# Převedení výsledku na seznam (v Python 3 map() vrací iterátor)
doubled_numbers_list = list(doubled_numbers)

# Výsledek
print(doubled_numbers_list)
# Vytiskne: [2, 4, 6, 8, 10]
```

Funkce filter() v Pythonu
======================

Funkce filter() v Pythonu slouží k filtrování prvků v iterovatelném objektu (seznamu, tuple, nebo řetězci) na základě podmínky definované v funkci. Výsledkem je iterátor obsahující pouze ty prvky, které splňují zadanou podmínku.

Níže je popis a příklad použití filter():

```python
filter(function, iterable)
```
* function: Funkce, která určuje podmínku filtrování.
* iterable: Iterovatelný objekt, ze kterého jsou prvky filtrovány.

```python
# Seznam čísel
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lambda funkce pro filtrování sudých čísel
filter_even = lambda x: x % 2 == 0

# Použití filter s lambda funkcí pro filtrování sudých čísel
even_numbers = filter(filter_even, numbers)

# Převedení výsledku na seznam (v Python 3 filter() vrací iterátor)
even_numbers_list = list(even_numbers)

# Výsledek
print(even_numbers_list)
# Vytiskne: [2, 4, 6, 8, 10]
```