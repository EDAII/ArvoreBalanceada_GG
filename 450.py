# Definição do nó da árvore binária
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _find_min(self, node: TreeNode) -> TreeNode:
        # Função auxiliar para encontrar o menor valor na subárvore (o mais à esquerda)
        current = node
        while current.left is not None:
            current = current.left
        return current

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # Caso base: Se a árvore está vazia
        if not root:
            return root

        # 1. Busca o nó a ser deletado (mantendo a propriedade BST)
        if key < root.val:
            # Se a chave é menor, vá para a subárvore esquerda
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Se a chave é maior, vá para a subárvore direita
            root.right = self.deleteNode(root.right, key)
        
        # 2. O nó a ser deletado FOI ENCONTRADO (key == root.val)
        else:
            # Caso A: Nó é folha ou tem apenas 1 filho
            if not root.left:
                return root.right # Substitui pelo filho direito (pode ser None)
            elif not root.right:
                return root.left  # Substitui pelo filho esquerdo

            # Caso B: O nó tem DOIS FILHOS (O caso mais difícil)
            # a) Encontra o sucessor in-order (o nó de menor valor na subárvore direita)
            successor = self._find_min(root.right)
            
            # b) Copia o valor do sucessor para o nó atual (o que vai ser "deletado")
            root.val = successor.val
            
            # c) Deleta o sucessor (que agora é um nó com no máximo um filho, facilitando a deleção recursiva)
            root.right = self.deleteNode(root.right, successor.val)

        return root