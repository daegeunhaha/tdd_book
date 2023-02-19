from const.currency import Currency


class Pair:
    def __init__(self, source: Currency, target: Currency):
        self._source = source
        self._target = target

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pair):
            return NotImplemented
        return (self._source == other._source) and (self._target == other._target)

    def __hash__(self) -> int:
        return 0
