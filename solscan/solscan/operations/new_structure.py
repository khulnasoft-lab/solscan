from typing import List, Union

from solscan.slithir.operations.call import Call
from solscan.slithir.operations.lvalue import OperationWithLValue

from solscan.slithir.utils.utils import is_valid_lvalue

from solscan.core.declarations.structure import Structure
from solscan.core.declarations.structure_contract import StructureContract
from solscan.slithir.variables.constant import Constant
from solscan.slithir.variables.temporary import TemporaryVariable
from solscan.slithir.variables.temporary_ssa import TemporaryVariableSSA


class NewStructure(Call, OperationWithLValue):
    def __init__(
        self,
        structure: StructureContract,
        lvalue: Union[TemporaryVariableSSA, TemporaryVariable],
    ) -> None:
        super().__init__()
        assert isinstance(structure, Structure)
        assert is_valid_lvalue(lvalue)
        self._structure = structure
        # todo create analyze to add the contract instance
        self._lvalue = lvalue

    @property
    def read(self) -> List[Union[TemporaryVariableSSA, TemporaryVariable, Constant]]:
        return self._unroll(self.arguments)

    @property
    def structure(self) -> StructureContract:
        return self._structure

    @property
    def structure_name(self):
        return self.structure.name

    def __str__(self):
        args = [str(a) for a in self.arguments]
        lvalue = self.lvalue
        return f"{lvalue}({lvalue.type}) = new {self.structure_name}({','.join(args)})"
