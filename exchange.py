"""
Virtual Python Exchange Package

This module contains functions for performing various financial exchange operations,
including currency conversion and bill calculations.

Author: Richard Dubný
Date: 17.09.2023
"""

def exchange_money(budget,exchange_rate):
    """ Fuction that callculates the exchange of money
    :param budget: Budget of money that are going to get exchange
    :param exchange_rate: rate of the exchange office, typicaly a 1.xx number
    :return: return of the division of the budget by exchange rate
    """
    return budget / exchange_rate
def get_change(budget,exchanging_value):
    """ The fuction that returns overleft currency
    :param budget: Budget of money we have for exchanging
    :param exchanging_value: value of the money that is going to get exchanged
    :return: returns the change
    """
    return budget - exchanging_value
def get_value_of_bills(denomination,number_of_bills):
    """ Counts value of bills, simply multiplies value of a single bills by number of the bills
    :param denomination: Value of a single bill
    :param number_of_bills: Number of bill's of the value given
    :return: result of multiplying value by number
    """
    return number_of_bills * denomination
def get_number_of_bills(budget,denomination):
    result = int(budget / denomination)
    return result
def get_leftover_of_bills(budget,denomination):
    """ Gets bill's that left fromm the previous operation
    :param budget: Budget of money we have for exchanging
    :param denomination: Value of a single bill
    :return: Left over bills that won't fit the denomination value
    """
    return budget % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """ This function calculates the maximum value of the new currency after exchange.

    :param budget: Our budget we have for exchanging.
    :param exchange_rate: The rate of exchange (e.g., 1.3, 1.2, etc.).
    :param spread: Spread of the exchange rate as a percentage (e.g., 10 for 10%).
    :param denomination: Value of a single bill.
    :return: The maximum value of the new currency as a whole number.
    """

    actual_exchange_rate = exchange_rate + (exchange_rate * float(spread / 100))

    exchange_process = (budget / actual_exchange_rate) / denomination

    result = int(exchange_process) * denomination

    return result


