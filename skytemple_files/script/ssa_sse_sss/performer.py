#  Copyright 2020 Parakoopa
#
#  This file is part of SkyTemple.
#
#  SkyTemple is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SkyTemple is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SkyTemple.  If not, see <https://www.gnu.org/licenses/>.
from skytemple_files.script.ssa_sse_sss.position import SsaPosition


class SsaPerformer:
    def __init__(self, type, unk4, unk6, pos: SsaPosition, unk10, unk12):
        # TODO: This is an enum: An enum value from 0 to 5 that dictates what entity will be picked to be this performer.
        self.type = type
        self.unk4 = unk4
        self.unk6 = unk6
        self.pos = pos
        self.unk10 = unk10
        self.unk12 = unk12

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return f"SsaPerformer<{str({k: v for k, v in self.__dict__.items() if v is not None})}>"