# Pokročilejší programování v Pythonu

https://www.umimeinformatiku.cz/cviceni-regularni-vyrazy

## Regulární výrazy
Regulární výrazy (nebo regex) jsou řetězce znaků, které definují vzory pro vyhledávání a manipulaci s textem. Tyto vzory jsou využívány v textových procesorech, programovacích jazycích a různých nástrojích pro práci s řetězci. Regulární výrazy umožňují flexibilní a mocné vyhledávání, filtraci a transformaci textových dat.

### Základní stavební bloky regulárních výrazů

1. **Základní znaky:**
   - Alfanumerické znaky: reprezentují samy sebe.
   - Speciální znaky: mají speciální význam a mohou označovat skupiny znaků, opakování atd.

2. **Speciální znaky pro kvantifikaci:**
   - `*`, `+`, `?`: Specifikují, kolikrát se předchozí znak nebo skupina mohou opakovat.

3. **Skupiny a rozsahy:**
   - `( )`: Vytvářejí skupiny znaků.
   - `[ ]`: Definují rozsahy znaků, ze kterých se může vybrat.

4. **Speciální znaky pro shodu s pozicí:**
   - `^`: Začátek řetězce.
   - `$`: Konec řetězce.
   - `\b`: Hranice slova.

5. **Speciální znaky pro shodu s třídami znaků:**
   - `\d`: Shoduje se s číslicí.
   - `\D`: Shoduje se s nečíslicovým znakem.
   - `\w`: Shoduje se s alfanumerickým znakem (včetně podtržítka).
   - `\W`: Shoduje se s nealfanumerickým znakem.
   - `\s`: Shoduje se s mezerou nebo tabulátorem.
   - `\S`: Shoduje se s neprázdným znakem.

### Příklad regulárního výrazu

Příklad regulárního výrazu: `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`. Tento regulární výraz odpovídá e-mailovým adresám a zahrnuje různé konstrukce pro validaci uživatelské části, domény a top-level domény e-mailu.
