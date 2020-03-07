import Orange
hiv = Orange.data.Table("1625-hiv-input.tab")
tree_classifier = Orange.classification.tree.TreeLearner(hiv)
def tree_size(node):
        if not node:
            return 0
        size = 1
        if node.branch_selector:
            for branch in node.branches:
                size += tree_size(branch)
        return size

def print_tree0(node, level):
    if not node:
        print " "*level + "<null node>"
        return
    if node.branch_selector:
        node_desc = node.branch_selector.class_var.name
        node_cont = node.distribution
        print "\n" + "   "*level + "%s (%s)" % (node_desc, node_cont),
        for i in range(len(node.branches)):
            print "\n" + "   "*level + ": %s" % node.branch_descriptions[i],
            print_tree0(node.branches[i], level+1)
    else:
        node_cont = node.distribution
        major_class = node.node_classifier.default_value
        print "--> %s (%s) " % (major_class, node_cont),

def print_tree(x):
    if isinstance(x, Orange.classification.tree.TreeClassifier):
        print_tree0(x.tree, 0)
    elif isinstance(x, Orange.classification.tree.Node):
        print_tree0(x, 0)
    else:
        raise TypeError, "invalid parameter"

def cut_tree(node, level):
        if node and node.branch_selector:
                if level:
                        for branch in node.branches:
                                cut_tree(branch, level-1)
                else:
                        node.branch_selector = None
                        node.branches = None
                        node.branch_descriptions = None

cut_tree(tree_classifier.tree, 6)
print_tree(tree_classifier)