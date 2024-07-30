import click
import sqsquery
import time 

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
        'Pizza': 10,
        'Wings': 3,
        'Pasta': 8,
        'Lasagna': 5,
        'Calzone': 12,
        'Cheese Pizza': 7,
        'Pepperoni Pizza': 13,
        'Vodka Pasta': 14,
        'Breadsticks': 6,
        'Pretzel Sticks': 4
    }
    return time_dict.get(order, 0)

@click.group()
def cli():
    pass

@click.command()
def start():
    click.echo(print_banner())
    click.echo("Welcome to George's Pizza Shop!")

@click.command()
#calls get_orders form sqsquery and forms a order list
#could put the timers in the loop so that they are dependent on the timers finishing to pop orders form the array
def cook():
    customer_Orders = []
    for x in range(5):
        print(f"Getting order {x + 1}")
        order = sqsquery.get_order(5)
        customer_Orders.append(order)
    while len(customer_Orders) != 0:
        order_time1 = setTime(customer_Orders[0])
        customer_Orders.pop(0)
        if len(customer_Orders) > 1:
            chefTwo = True
            order_time2 = setTime(customer_Orders[1])
            customer_Orders.pop(1)
        print("Chef one is cooking")
        time.sleep(order_time1)
        if chefTwo:
            time.sleep(order_time2)
            print("Chef two is cooking")
        print("ready to serve")
    print(customer_Orders)
    


cli.add_command(start)
cli.add_command(cook)


if __name__ == '__main__':
    cli()
