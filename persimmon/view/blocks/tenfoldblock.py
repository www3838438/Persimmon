from persimmon.view.util import EmptyContent, CircularButton
from persimmon.view.blocks import Block

from kivy.lang import Builder
from kivy.properties import ObjectProperty


Builder.load_file('view/blocks/tenfoldblock.kv')

class TenFoldBlock(Block):
    in_1 = ObjectProperty()
    out_1 = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pins.append(self.in_1)
        self.pins.append(self.out_1)
