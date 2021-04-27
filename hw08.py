"""
DSC 20 Homework 08
Name: Joshua Chuang
PID:  A16233072
"""


# Question 1
def course_doctests():
    """
    Doctests for Course.
    >>> dsc20 = Course("DSC20", "Intro to Programming", "Marina Langlois",
    ... 150, False)
    >>> print(dsc20)
    DSC20: Intro to Programming, a lower-division course instructed by Marina \
Langlois, allows 150 students to enroll.
    >>> dsc20
    Course('DSC20', 'Intro to Programming', 'Marina Langlois', 150, False)

    >>> dsc106 = Course("DSC106", "Intro to Data Visualization",
    ... "Thomas Powell", 100, True)
    >>> print(dsc106)
    DSC106: Intro to Data Visualization, an upper-division course instructed \
by Thomas Powell, allows 100 students to enroll.
    >>> dsc106
    Course('DSC106', 'Intro to Data Visualization', 'Thomas Powell', 100, True)

    # TODO: Create three additional Course instances, and for each object \
create
    #       a set of doctests similar to the above ones.

    >>> cogs14b = Course("COGS14B", "Intro to Statistical Analysis",
    ... "Steve Barrera", 220, False)
    >>> print(cogs14b)
    COGS14B: Intro to Statistical Analysis, a lower-division course \
instructed by Steve Barrera, allows 220 students to enroll.
    >>> cogs14b
    Course('COGS14B', 'Intro to Statistical Analysis', 'Steve Barrera', 220, \
False)

    >>> wcwp10b = Course("WCWP10B", "Warren Writing", "Iman Muniz", 15, False)
    >>> print(wcwp10b)
    WCWP10B: Warren Writing, a lower-division course instructed by Iman \
Muniz, allows 15 students to enroll.
    >>> wcwp10b
    Course('WCWP10B', 'Warren Writing', 'Iman Muniz', 15, False)

    >>> dsc100 = Course("DSC100", "Intro to Data Management", "Mikio Aoi",
    ... "200", True)
    >>> print(dsc100)
    DSC100: Intro to Data Management, an upper-division course instructed by \
Mikio Aoi, allows 200 students to enroll.
    >>> dsc100
    Course('DSC100', 'Intro to Data Management', 'Mikio Aoi', 200, True)
    """
    return


class Course:
    """
    # TODO: Add class description #
    A class that creates a course instance.
    """

    def __init__(self, course_code, name, instructor, \
                 enrollment_limit, is_upperdiv):
        """
        Constructor of Course class. DO NOT CHANGE THIS.
        Contains the instance attributes for each course.
        """
        self.course_code = course_code
        self.name = name
        self.instructor = instructor
        self.enrollment_limit = enrollment_limit
        self.is_upperdiv = is_upperdiv

    def __str__(self):
        """
        # TODO: Add method description #
        Sets a string representation of an object when printed.
        """
        # YOUR CODE GOES HERE #
        if self.is_upperdiv:
            div_level = 'an upper-division'
        else:
            div_level = 'a lower-division'
        return (
            "{}: {}, {} course instructed by {}, allows {} students to enroll."
            ).format(
                self.course_code,
                self.name, div_level,
                self.instructor,
                self.enrollment_limit)

    def __repr__(self):
        """
        # TODO: Add method description #
        Sets the object representation in string format.
        """
        # YOUR CODE GOES HERE #
        return "Course('{}', '{}', '{}', {}, {})".format(
                self.course_code,
                self.name,
                self.instructor,
                self.enrollment_limit,
                self.is_upperdiv)


# Question 2
def find_two_sums_rec(main, sub):
    """
    # TODO: Add method description and at least 3 new doctests #
    A function that returns a tuple that contains the sums of the numbers in
    both main and sub and the sums of the numbers in main that are not in sub.
    >>> main_seq = [0, 1, 1, 2, 3, 3, 4, 5, 5]
    >>> find_two_sums_rec(main_seq, [])
    (0, 24)
    >>> find_two_sums_rec(main_seq, [1, 2])
    (4, 20)
    >>> find_two_sums_rec(main_seq, [3, 4, 5])
    (20, 4)

    >>> main_seq_2 = [1, 5, 1, 1, 10]
    >>> main_seq_3 = []
    >>> find_two_sums_rec(main_seq_3, [])
    (0, 0)
    >>> find_two_sums_rec(main_seq_2, [5, 0, 2])
    (5, 13)
    >>> find_two_sums_rec(main_seq_2, main_seq)
    (8, 10)
    """
    # YOUR CODE GOES HERE #
    if len(main) == 0:
        return (0, 0)
    if main[0] in sub:
        return (main[0] + find_two_sums_rec(main[1:], sub)[0],
                find_two_sums_rec(main[1:], sub)[1])
    return (find_two_sums_rec(main[1:], sub)[0],
            main[0] + find_two_sums_rec(main[1:], sub)[1])


