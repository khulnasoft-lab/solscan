import abc
from typing import Any, List, Optional, TYPE_CHECKING
from solscan.core.context.context import Context
from solscan.core.expressions.expression import Expression
from solscan.core.variables.variable import Variable
from solscan.utils.utils import unroll

if TYPE_CHECKING:
    from solscan.core.compilation_unit import SolscanCompilationUnit
    from solscan.core.cfg.node import Node


class AbstractOperation(abc.ABC):
    @property
    @abc.abstractmethod
    def read(self):
        """
        Return the list of variables READ
        """
        pass  # pylint: disable=unnecessary-pass

    @property
    @abc.abstractmethod
    def used(self):
        """
        Return the list of variables used
        """
        pass  # pylint: disable=unnecessary-pass


class Operation(Context, AbstractOperation):
    def __init__(self) -> None:
        super().__init__()
        self._node: Optional["Node"] = None
        self._expression: Optional[Expression] = None

    def set_node(self, node: "Node") -> None:
        self._node = node

    @property
    def node(self) -> "Node":
        assert self._node
        return self._node

    @property
    def compilation_unit(self) -> "SolscanCompilationUnit":
        return self.node.compilation_unit

    @property
    def used(self) -> List[Variable]:
        """
        By default used is all the variables read
        """
        return self.read

    # if array inside the parameters
    @staticmethod
    def _unroll(l: List[Any]) -> List[Any]:
        return unroll(l)

    def set_expression(self, expression: Expression) -> None:
        self._expression = expression

    @property
    def expression(self) -> Optional[Expression]:
        return self._expression
