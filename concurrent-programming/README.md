# Python Concurrency
# Basic concepts
- threads share the same memory
- processes `don't share memory
	- each process has its own Python Interpreter and Global Interpreter Lock
- Global Interpreter Lock = only one thread can be running at one time
# Threading functions
- join() = blocks main thread until thread finishes like a "wait for me"
- initializing a new thread:
	- t = threading.Thread(target="some function", args= ("one arg", ), daemon=True)
	- args needs to be a tuple
	- daemon makes a thread work without being joined like a "we don't care when you finish"
		- daemon threads will finish when all of the non-daemon threads from the same process exit
		- the main thread is always a non-daemon thread
# Some OOP basics
- each class must have an \_\_init\_\_  function
- if a class inherits from other classes, then it should:
```
class SomeClass(#parent classes): # classes it inherits from
	def __init__(self, #parameters/attributes):
		self.parameter = #parameter
		super().__init__() # to also initialize parent 
```
- after this, you can use self keyword with functionality from parent classes
# Threading classes
- the worker classes for different threads will inherit from the threading.Thread class
- in the \_\_init\_\_ function,  after initializing the parent classes, self.start() should be called
- start() actually calls a run() function (which is defined in the Thread class)
	- when we did t = threading.Thread(target=function, args=(value, )) and then t.start()
	- Thread.run() would internally call self.function(value)
- so, when we use a threading class, we override ourselves the run() function and call from there the target function 
	- basically what we want the thread to do
# Locking and race conditions
- locks
	- loc = threading.Lock()
	- lock.release()
	- lock.acquire( )
	- to not need to always acquire and release, we can:
		- with lock: and everything in that indent is safe
# Multiprocessing
- can be more efficient than threading for CPU-bound tasks because each process has its own Python interpreter (no GIL), allowing true parallel execution across available cores
- generally more suited for splitting our workload over multiple different segments
	- not doing same thing over all processes
## Multiprocessing pooling
```
with Pool(2) as mp_pool:
	result = mp_pool.map(target, input_list)
```
- it creates 2 worker processes and distributes workload across them and it puts the result in the same order as in the input_list in the result
- pooling can be done for threads as well using the ThreadPoolExecutor from concurrent.futures
### Multiple args pooling
- we can use functools for importing the partial functions
- if we want to be able to have varying args then we can use the starmap function instead of the pool.map one
# Asynchronous programs
- we only have 1 thread and 1 process running
-  a coroutine:
	- we schedule several asynchronous functions
		- each of them will provide a future
			- that will at some point finish or reach some checkpoint
			- and then we can move to a next step in our coroutine
- we also need an event loop to consume all of this coroutines
- await keyword can be used only inside async def functions
- we can only have one event loop per thread
```
async def async_sleep(): # this is a coroutine
    print('Before sleep')
    await asyncio.sleep(5)
    print('After sleep')
    
async def return_hello():
    return 'Hello'

async def main():
    await async_sleep()
    result = await return_hello()
```
- for the code above I have one main coroutine which calls 2 other coroutines
	- await means in this case: "I'm waiting for a response here but another coroutine can take control until I'm done"
	- because I have only one main event loop, it doesn't have another coroutine to transfer control to while its waiting so currently this is actually a sequential program
- await gives control back to event loop for other coroutines to take it
## Creating tasks
- task = asyncio.create_task(async_sleep())
- creating a task = we schedule this coroutine to be worked on whenever is convenient
```
async def main():

    task = asyncio.create_task(async_sleep()) # this says "work on me whenever is convenient for you"

    await async_sleep() # await gives control back to event loop for other coroutines to take it

    await task # this is another coroutine which can be executed in parallel with the first sleep

    await print_hello()
```
- after sleep is executed, the control is given back to event loop and because we have the task which should be done "whenever convenient"
	- it does it now
	- then returns "finishes" sleep 
	- and only then can do the hello function
## Gathering
- await asyncio.gather(#coroutines)
- this will actually make the coroutines given as parameters work in parallel, after each of them is started, they give back control to event loop so it can continue
## Async vs Threading
- async is usually in one thread & one process
	- USE WHEN building individual tasks (web dev used )
	- single core, single thread
	
- while in threading we create multiple threads in the same process with more overhead
	- USE WHEN building worker-like programs 
	- single core, multiple cores (more overhead)
## Async timeout
```
try:
	await asyncio.gather(asyncio.wait_for(async_sleep(30), 5))
	# will wait for 5 seconds before giving a TimeoutError
except asyncio.TimeoutError:
	print('Timeout error')
```
- we need to be careful because this will also stop or interrupt other coroutines gathered with one that reaches Timeout
### Async for
- **`async for`** = items arrive over time, with async waits in between.