import types


def single(seq):
    """Returns the first element in a list, throwing an exception if there is an unexpected number of items"""
    if isinstance(seq, types.GeneratorType):
        seq = list(seq)
    if len(seq) != 1:
        raise UnexpectedLengthError(
            "Unexpected number of items in the list ({})".format(len(seq)))
    return seq[0]


class UnexpectedLengthError(ValueError):
    pass
