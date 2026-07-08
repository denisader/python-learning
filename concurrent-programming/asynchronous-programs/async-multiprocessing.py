import asyncio
import multiprocessing

class MultiprocessingAsync(multiprocessing.Process):
    def __init__(self, duration):
        super().__init__()
        self._duration = duration
    
    @staticmethod
    async def async_sleep(duration):
        await asyncio.sleep(duration)
        return duration

    async def consecutive_sleeps(self):
        pending = set()
        for duration in self._duration:
            pending.add(asyncio.create_task(self.async_sleep(duration))) # creates async tasks for each 1s, 2s, etc at once
        
        while len(pending) > 0:
            done, pending = await asyncio.wait(pending, timeout=1)
            for done_task in done:
                print(await done_task)
    
    def run(self):
        asyncio.run(self.consecutive_sleeps())

if __name__ == '__main__':
    durations = []
    for i in range(1, 11):
        durations.append(i)
    
    processes = []
    for i in range(2):
        processes.append(MultiprocessingAsync(durations[i*5:(i+1)*5])) # splits into 2 chunks
    # process 1 will have sleep(1) -> sleep(5) - take 5s
    # process 2 will have sleep(6) -> sleep(10) - take 10s (all parallel)
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
    