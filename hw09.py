"""
DSC 20 Homework 09
Name: Joshua Chuang
PID:  A16233072
"""


# Question 1
def check_inputs(input1, input2):
    """
    # TODO: Add method description and at least 3 new doctests #
    A function that checks if input1 is a list of numerical values and input2
    is a numerical value also found in input1. Returns 'input validated' if
    passes all the checks. If not, it will raise an error with an error message
    explaining why.
    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'
    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1
    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type
    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric
    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type

    >>> check_inputs([1], 1)
    'Input validated'
    >>> check_inputs(['0', 0], 0)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 0 is not numeric
    >>> check_inputs([1, 0, 83], 3)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1
    """
    if not isinstance(input1, list):
        raise TypeError('input1 is not the correct type')
    for i, j in enumerate(input1):
        if not isinstance(j, (float, int)):
            raise TypeError('The element at index {} is not numeric'.format(i))
    if not isinstance(input2, (float, int)):
        raise TypeError('input2 is not the correct type')
    if input2 not in input1:
        raise TypeError('input2 not in input1')
    return 'Input validated'


# Question 2
def load_file(filename):
    """
    # TODO: Add method description and at least 3 new doctests #
    A function that checks if filename is a string and a valid file that is
    not empty. If it passes the checks, it will return the number of words in
    the file.
    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filename is not a string
    >>> load_file('files/ten_words.txt')
    10
    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty
    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist

    >>> load_file('files/file1.txt')
    5
    >>> load_file(['0'])
    Traceback (most recent call last):
    ...
    TypeError: filename is not a string
    >>> load_file('file1')
    Traceback (most recent call last):
    ...
    FileNotFoundError: file1 does not exist
    """
    if not isinstance(filename, str):
        raise TypeError('filename is not a string')
    try:
        with open(filename, 'r') as f:
            text = f.read()
            words = text.split()
    except FileNotFoundError:
        raise FileNotFoundError(filename + ' does not exist')
    else:
        if len(words) == 0:
            raise ValueError('File is empty')
        return len(words)


# Question 3
def q3_doctests():
    """
    Q3 doctests go here.

    >>> h = Nonmetal("H")
    >>> h
    Nonmetal("H")
    >>> print(h)
    Nonmetal name: H, atomic number: 8, period: 2, group: 2
    >>> h.get_mass()
    66

    >>> f = Metal("F")
    >>> f
    Metal("F")
    >>> print(f)
    Metal name: F, atomic number: 6, period: 1, group: 6
    >>> f.get_mass()
    78

    >>> f == h
    False
    >>> f != h
    True
    >>> f > h
    True
    >>> f < h
    False

    >>> water = Compound("H2O1")
    >>> water
    Compound("H2O1")
    >>> print(water)
    H2O1
    >>> water.elements
    {'H': 2, 'O': 1}
    >>> water.get_compound_mass()
    255

    >>> yummy_metal = Compound("U1")
    >>> dsc2 = Compound("D2S2C2")
    >>> dsc3 = Compound("D3S3C3")
    >>> cse = Compound("C7S8E9")
    >>> lava = Compound("H3O4")
    >>> obsidian = Compound("H5O5")
    >>> smelly_gas = Compound("H2")

    >>> water == yummy_metal
    True
    >>> water <= yummy_metal
    True
    >>> water > dsc2
    False

    >>> dsc2 + dsc3
    Compound("C5D5S5")
    >>> water - smelly_gas
    Compound("O1")
    >>> dsc2 + cse
    Traceback (most recent call last):
    ...
    ValueError
    >>> water - lava
    Traceback (most recent call last):
    ...
    ValueError
    >>> water + lava == obsidian
    True

    >>> o = Nonmetal('O')
    >>> n = Nonmetal('N')
    >>> c = Nonmetal('C')

    >>> k = Metal('K')
    >>> m = Metal('M')
    >>> a = Metal('A')

    >>> o.get_mass()
    123
    >>> n.get_mass()
    115
    >>> c.get_mass()
    25
    >>> k.get_mass()
    137
    >>> m.get_mass()
    163
    >>> a.get_mass()
    13

    >>> o
    Nonmetal("O")
    >>> n
    Nonmetal("N")
    >>> c
    Nonmetal("C")
    >>> k
    Metal("K")
    >>> m
    Metal("M")
    >>> a
    Metal("A")
    >>> print(o)
    Nonmetal name: O, atomic number: 15, period: 3, group: 3
    >>> print(n)
    Nonmetal name: N, atomic number: 14, period: 3, group: 2
    >>> print(c)
    Nonmetal name: C, atomic number: 3, period: 1, group: 3
    >>> print(k)
    Metal name: K, atomic number: 11, period: 2, group: 5
    >>> print(m)
    Metal name: M, atomic number: 13, period: 2, group: 7
    >>> print(a)
    Metal name: A, atomic number: 1, period: 1, group: 1

    >>> o < n
    False
    >>> k > a
    True
    >>> m == a
    False
    >>> a <= c
    True
    >>> k >= o
    True
    >>> m != a
    True

    >>> oxygen = Compound('O2')
    >>> co2 = Compound('C1O2')
    >>> acid = Compound('H1I1')

    >>> oxygen.get_compound_mass()
    246
    >>> co2.get_compound_mass()
    271
    >>> acid.get_compound_mass()
    140

    >>> oxygen.elements
    {'O': 2}
    >>> co2.elements
    {'C': 1, 'O': 2}
    >>> acid.elements
    {'H': 1, 'I': 1}

    >>> oxygen
    Compound("O2")
    >>> print(oxygen)
    O2
    >>> co2
    Compound("C1O2")
    >>> print(co2)
    C1O2
    >>> acid
    Compound("H1I1")
    >>> print(acid)
    H1I1

    >>> oxygen < co2
    True
    >>> acid <= oxygen
    True
    >>> acid > co2
    False
    >>> oxygen >= co2
    False
    >>> co2 == co2
    True
    >>> co2 != co2
    False
    >>> oxygen + co2
    Compound("C1O4")
    >>> co2 - oxygen
    Compound("C1")
    """
    return


