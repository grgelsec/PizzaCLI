import click
import sqsquery

#cli takes in 2 orders at a time
#if chef 1 is busy, then try chef 2
#if chef 1 and chef 2 are busy then add a to a queue (FIFO), display count of the queue
    
def print_banner():
    return """
\033[91m  ____  _                \033[0m\033[92m ____  _                 \033[0m
\033[91m |  _ \(_)__________ _   \033[0m\033[92m/ ___|| |__   ___  _ __  \033[0m
\033[91m | |_) | |_  /_  / _` |  \033[0m\033[92m\___ \| '_ \ / _ \| '_ \ \033[0m
\033[97m |  __/| |/ / / / (_| |  \033[0m\033[97m ___) | | | | (_) | |_) |\033[0m
\033[97m |_|   |_/___/___\__,_|  \033[0m\033[97m|____/|_| |_|\___/| .__/ \033[0m
\033[97m                         \033[0m\033[97m                  |_|    \033[0m
    """

@click.command()
def cli():
    click.echo(print_banner())
    if sqsquery.order:
        click.echo(sqsquery.order)

if __name__ == '__main__':
    cli()