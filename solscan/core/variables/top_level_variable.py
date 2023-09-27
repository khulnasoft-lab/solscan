from typing import Optional, TYPE_CHECKING

from solscan.core.declarations.top_level import TopLevel
from solscan.core.variables.variable import Variable

if TYPE_CHECKING:
    from solscan.core.cfg.node import Node
    from solscan.core.scope.scope import FileScope


class TopLevelVariable(TopLevel, Variable):
    def __init__(self, scope: "FileScope") -> None:
        super().__init__()
        self._node_initialization: Optional["Node"] = None
        self.file_scope = scope

    # endregion
    ###################################################################################
    ###################################################################################
    # region IRs (initialization)
    ###################################################################################
    ###################################################################################

    @property
    def node_initialization(self) -> Optional["Node"]:
        """
        Node for the state variable initalization
        :return:
        """
        return self._node_initialization

    @node_initialization.setter
    def node_initialization(self, node_initialization):
        self._node_initialization = node_initialization

    # endregion
    ###################################################################################
    ###################################################################################
