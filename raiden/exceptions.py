# -*- coding: utf-8 -*-
from raiden.utils import pex


class RaidenError(Exception):
    """ Base exception, used to catch all raiden related exceptions. """
    pass


# Exceptions raised due to programming errors

class HashLengthNot32(RaidenError):
    """ Raised if the length of the provided element is not 32 bytes in length,
    a keccak hash is required to include the element in the merkle tree.
    """
    pass


# Exceptions raised due to user interaction (the user may be another software)


class InsufficientFunds(RaidenError):
    """ Raised when provided account doesn't have token funds to complete the
    requested deposit.

    Used when a *user* tries to deposit a given amount of token in a channel,
    but his account doesn't have enough funds to pay for the deposit.
    """
    pass


class InvalidAddress(RaidenError):
    """ Raised when the user provided value is not a valid address. """
    pass


class InvalidAmount(RaidenError):
    """ Raised when the user provided value is not a integer and cannot be used
    to defined a transfer value.
    """
    pass


class NoPathError(RaidenError):
    """ Raised when there is no path to the requested target address in the
    payment network.

    This exception is raised if there is not a single path in the network to
    reach the target, it's not used if there is a path but the transfre failed
    because of the lack of capacity or network problems.
    """
    pass


# TODO: Use more descriptive exceptions than this
class InvalidState(RaidenError):
    """ Raised when the user requested action cannot be done due to the current
    state of the channel.
    """
    pass


class TransferWhenClosed(RaidenError):
    """ Raised when a user tries to request a transfer is a closed channel. """
    pass


class UnknownAddress(RaidenError):
    """ Raised when the user provided address is valid but is not from a known
    node. """
    pass


# Exceptions raised due to protocol errors (this includes messages received
# from a bizantine node)


class InsufficientBalance(RaidenError):
    """ Raised when the netting channel doesn't enough available capacity to
    pay for the transfer.

    Used for the validation of an *incoming* messages.
    """
    pass


class InvalidLocksRoot(RaidenError):
    """ Raised when the received message has an invalid locksroot.

    Used to reject a message when a pending lock is missing from the locksroot,
    otherwise if the message is accepted there is a pontential loss of token.
    """
    def __init__(self, expected_locksroot, got_locksroot):
        msg = 'Locksroot mismatch. Expected {} but got {}'.format(
            pex(expected_locksroot),
            pex(got_locksroot),
        )

        super(InvalidLocksRoot, self).__init__(msg)


class InvalidNonce(RaidenError):
    """ Raised when the received messages has an invalid value for the nonce.

    The nonce field must change incrementally.
    """
    pass


class TransferUnwanted(RaidenError):
    """ Raised when the node is not receiving new transfers. """
    pass


class UnknownTokenAddress(RaidenError):
    def __init__(self, address):
        super(UnknownTokenAddress, self).__init__(
            'Message with unknown token address {} received'.format(pex(address))
        )

        self.address = address


class STUNUnavailableException(RaidenError):
    pass
