# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from etherscan import Etherscan
from datetime import datetime
import numpy as np


# Press the green button in the gutter to run the script.


def createNFTInfoListFromTransaction(NFTTransactions: list) -> list:
    NFTInfoList = []
    for transaction in NFTTransactions:
        NFTInfo = {key: value for key, value in transaction.items() if key in ["timeStamp", "tokenName", "tokenID"]}
        NFTInfo["dateTime"] = datetime.fromtimestamp(int(NFTInfo["timeStamp"]))
        NFTInfoList.insert(0, NFTInfo)  # the nft info is sorted according to the time, latest at front

    return NFTInfoList


if __name__ == '__main__':
    ether = Etherscan(api_key="noway")
    # ethPrice: float = ether.get_eth_price()

    accountName: str = "noway"
    accountBalance = int(ether.get_eth_balance(address=accountName)) * 1E-18
    accountNFTTransaction = ether.get_erc721_token_transfer_events_by_address(address=accountName, startblock=0,
                                                                              endblock=100000000,
                                                                              sort="asc")

    print("Account:", accountName)
    print("Balance:", accountBalance, "Ether")
    NFTList = createNFTInfoListFromTransaction(accountNFTTransaction)

    print(NFTList[0:5])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
