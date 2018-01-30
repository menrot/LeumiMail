# -*- coding: utf-8 -*-
import csv

class Table (list):
    def __init__(self):
        self = [ ] # "list of dicts"
        return

    def populate_Table(self, csv_fp):
        rdr = csv.DictReader(csv_fp)
        self.extend(rdr)
        return

    def query_Table(self, filter=None, sort_keys=None):
        if filter is not None:
            Result = (r for r in self if filter(r))
        if sort_keys is not None:
            Result = sorted(self, key=lambda r:[r[k] for k in sort_keys])
        else:
            Result = list(self)
        return Result

    def lookup_Table(self, **kw):
        for row in self:
            for k,v in kw.iteritems():
                if row[k] != str(v): break
            else:
                return row
        return None

