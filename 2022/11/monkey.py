"""A Money class"""

@dataclass
class Monkey:
    """A Monkey class"""
    idx: int = None
    items: list = field(default_factory=list)
    mod: int = None
    op: str = None

    @classmethod
    def from_input(cls, desc):
        """
        Create a Monkey from input text according to this formatting:

        Monkey IDX:
            Starting items:
            Operation:
            Test:
                True:
                False:
        """

