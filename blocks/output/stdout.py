from output import Output

class StdOut(Output):
    def __init__(self, incoming_blocks: list):
        super().__init__(incoming_blocks=incoming_blocks, destination=print)