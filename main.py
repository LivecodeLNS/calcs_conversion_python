from milc import cli
from email.policy import default
from def_texts import TextStylist
from conversor.calculation import Calculation
from milc import set_metadata
set_metadata(version='v-0.1.0', author='Lautaro Schnaider')


@cli.argument('-ic', '--initial-calculation', type=str, action='store', default="((3 * 4) + 5 ^ 6 - 7) / 8", required=False, help='To specify the calculation you will convert.')
@cli.argument('-tn', '--target-notation', type=int, action='store', default=3, required=False, help='To specify the notation you want to obtain. Available notations: 1 (prefix), 2 (infix), 3 (postfix).')
@cli.entrypoint('Perform conversion and show result.')
def main(cli):
    try:
        clcltn: Calculation = Calculation(
            cli.args.initial_calculation, cli.args.target_notation
        )
        clcltn.convert()
        sum_stat: dict = clcltn.state
        del clcltn
        stylist: TextStylist = TextStylist(
            cli.echo, sum_stat['len_initial_calculation']
        )
        stylist.line_open()
        stylist.title('¡Welcome to the conversor!')
        stylist.info(
            f'The initial notation is:    {sum_stat['initial_notation']:7}'
        )
        stylist.info(
            f'The target notation is:    {sum_stat['target_notation']:7}'
        )
        stylist.title('INITIAL CALCULATION')
        stylist.calc(sum_stat['initial_calculation'])
        stylist.title('TARGET CALCULATION RESULT:')
        stylist.calc(sum_stat['target_calculation'])
        stylist.line_close()
    except ValueError as error_msg:
        stylist: TextStylist = TextStylist(cli.echo, len(error_msg.args[0])+1)
        stylist.error_line_open()
        stylist.error_title('¡ERROR!')
        stylist.error_info('Please review the input data.')
        stylist.error_info(error_msg.args[0])
        stylist.error_line_close()


if __name__ == '__main__':
    cli()
