


import asyncio

loop = asyncio.new_event_loop()



Return the running event loop in the current OS thread.

If there is no running event loop a RuntimeError is raised. This function can only be called from a coroutine or a callback.


loop = asyncio.get_event_loop()
loop.run_forever()

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.sleep(3))

from datetime import datetime

def print_now():
     print(datetime.now())

loop.call_soon(print_now)
loop.call_soon(print_now)
loop.run_until_complete(asyncio.sleep(3))



def trampoline(name: str = '') -> None:
     print(name, end=' ')
     print_now()
     loop.call_later(0.5, trampoline, name)

loop.call_soon(trampoline)
loop.call_later(8, loop.stop)
loop.run_forever()

loop.call_soon(trampoline, 'First')
loop.call_soon(trampoline, 'Second')
loop.call_soon(trampoline, 'Third')
loop.call_later(8, loop.stop)
loop.run_forever()



# loop.run_until_complete(future)
#   Run until the future (an instance of Future) has completed.
#
# loop.run_forever()
#   Run the event loop until stop() is called.
#
# loop.stop()
#   Stop the event loop.
#
# loop.is_running()
#   Return True if the event loop is currently running.
#
# loop.is_closed()
#   Return True if the event loop was closed.
#
# loop.close()
#   Close the event loop.


# loop.call_soon(callback, *args, context=None)
#   Schedule the callback callback to be called with args arguments at the
# next iteration of the event loop. This method is not thread-safe.
#
# loop.call_soon_threadsafe(callback, *args, context=None)
#   A thread-safe variant of call_soon(). Must be used to schedule callbacks
# from another thread.


# loop.call_later(delay, callback, *args, context=None)
#   Schedule callback to be called after the given delay number of seconds (
# can be either an int or a float).
#
# loop.call_at(when, callback, *args, context=None)
#   Schedule callback to be called at the given absolute timestamp when (an
# int or a float), using the same time reference as loop.time().
#
# loop.time()
#   Return the current time, as a float value, according to the event loop’s
# internal monotonic clock.