LIST_METAL = "FKLPQRUVWXZ"


class Element:
    """
    # TODO: add class docstring #
    A class that creates an element instance.
    """

    def __init__(self, name):
        """
        Constructor of Element
        Input validation is required
        Parameter:
        name (str): a single uppercase character from 'A' to 'Z' that
                    represents the name of the element
        """
        # YOUR CODE GOES HERE #
        if any([not isinstance(name, str), len(name) != 1, name.islower()]):
            raise ValueError('invalid argument')
        num_diff = 64
        period_len = 6
        self.name = name
        self.atomic_num = ord(name) - num_diff
        self.period = self.atomic_num//(period_len + 1) + 1
        self.group = self.atomic_num - (period_len * (self.period - 1))

    def get_mass(self):
        """
        Returns atomic mass of this element
        This method is a placeholder to avoid style check errors in some
        editors or tools. You will overwrite this method in the subclasses.
        """
        # DO NOT MODIFY #
        raise NotImplementedError("must be implemented in the subclasses")

    def __eq__(self, other_elem):
        """
        Returns True when two Elements are equal.
        Equality is determined by their atomic mass
        """
        # YOUR CODE GOES HERE #
        return self.get_mass() == other_elem.get_mass()

    def __ne__(self, other_elem):
        """ Returns True when two Elements are not equal """
        # YOUR CODE GOES HERE #
        return self.get_mass() != other_elem.get_mass()

    def __gt__(self, other_elem):
        """ Returns True when this Element is greater than the other """
        # YOUR CODE GOES HERE #
        return self.get_mass() > other_elem.get_mass()

    def __ge__(self, other_elem):
        """
        Returns True when this Element is greater than or
        equal to the other
        """
        # YOUR CODE GOES HERE #
        return self.get_mass() >= other_elem.get_mass()

    def __lt__(self, other_elem):
        """ Returns True when this Element is less than the other """
        # YOUR CODE GOES HERE #
        return self.get_mass() < other_elem.get_mass()

    def __le__(self, other_elem):
        """
        Returns True when this Element is less than or
        equal to the other
        """
        # YOUR CODE GOES HERE #
        return self.get_mass() <= other_elem.get_mass()

    def __repr__(self):
        """ Returns object representation of this Element """
        # uncomment the following code
        repr_form = "{0}(\"{1}\")"
        class_name = self.__class__.__name__
        repr_form = repr_form.format(class_name, self.name)
        return repr_form


class Nonmetal(Element):
    """
    # TODO: add class docstring #
    A child class of Element that creates a nonmetal instance.
    """

    def get_mass(self):
        """ Returns atomic mass of this Nonmetal element """
        # YOUR CODE GOES HERE #
        nonmetal_mass = 8
        return nonmetal_mass * self.atomic_num + self.period

    def __str__(self):
        """ Returns string representation of this Nonmetal element """
        # uncomment the following code
        str_form = \
            "Nonmetal name: {}, atomic number: {}, period: {}, group: {}"
        return str_form.format(
            self.name, self.atomic_num, self.period, self.group)


