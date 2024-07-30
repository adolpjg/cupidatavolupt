def run_optimizer(node):
    # Check if the node has children
    if node.children:
        # Iterate through the children and run the optimizer recursively
        for child in node.children:
            run_optimizer(child)
        # Run the optimizer on the current node
        # (code for running the optimizer on the current node)
    else:
        # If the node has no children, it is a leaf node and the optimizer can be applied directly
        # (code for running the optimizer on the leaf node)
