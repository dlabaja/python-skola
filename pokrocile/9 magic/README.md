__init__(self, ...): Konstruktor, volá se při vytváření nové instance třídy.

__del__(self): Destruktor, volá se při odstranění instance z paměti. Není vždy spolehlivě volán, není doporučováno spoléhat se na něj pro správu zdrojů.

__str__(self): Definuje textovou reprezentaci objektu pro funkce str() a print().

__repr__(self): Definuje reprezentaci objektu, která měla být nezávislá na lidské interpretaci a používá se v kombinaci s funkcí repr().

__len__(self): Definuje délku objektu pro funkci len().

__getitem__(self, key): Definuje chování pro indexování objektu, tedy umožňuje použití hranatých závorek pro získání hodnoty (obj[key]).

__setitem__(self, key, value): Definuje chování pro nastavení hodnoty pomocí indexu (obj[key] = value).

__delitem__(self, key): Definuje chování pro odstranění hodnoty pomocí indexu (del obj[key]).

__iter__(self): Definuje iterátor pro objekt, umožňuje použití objektu v for smyčce.

__next__(self): Definuje chování pro získání další hodnoty v iterátoru.

__contains__(self, item): Definuje chování pro operátor in, umožňuje zjistit, zda objekt obsahuje danou hodnotu.

__call__(self, ...): Umožňuje volání instance třídy jako funkce.

__eq__(self, other): Definuje chování pro porovnání rovnosti pomocí operátoru ==.

__ne__(self, other): Definuje chování pro porovnání nerovnosti pomocí operátoru !=.

__lt__(self, other), __le__(self, other), __gt__(self, other), __ge__(self, other): Definují chování pro porovnání (např. <, <=, >, >=).

__add__(self, other), __sub__(self, other), __mul__(self, other), __truediv__(self, other): Definují chování pro aritmetické operátory (např. +, -, *, /).

__hash__(self): Definuje chování pro výpočet hashe objektu. Je používáno například při použití objektu jako klíče v slovnících.

__bool__(self): Definuje chování pro zjištění, zda je objekt považován za pravdivý nebo ne, když je používán v kontextu podmíněného výrazu (if obj:).

__enter__(self), __exit__(self, exc_type, exc_value, traceback): Tyto metody se používají v kontextových managerech. __enter__ se volá při vstupu do bloku with, a __exit__ se volá při opuštění bloku with. Například pro správu zdrojů nebo manipulaci s kontextem.

__copy__(self): Definuje chování pro kopírování objektu pomocí funkce copy.copy().

__deepcopy__(self, memo): Definuje chování pro hluboké kopírování objektu pomocí funkce copy.deepcopy().

__instancecheck__(self, instance): Definuje chování pro kontrolu, zda je objekt instancí dané třídy (isinstance(obj, cls)).

__subclasscheck__(self, subclass): Definuje chování pro kontrolu, zda je třída podtřídou dané třídy (issubclass(subclass, cls)).

__dir__(self): Definuje chování pro získání seznamu atributů objektu, který se používá při volání funkce dir().

__setattr__(self, name, value): Definuje chování pro nastavení hodnoty atributu (obj.name = value).

__getattr__(self, name): Definuje chování pro čtení hodnoty neexistujícího atributu (obj.name), pokud atribut není nalezen.

__delattr__(self, name): Definuje chování pro odstranění atributu (del obj.name).

__format__(self, format_spec): Definuje chování pro formátování řetězce pomocí metody format().

__call__(self, *args, **kwargs): Definuje chování pro volání instance třídy jako funkce (obj()).

__sizeof__(self): Definuje chování pro získání velikosti objektu v bajtech pomocí funkce sys.getsizeof().