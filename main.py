import sys

from anytree import Node

from dataset_reader import read_dataset
from util import write_tree_on_file, print_tree, read_attributes_type
from decision_tree import decision_tree


def main():
    print("Starting Random Forests Algorithm...")

    # 1st parameter: dataset.csv
    # 2nd parameter: dataset_config.txt
    # 3rd parameter: use sample of attributes when choosing next attribute to split?
    dataset, attributes = read_dataset(sys.argv[1])
    attributes_types = read_attributes_type(sys.argv[2])
    attributes_types = read_attributes_type(sys.argv[2])
    use_sample_attributes = sys.argv[3]

    attributes.remove('class')
    tree = Node("Decision Tree")
    final_decision_tree = decision_tree(
        dataset, attributes, attributes_types, use_sample_attributes, tree)

    print_tree(final_decision_tree)
    write_tree_on_file(final_decision_tree)


if __name__ == "__main__":
    main()
