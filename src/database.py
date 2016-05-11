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
#     create(name)        - create a new database
#     open(name)          - open an existing database
#     close()             - close the open database
#     remove(name)        - remove the database completely
#     revision()->number  - unique revision number of this database (increments on each write)
#   write
#     set(key, value)     - set a key to a value
#     delete(key)         - delete a key
#   read
#     check(key)->flag    - check if a key exists
#     get(key)->value     - get the value associated with a key
#     list()->keys(iter)  - list all keys

# Store - a local cache of values, possibly non-volatile, possibly platform-dependent format
#   lifecycle
#     create(name)        - create a new store
#     open(name)          - open an existing store
#     close()             - close the store
#     remove(name)        - remove any persistent version of the store
#     revision()->number  - unique revision number of this database (increments on each write)
#     lock()              - enable an exclusive lock
#     unlock()            - disable an exclusive lock
#   write
#     set(key, value)     - set a key to a value
#     delete(key)         - delete a key
#   read
#     check(key)->flag    - check if a key exists
#     get(key)->value     - get the value associated with a key
#     list()->keys(iter)  - get all keys

# Protocol - the wire protocol for exchanging updates via some form of transport
#  lifecycle
#    start(topic)         - start a communications session
#    finish()             - finish a communications session
#  write
#    set(key, value)      - set a key to a value
#    delete(key)          - delete a key
#  sync
#    request(from, to)    - request history catchup from other copies, between revisions
#  comms
#    send(msg)            - send a raw encoded message
#    incoming(msg)        - receive a raw encoded message
#  handlers
#    dispatch(msg)        - route a raw encoded message to correct handler
#    do_set(key, value)   - set a key to a value
#    do_delete(key)       - delete a key
#    do_request(from, to) - request history to be sent between two revisions

# END
