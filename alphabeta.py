def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta):
    
    # Base case: leaf node
    if depth == 0:
        return values[node_index]

    if maximizing_player:
        max_eval = float('-inf')

        for i in range(2):  # 2 children (binary tree)
            eval = alpha_beta(depth - 1, node_index * 2 + i, False, values, alpha,beta)

            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)

            # Pruning condition
            if beta <= alpha:
                break

        return max_eval

    else:
        min_eval = float('inf')

        for i in range(2):
            eval = alpha_beta(depth - 1, node_index * 2 + i,  True, values, alpha,beta)

            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

            # Pruning condition
            if beta <= alpha:
                break

        return min_eval




values = [3, 5, 6, 9, 1, 2, 0, -1]  # Leaf nodes                 ->    values 
depth = 3  # Tree depth

result = alpha_beta(depth, 0, True, values, float('-inf'), float('inf'))

print("Optimal value:", result)
