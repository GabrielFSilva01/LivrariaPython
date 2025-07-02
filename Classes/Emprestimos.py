

from dataclasses import dataclass
@dataclass
class emprestimos:
    codigo: int
    codigo_livro: int
    codigo_pessoa: int
    data_empréstimo: str
    data_devolucao: str