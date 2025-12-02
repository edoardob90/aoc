"""
AoC day 7, 2022

Alternative solution with a class
"""
import sys
import pathlib


class Dir:
    """A Dir class"""

    def __init__(self, name):
        self.name = name
        self.children = {}
        self.parent = None

    def add(self, child, content=None) -> None:
        """Add children to Dir"""
        self.children[child] = content

    @property
    def parents(self) -> str:
        """All the parents of this Dir"""
        parents = ""
        current_parent = self.parent
        while current_parent:
            parents = f"{current_parent.name}/{parents}"
            current_parent = current_parent.parent
        return parents

    @property
    def size(self) -> int:
        """Total size of this Dir"""
        _size = 0
        if self.children:
            for child in self.children.values():
                _size += child.size if isinstance(child, Dir) else child
        return _size

    def __repr__(self) -> str:
        return f"Dir({self.children}, parent: '{self.parent.name if self.parent else None}')"


def parse(puzzle_input):
    """Parse input"""
    root = Dir("/")
    current = root
    for line in puzzle_input.splitlines()[1:]:
        if line.startswith("$"):
            if line[2] == "c":
                if not (dest := line[5:]).startswith(".."):
                    new = Dir(dest.strip())
                    new.parent = current
                    current.add(new.name, new)
                    current = new
                else:
                    current = current.parent
        else:
            if not line.startswith("dir"):
                size, fname = line.split()
                current.add(fname.strip(), int(size))
    return root


if __name__ == "__main__":
    for path in sys.argv[1:]:
        root = parse(pathlib.Path(path).read_text().strip())

        print(root.parents)

        def find_sizes(_dir: Dir) -> dict:
            """Find all directories and their sizes"""
            dir_size = {(_dir.parents + _dir.name).replace("//", "/"): _dir.size}
            for child in _dir.children.values():
                if isinstance(child, Dir):
                    dir_size.update(find_sizes(child))
            return dir_size

        # Part 1

        total = 0
        for size in find_sizes(root).values():
            if size <= 100_000:
                total += size

        print(total)