# Question 3
def counter_doctests():
    """
    Doctests for Counter and AlphanumericCounter.
    >>> counter = Counter()
    >>> counter.size()
    0
    >>> counter.add_items([123, 123, "abc", (10, 10), (10, 20)])
    >>> counter.size()
    5
    >>> counter.get_count(123)
    2
    >>> counter.get_count("dsc20")
    0
    >>> counter.get_all_counts()
    {123: 2, 'abc': 1, (10, 10): 1, (10, 20): 1}
    >>> an_counter = AlphanumericCounter()
    >>> an_counter.size()
    0
    >>> len(an_counter.counts)
    62
    >>> an_counter.add_items("DSC 20 (Marina Langlois)")
    >>> an_counter.size()
    19
    >>> an_counter.get_count("a")
    3
    >>> an_counter.get_count("?")
    0
    >>> an_counter.get_all_counts()
    {'0': 1, '2': 1, 'a': 3, 'g': 1, 'i': 2, 'l': 1, 'n': 2, 'o': 1, \
'r': 1, 's': 1, 'C': 1, 'D': 1, 'L': 1, 'M': 1, 'S': 1}

    # TODO: Initialize at least 1 new instance for each class #
    # TODO: Add at least 3 new doctests for each method #

    >>> counter_2 = Counter()
    >>> counter_2.size()
    0
    >>> counter_2.add_items([1, 1, 'cd', 9])
    >>> counter_2.size()
    4
    >>> counter_2.get_all_counts()
    {1: 2, 'cd': 1, 9: 1}
    >>> counter_2.get_count(9)
    1
    >>> counter_2.add_items([3])
    >>> counter_2.get_count(1)
    2
    >>> counter_2.get_all_counts()
    {1: 2, 'cd': 1, 9: 1, 3: 1}
    >>> counter_2.add_items([(1, 2), (0, 'a')])
    >>> counter_2.size()
    7
    >>> counter_2.get_all_counts()
    {1: 2, 'cd': 1, 9: 1, 3: 1, (1, 2): 1, (0, 'a'): 1}
    >>> counter_2.get_count((0, 'a'))
    1

    >>> an_counter_2 = AlphanumericCounter()
    >>> an_counter_2.get_index('5')
    5
    >>> an_counter_2.get_index('*')
    -1
    >>> an_counter_2.get_index('R')
    53
    >>> an_counter_2.get_char(61)
    'Z'
    >>> an_counter_2.get_char(0)
    '0'
    >>> an_counter_2.get_char(35)
    'z'
    >>> an_counter_2.size()
    0
    >>> an_counter_2.add_items("hello, I am taking DSC 20!")
    >>> an_counter_2.size()
    19
    >>> an_counter_2.get_count("a")
    2
    >>> an_counter_2.get_count("!")
    0
    >>> an_counter_2.get_all_counts()
    {'0': 1, '2': 1, 'a': 2, 'e': 1, 'g': 1, 'h': 1, 'i': 1, 'k': 1, 'l': 2, \
'm': 1, 'n': 1, 'o': 1, 't': 1, 'C': 1, 'D': 1, 'I': 1, 'S': 1}
    >>> an_counter_2.add_items("why")
    >>> an_counter_2.get_all_counts()
    {'0': 1, '2': 1, 'a': 2, 'e': 1, 'g': 1, 'h': 2, 'i': 1, 'k': 1, 'l': 2, \
'm': 1, 'n': 1, 'o': 1, 't': 1, 'w': 1, 'y': 1, 'C': 1, 'D': 1, 'I': 1, 'S': 1}
    >>> an_counter_2.add_items("@2")
    >>> an_counter_2.get_count("2")
    2
    >>> an_counter_2.size()
    23
    >>> an_counter_2.get_all_counts()
    {'0': 1, '2': 2, 'a': 2, 'e': 1, 'g': 1, 'h': 2, 'i': 1, 'k': 1, 'l': 2, \
'm': 1, 'n': 1, 'o': 1, 't': 1, 'w': 1, 'y': 1, 'C': 1, 'D': 1, 'I': 1, 'S': 1}

    """
    return