class Metal(Element):
    """
    # TODO: add class docstring #
    A child class of Element that creates a metal instance.
    """

    def get_mass(self):
        """ Returns atomic mass of this Metal element """
        # YOUR CODE GOES HERE #
        metal_mass = 12
        return metal_mass * self.atomic_num + self.group

    def __str__(self):
        """ Returns string representation of this Metal element """
        # uncomment the following code
        str_form = "Metal name: {}, atomic number: {}, period: {}, group: {}"
        return str_form.format(
            self.name, self.atomic_num, self.period, self.group)


class Compound:
    """
    # TODO: add class docstring #
    A class that creates a compound instance.
    """

    def __init__(self, name):
        """
        Constructor of Compound
        Input validation is required
        Parameter:
        name (str): a string that represents the name of the compound
        """
        # YOUR CODE GOES HERE #
        if not isinstance(name, str):
            raise ValueError('invalid argument')
        for i, j in enumerate(name):
            if i % 2 == 0 & j.isupper():
                continue
            elif i % 2 == 1 & j.isnumeric():
                continue
            else:
                raise ValueError('invalid argument')
        self.name = name
        self.elements = (
            {j: int(name[i + 1]) for i, j in enumerate(name) if j.isupper()}
            )
        self.compound_mass = 0
        for i in self.elements.keys():
            if i in LIST_METAL:
                metal = Metal(i)
                self.compound_mass += metal.get_mass() * self.elements[i]
            else:
                nonmetal = Nonmetal(i)
                self.compound_mass += nonmetal.get_mass() * self.elements[i]

    def get_compound_mass(self):
        """ A simple getter of compound_mass """
        # YOUR CODE GOES HERE #
        return self.compound_mass

    def __eq__(self, other_comp):
        """
        Returns True when two Compounds are equal.
        Equality is determined by their compound mass
        """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() == other_comp.get_compound_mass()

    def __ne__(self, other_comp):
        """ Returns True when two Compounds are not equal """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() != other_comp.get_compound_mass()

    def __gt__(self, other_comp):
        """ Returns True when this Compound is greater than the other """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() > other_comp.get_compound_mass()

    def __ge__(self, other_comp):
        """
        Returns True when this Compound is greater than or
        equal to the other
        """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() >= other_comp.get_compound_mass()

    def __lt__(self, other_comp):
        """ Returns True when this Compound is less than the other """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() < other_comp.get_compound_mass()

    def __le__(self, other_comp):
        """
        Returns True when this Compound is less than or
        equal to the other
        """
        # YOUR CODE GOES HERE #
        return self.get_compound_mass() <= other_comp.get_compound_mass()

    def __add__(self, other_comp):
        """
        Synthesize a new Compound by adding this Compound with another
        Exception:
        ValueError will be raised if the product is invalid
        """
        # YOUR CODE GOES HERE #
        limit = 9
        new_comp = dict(self.elements)
        for i in other_comp.elements.keys():
            if i in new_comp.keys():
                new_comp[i] += other_comp.elements[i]
            else:
                new_comp[i] = other_comp.elements[i]
        if any([i > limit for i in new_comp.values()]):
            raise ValueError()
        new_comp_name = ''.join(
            sorted([k + str(v) for k, v in new_comp.items()]))
        return Compound(new_comp_name)

    def __sub__(self, other_comp):
        """
        Decompose this Compound by subtracting another from it. A new product
        is returned after decomposition
        Exception:
        ValueError will be raised if the product is invalid
        """
        # YOUR CODE GOES HERE #
        new_comp = dict(self.elements)
        for i in other_comp.elements.keys():
            if i in new_comp.keys():
                new_comp[i] -= other_comp.elements[i]
            else:
                raise ValueError()
        if any([i < 0 for i in new_comp.values()]):
            raise ValueError()
        for k, v in list(new_comp.items()):
            if v == 0:
                del new_comp[k]
        new_comp_name = ''.join(
            sorted([k + str(v) for k, v in new_comp.items()]))
        return Compound(new_comp_name)

    def __str__(self):
        """ Returns string representation of this Compound """
        # YOUR CODE GOES HERE #
        return self.name

    def __repr__(self):
        """ Returns object representation of this Compound """
        # uncomment the following code
        repr_form = "{0}(\"{1}\")"
        class_name = self.__class__.__name__
        repr_form = repr_form.format(class_name, self.name)
        return repr_form
