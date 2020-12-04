class Passport:
    """
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    """
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    @property
    def byr(self):
        return self._byr

    @property
    def iyr(self):
        return self._iyr

    @property
    def eyr(self):
        return self._eyr

    @property
    def hgt(self):
        return self._hgt

    @property
    def hcl(self):
        return self._hcl

    @property
    def ecl(self):
        return self._ecl

    @property
    def pid(self):
        return self._pid

    @property
    def cid(self):
        return self._cid

    @byr.setter
    def byr(self, input):
        conditions = [
            len(input) == 4,
            1920 <= int(input) <= 2002
        ]
        valid = all(conditions)
        self._byr = input, valid

    @iyr.setter
    def iyr(self, input):
        conditions = [
            len(input) == 4,
            2010 <= int(input) <= 2020
        ]
        valid = all(conditions)
        self._iyr = input, valid

    @eyr.setter
    def eyr(self, input):
        conditions = [
            len(input) == 4,
            2020 <= int(input) <= 2030
        ]
        valid = all(conditions)
        self._eyr = input, valid

    @hgt.setter
    def hgt(self, input):
        units = input[-2:]
        measurement = input[:-2]
        conditions = [
            units in ['cm', 'in'],
            (150 <= int(measurement) <= 193) 
                if units == 'cm' else 
                (59 <= int(measurement) <= 76)
        ]
        
        valid = all(conditions)
        self._hgt = input, valid

    @hcl.setter
    def hcl(self, input):
        acceptable_characters = 'abcdef0123456789'
        code = input[1:]
        conditions = [
            input[0] == '#',
            len(code) == 6,
            all([char in acceptable_characters for char in code])
        ]
        
        valid = all(conditions)
        self._hcl = input, valid

    @ecl.setter
    def ecl(self, input):
        acceptable_inputs = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        conditions = [input in acceptable_inputs]
        valid = all(conditions)
        self._ecl = input, valid

    @pid.setter
    def pid(self, input):
        conditions = [
            len(input) == 9,
            int(input) > -1
        ]
        valid = all(conditions)
        self._pid = input, valid

    @cid.setter
    def cid(self, input):
        valid = True
        self._cid = input, valid

    @byr.getter
    def byr(self):
        return self.byr[0]

    @iyr.getter
    def iyr(self):
        return self.iyr[0]

    @eyr.getter
    def eyr(self):
        return self.eyr[0]

    @hgt.getter
    def hgt(self):
        return self.hgt[0]

    @hcl.getter
    def hcl(self):
        return self.hcl[0]

    @ecl.getter
    def ecl(self):
        return self.ecl[0]

    @pid.getter
    def pid(self):
        return self.pid[0]

    @cid.getter
    def cid(self):
        return self.cid[0]

    def is_valid(self):
        conditions = [
            self._byr[1],
            self._iyr[1],
            self._eyr[1],
            self._hgt[1],
            self._hcl[1],
            self._ecl[1],
            self._pid[1],
            self._cid[1],
        ]
        return all(conditions)