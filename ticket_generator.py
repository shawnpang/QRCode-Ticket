import os
from config import (
    qr_code_image_size,
    available_ticket_info_file,
    ticket_images_folder
)
import pyqrcode
import datetime





def generate_tickets(num_of_tickets):
    """
    generate a specified number of tickets
    :param num: number of tickets
    :return:
    """
    currentDT = datetime.datetime.now()
    sub_folder_name = str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+"/"
    folder_name = ticket_images_folder + sub_folder_name
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    for i in range(0,num_of_tickets):
        hash_value = _generate_each_ticket(folder_name,i+1)
        _save_ticket_info(hash_value)







def _generate_each_ticket(folder_name,image_order):
    currentDT = datetime.datetime.now()
    hash_value = str(currentDT.__hash__())
    qr_ticket = pyqrcode.create(hash_value)


    file_name = folder_name + str(image_order) + ".png"
    print(file_name)
    qr_ticket.png(file_name, scale=qr_code_image_size)

    return hash_value


def _save_ticket_info(hash_value):
    with open(available_ticket_info_file, "a") as file:
        file.write(hash_value)
        file.write("\n")


def init():
    if not os.path.exists(ticket_images_folder):
        os.mkdir(ticket_images_folder)
    pass


init()