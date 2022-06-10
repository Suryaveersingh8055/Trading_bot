import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root
# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("06bc84781f229f536a94bbd8a03ca3eb58fda0d5c1a235e4a89f89eec8a06480",
                            "44e3c89c026dfb6dcc5168d51cb2c7b27824a64e1ad1a0c73a1185ecd12c26bf",
                            testnet=True, futures=True)
    bitmex = BitmexClient("R4SV7ZCl1BJsa3IDgYFs6hU6", "ZP_tCR3rOGXW4fwY7wZQSzUPqic5lwcAP19sJ_einqVM4erU", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
