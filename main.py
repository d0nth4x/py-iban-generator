config = {
    'nr_oddzialu': 12345678,
    'id_posiadacza': 1234,
    'start': 1,
    'stop': 3000,
}


class Iban:
    def __init__(self, nr_oddzialu, id_posiadacza):
        self.oddzial = nr_oddzialu
        self.posiadacz = id_posiadacza

    def count(self, account_id):
        result = str(self.oddzial) + str(self.posiadacz)
        result += str(account_id).rjust(16 - len(str(self.posiadacz)), '0') + '252100'    # '252100' = ASCII(PL00)

        nn = int(result) % 97
        cc = str(98 - nn).rjust(2, '0')

        retval = cc + str(self.oddzial) + str(self.posiadacz)
        retval += str(account_id).rjust(16 - len(str(self.posiadacz)), '0')

        return retval

if __name__ == '__main__':
    iban = Iban(config['nr_oddzialu'], config['id_posiadacza'])

    for x in range(config['start'], config['stop']+1):
        print(iban.count(x))