class Counter:
    """
    # TODO: Add class description #
    Class that counts the number of occurences of characters.
    """

    def __init__(self):
        """
        # TODO: Add method description #
        A constructor that builds the counter and keeps track of the counter
        values and items.
        """
        # YOUR CODE GOES HERE #
        self.nelems = 0
        self.counts = {}

    def size(self):
        """
        # TODO: Add method description #
        A function that returns the size or the total number of elements
        counted.
        """
        # YOUR CODE GOES HERE #
        return self.nelems

    def get_count(self, item):
        """
        # TODO: Add method description #
        A function that gets the number of occurences of item.
        """
        # YOUR CODE GOES HERE #
        try:
            return self.counts[item]
        except KeyError:
            return 0

    def get_all_counts(self):
        """
        # TODO: Add method description #
        A function that returns the dictionary of all the items and counts.
        """
        # YOUR CODE GOES HERE #
        return self.counts

    def add_items(self, items):
        """
        # TODO: Add method description #
        A function that adds items to the counter dictionary.
        """
        # YOUR CODE GOES HERE #
        for k in items:
            if k in self.counts.keys():
                self.counts[k] += 1
                self.nelems += 1
            else:
                self.counts[k] = 1
                self.nelems += 1


class AlphanumericCounter(Counter):
    """
    # TODO: Add class description #
    Class that counts the number of occurences of alphanumerical characters.
    """

    def __init__(self):
        """
        # TODO: Add method description #
        A constructor that builds the counter as a list and keeps track of the
        total number of elements.
        """
        super().__init__()
        len_counter_list = 62
        self.counts = [0 for i in range(len_counter_list)]

    def get_index(self, item):
        """
        # TODO: Add method description #
        A function that returns the index of item in the counter list.
        """
        # YOUR CODE GOES HERE #
        numeric_idx_diff = 48
        lower_idx_diff = 87
        upper_idx_diff = 29
        if item.isnumeric():
            return ord(item) - numeric_idx_diff
        if item.islower():
            return ord(item) - lower_idx_diff
        if item.isupper():
            return ord(item) - upper_idx_diff
        return -1

    def get_char(self, idx):
        """
        # TODO: Add method description #
        A function that returns the character using the index from the counter
        list.
        """
        # YOUR CODE GOES HERE #
        numeric_idx_diff = 48
        lower_idx_diff = 87
        upper_idx_diff = 29
        counter_idx_bound_1 = 10
        counter_idx_bound_2 = 36
        if idx < counter_idx_bound_1:
            return chr(idx + numeric_idx_diff)
        if (idx >= counter_idx_bound_1) & (idx < counter_idx_bound_2):
            return chr(idx + lower_idx_diff)
        if idx >= counter_idx_bound_2:
            return chr(idx + upper_idx_diff)

    def get_count(self, item):
        """
        # TODO: Add method description #
        A function that returns the counts of item.
        """
        # YOUR CODE GOES HERE #
        idx = self.get_index(item)
        if idx != -1:
            return self.counts[idx]
        return 0

    def get_all_counts(self):
        """
        # TODO: Add method description #
        A function that return a dictionary of all the alphanumeric characters
        and their corresponding counts.
        """
        # YOUR CODE GOES HERE #
        return {
            self.get_char(k): v for k, v in enumerate(self.counts) if v > 0}

    def add_items(self, items):
        """
        # TODO: Add method description #
        A function that adds characters to count.
        """
        # YOUR CODE GOES HERE #
        for item in items:
            idx = self.get_index(item)
            if idx != -1:
                self.counts[idx] += 1
                self.nelems += 1


# Question 4 (Optional Practice Question)
def compute_max_string(base, pattern):
    """
    # TODO: Add method description and at least 3 new doctests #
    >>> compute_max_string("jumpsjump", "jump")
    9
    >>> compute_max_string("hwhwhw", "hwh")
    5
    >>> compute_max_string("frontsdakonsakdna", "front")
    5
    >>> compute_max_string("life", "life")
    4
    """
    # YOUR CODE GOES HERE #
    if len(base) < len(pattern):
        return 0
    if all([base[i] == pattern[i] for i in range(len(pattern))]):
        return len(pattern) + compute_max_string(base[1:], pattern)
    return compute_max_string(base[1:], pattern)


# Question 5 (Extra Credit)
def group_summation(nums, target):
    """
    # TODO: Add method description and at least 3 new doctests #
    A function that returns True if there is a combination of nums that sum up
    to target.
    >>> group_summation([3, 34, 4, 12, 5, 2], 9)
    True
    >>> group_summation([1, 1, 1], 9)
    False
    >>> group_summation([1, 10, 9, 8], 17)
    True

    >>> group_summation([1, 2, 5, 10, 40], 8)
    True
    >>> group_summation([1, 1, 1, 6, 0, 1, 1], 5)
    True
    >>> group_summation([0, 10, 2, 9], 4)
    False
    """
    # YOUR CODE GOES HERE #
    if len(nums) == 0:
        return False
    if any([nums[0] + nums[i] == target for i in range(len(nums))]):
        return True
    else:
        return group_summation(nums[1:], target)
