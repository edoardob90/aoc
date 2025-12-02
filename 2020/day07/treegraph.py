from treelib import Tree
import json
import uuid

bags = {
    "gold": {
        "red": 2,
        "blue": 3,
    },
    "red": {
        "orange": 2,
    },
    "blue": {},
    "orange": {
        "yellow": 2,
    },
    "yellow": {
        "green": 3,
        "purple": 2,
        "blue": 1,
    },
    "green": {},
    "purple": {},
}

def build_tree(root_node: str, idx: int = None) -> dict:
    node_tag = f"{root_node}_{idx}" if idx is not None else root_node
    tree = {node_tag: {"children": []}}
    try:
        for child, count in bags[root_node].items():
            for _ in range(count):
                i = str(uuid.uuid4())
                if not bags[child]:
                    # current child has no children
                    # print(f"child '{child}' has no children")
                    tree[node_tag]["children"].append(f"{child}_{i}")
                else:
                    # child is a tree itself
                    # print(f"child '{child}' is a tree itself")
                    tree[node_tag]["children"].append(build_tree(child, i))
    except KeyError:
        raise

    return tree


def count_bags(outer_bag: str) -> int:
    if not bags[outer_bag]:
        print(f"'{outer_bag}' bag contains no other bags")
        return 0
    
    count = 0
    for bag in bags[outer_bag]:
        inner_content = bags[outer_bag][bag]
        print(f"'{outer_bag}' bag contains {inner_content} '{bag}' bags")
        count += inner_content * (1 + count_bags(bag))
    return count


def load_tree(json_tree: dict, depth: int = 0, parent = None) -> None:
    k = tuple(json_tree.keys())[0]
    
    if parent is None:
        tree.create_node(tag=str(k), identifier=str(k)+str(depth))
        parent = tree.get_node(str(k)+str(depth))

    for child in json_tree[k]['children']:    
        if isinstance(child, str):
            child_name = child.split("_")[0]
            tree.create_node(tag=child_name, identifier=child+"_"+str(depth), parent=parent)
        else:
            assert isinstance(child, dict), f"child '{child}' should be a dict"
            child_tag = tuple(child)[0]
            child_name = child_tag.split("_")[0]
            tree.create_node(tag=child_name, identifier=child_tag+"_"+str(depth), parent=parent)
            load_tree(child, depth+1, tree.get_node(child_tag+"_"+str(depth)))


if __name__ == "__main__":
    count = count_bags("gold")
    print(f"\nBag 'gold' must contain {count} other bags\n")

    tree = build_tree("gold")
    # print(tree)
    with open("bags_tree.json", "w") as fp:
        json.dump(tree, fp, ensure_ascii=True, indent=2)

    with open('bags_tree.json', 'r') as fp:
        tree_json = json.load(fp)
    tree = Tree()
    load_tree(tree_json)
    tree.show()
