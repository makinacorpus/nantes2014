#!/usr/bin/env python
#-*- coding: utf-8 -*-

from collections import namedtuple
import json
import sys


"""
    Ce fichier convertit les données brutes de bureaux provenant de
    data.nantes.fr en format lisible par le scrit Leaflet dans index.hmtl
candidates = ['DEFRANCE', 'NULS', 'BOUCHET', 'CROUPY', 'GOBET',
              'ROLLAND', 'CHIRON', 'VAN_GOETHEM', 'GARNIER', 'KONGOLO',
              'BRUCKERT']
"""

candidates = ['NULS', 'ROLLAND', 'GARNIER']
OfficeResults = namedtuple(
    'OfficeResult',
    ' ,'.join(candidates))

if __name__ == '__main__':

    if len(sys.argv) != 3:
        msg = 'Usage : {command} <input.json> <output.json>'.format(
            command=sys.argv[0])
        print(msg)
        exit()

    offices = {}
    with open(sys.argv[1], 'r') as json_file:

        reader = json.load(json_file, encoding='utf8')

        for row in reader['data']:
            # Get results for each political list
            results = sorted(
                [{candidate.lower(): float(row[candidate]) * 100. / float(row['VOTANTS'])}
                 for candidate in candidates],
                key=lambda k: k.values(),
                reverse=True)
            bureau = row['BUREAU_DE_VOTE'].split()[0]
            offices[bureau] = results
            pass

    with open(sys.argv[2], 'w') as outfile:
        response_json = json.dump(offices, outfile)
