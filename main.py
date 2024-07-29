import click
import sqsquery

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

#@click.group()
#def cli():
#    pass

#@click.command()
#def start():
#    click.echo(print_banner())
#    click.echo("Welcome to George's Pizza Shop!")

@click.command()
#calls get_orders form sqsquery and forms a order list
def orders():
    customer_Orders = []
    for x in range(3):
        print(f"Getting order {x}")
        order = sqsquery.get_order(5)
        customer_Orders.append(order)
    return print(customer_Orders)


#test
if __name__ == '__main__':
    orders()
