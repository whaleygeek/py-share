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
#     create - create a new database
#     open - open an existing database
#     close - close the open database
#     remove - remove the database completely
#   write
#     set - set a key to a value
#     delete - delete a key
#   read
#     check - check if a key exists
#     get - get the value associated with a key
#     list - list all keys

# Store - a local cache of values
#   lifecycle
#     create - create a new store
#     open - open an existing store
#     close - close the store
#     remove - remove any persistent version of the store
#     lock - enable an exclusive lock
#     unlock - disable an exclusive lock
#   write
#     set - set a key to a value
#     delete - delete a key
#   read
#     check - check if a key exists
#     get - get the value associated with a key
#     list - get all keys

# Protocol - the wire protocol for exchanging updates via some form of transport
#  lifecycle
#    start - start a communications session
#    create - create a new database
#    remove - remove an existing database
#    finish - finish a communications session
#  write
#    set - set a key to a value
#    delete - delete a key
#  sync
#    request - request history catchup from other copies
#  comms
#    send - send a raw encoded message
#    incoming - receive a raw encoded message
#  handlers
#    dispatch - route a raw encoded message to correct handler
#    do_set - set a key to a value
#    do_delete - delete a key
#    do_request - request history to be sent

# END
