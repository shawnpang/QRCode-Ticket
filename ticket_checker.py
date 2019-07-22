import os
from config import (available_ticket_info_file, used_ticket_info_file)


available_tickets=[]
used_tickets=[]

def check_in(ticket_hash):
    ticket_validity = _check_if_valid(ticket_hash)
    if ticket_validity == "Valid Ticket":
        _change_ticket_usage(ticket_hash)
    return ticket_validity


def _check_if_valid(ticket_hash):
    print(type(ticket_hash))
    print(ticket_hash)
    try:
        ticket_hash = int(ticket_hash)
    except:
        print("Exception!")
        return "WARNING: Unregistered Ticket"


    if ticket_hash in used_tickets:
        return "WARNING: Used Ticket!"
    elif ticket_hash in available_tickets:
        return "Valid Ticket"
    else:
        return "WARNING: Unregistered Ticket"

def _change_ticket_usage(ticket_hash):
    with open(used_ticket_info_file, "a") as file:
        file.write(ticket_hash)
        file.write("\n")
    used_tickets.append(int(ticket_hash))


def _read_ticket_info():
    if os.path.exists(available_ticket_info_file):
        with open(available_ticket_info_file, "r") as file:
            ticket_hash = file.readline().strip("\n")
            while ticket_hash != "":
                available_tickets.append(int(ticket_hash))
                ticket_hash = file.readline().strip("\n")


    if os.path.exists(used_ticket_info_file):
        with open(used_ticket_info_file, "r") as file:
            ticket_hash = file.readline().strip("\n")
            while ticket_hash != "":
                used_tickets.append(int(ticket_hash))
                ticket_hash = file.readline().strip("\n")



def init():
    _read_ticket_info()
    print(available_tickets)


init()