import click
import sqsquery
import time 
import asyncio
import random

#grab order from sqs and assign to a chef, assign to chef one, if chef one is busy, assign to chef two, if both chefs are busy, add to waitlist 
    
def print_banner():
    return """
\033[91m  ____  _                \033[0m\033[92m ____  _                 \033[0m
\033[91m |  _ \(_)__________ _   \033[0m\033[92m/ ___|| |__   ___  _ __  \033[0m
\033[91m | |_) | |_  /_  / _` |  \033[0m\033[92m\___ \| '_ \ / _ \| '_ \ \033[0m
\033[97m |  __/| |/ / / / (_| |  \033[0m\033[97m ___) | | | | (_) | |_) |\033[0m
\033[97m |_|   |_/___/___\__,_|  \033[0m\033[97m|____/|_| |_|\___/| .__/ \033[0m
\033[97m                         \033[0m\033[97m                  |_|    \033[0m
    """

def setTime(order):
    time_dict = {
        'Pizza': 5,
        'Wings': 3,
        'Pasta': 4,
        'Lasagna': 5,
        'Calzone': 4,
        'Cheese Pizza': 2,
        'Pepperoni Pizza': 3,
        'Vodka Pasta': 1,
        'Breadsticks': 2,
        'Pretzel Sticks': 4
    }
    return time_dict.get(order, 0)

async def cook_order(chefs_name, order):
    cook_time = setTime(order)
    print(f"{chefs_name} is cooking {order} for {cook_time} seconds")
    await asyncio.sleep(cook_time)
    print(f"{chefs_name} finished cooking {order}")

async def chef(name, order_queue):
    while True:
        if order_queue:
            order = order_queue.pop(0)
            await cook_order(name, order)
        else:
            await asyncio.sleep(1)


@click.command()
def start():
    click.echo(print_banner())
    click.echo("Welcome to George's Pizza Shop!")


#calls get_orders form sqsquery and forms a order list
async def cook():
    customer_orders = []
    random_amount = random.randint(1, 5)
    for x in range(random_amount):
        print(f"Getting order {x + 1}")
        order = sqsquery.get_order(random_amount)
        customer_orders.append(order)
    print(f"Orders received: {customer_orders}")
    chef1 = asyncio.create_task(chef("Chef 1", customer_orders))
    chef2 = asyncio.create_task(chef("Chef 2", customer_orders))
    await asyncio.gather(chef1, chef2)
    return print("Closing Shop")
    
            
def run_cook():
    click.echo(print_banner())
    asyncio.run(cook())
        
@click.command()
def cli():
    run_cook()

if __name__ == '__main__':
    cli()
