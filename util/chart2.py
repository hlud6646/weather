from util.scrapers import bom, smh, wzn
import pandas as pd
degree_sign = u"\N{DEGREE SIGN}"


def chart():
	df = pd.read_csv('data/temperature.csv')[-12:]
	return {
		'chart' : {
			'type': 'column'
		},
		'title' : {
			'text' : 'Temperature over last 12 hours'
		},
		'yAxis': {
			'title': {
				'text': f'Temp ({degree_sign}C)'
			}
		},
		'xAxis': {
			'title': {
				'text': 'Hours ago'
			}
		},
		'series': [ {'name': 'BOM', 'data': list(df['BOM'])[::-1]}, 
					{'name': 'SMH', 'data': list(df['SMH'])[::-1]}, 
					{'name': 'WZN', 'data': list(df['WZN'])[::-1]}]
	}
