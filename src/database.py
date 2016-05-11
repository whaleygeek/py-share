# database.py  11/05/2016  D.J.Whale
#
# A simple distributed database abstraction.
#
# This database can be layered on top of any form of transport.
# It responds like a key value store, but can be used to synchronise
# object stores transparently across masses of distributed platforms.

# The key is assumed to be a string.
# The value is any python object
# Probably serialised in json for transfer and storage
# Surfaces again at the other end as a python object.
# passing in json values is probably bad.

# DatabaseError

# Database - the key abstraction
#   lifecycle
#     open
#     close
#     remove
#   write
#     set
#     delete
#   read
#     check
#     get
#     list

# Store - a local cache of values
#   lifecycle
#     open
#     close
#     remove
#     lock
#     unlock
#   write
#     set
#     delete
#   read
#     check
#     get
#     list

# Protocol - the wire protocol for exchanging updates via some form of transport
#  lifecycle
#    start
#    create
#    remove
#    finish
#  write
#    set
#    delete
#  sync
#    request
#  comms
#    send
#    incoming
#  handlers
#    dispatch
#    do_set
#    do_delete
#    do_remove
#    do_request

# END
