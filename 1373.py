class TreeNode:
    """Definição para um nó de Árvore Binária."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        # Variável para rastrear a soma máxima global de uma BST válida
        self.max_sum = 0
        
        # Chamamos a função auxiliar que faz o percurso pós-ordem
        self._dfs(root)
        
        return self.max_sum

    def _dfs(self, node: TreeNode) -> tuple:
        # Caso Base: Nó nulo
        if not node:
            return (True, float('inf'), float('-inf'), 0)

        # 1. Recurso Pós-ordem: Visita os filhos
        # As tuplas retornam: (é_válida, min, max, soma)
        left_valid, left_min, left_max, left_sum = self._dfs(node.left)
        right_valid, right_min, right_max, right_sum = self._dfs(node.right)

        # 2. Verificação da Propriedade BST
        is_current_bst = (
            left_valid and right_valid and 
            left_max < node.val < right_min
        )

        if is_current_bst:
            # 3. É uma BST Válida: Calcular a soma e atualizar o máximo global
            current_sum = left_sum + right_sum + node.val
            self.max_sum = max(self.max_sum, current_sum)
            
            # 4. Retorno para o nó pai:
            new_min = min(left_min, node.val)
            new_max = max(right_max, node.val)
            
            return (True, new_min, new_max, current_sum)
        else:
            # 5. Não é uma BST Válida: Retornar valores que forcem o pai a também ser inválido
            return (False, float('-inf'), float('inf'), 0)