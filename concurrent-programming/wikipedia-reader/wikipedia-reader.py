import time

from workers.WikiWorker import WikiWorker
from workers.YahooFinanceWorkers import YahooFinanacePriceWorker

def main():
    start_time = time.time()

    wikiWorker = WikiWorker()
    current_workers = []
    for symbol in wikiWorker.get_sp_500_companies():
        yahooFinanacePriceWorker = YahooFinanacePriceWorker(symbol=symbol)
        current_workers.append(yahooFinanacePriceWorker)

    for i in range(len(current_workers)):
        current_workers[i].join()

    print('Extracting time took: ', round(time.time() - start_time, 1))


if __name__ == "__main__":
    main()
