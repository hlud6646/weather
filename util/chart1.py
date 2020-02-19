from util.scrapers import bom, smh, wzn
degree_sign = u"\N{DEGREE SIGN}"

def aggregate_temps():
    return [{
    	'name': 'Reporter', 
    	'data': [{'name': 'BOM', 		'y': bom()}, 
    			 {'name': 'SMH', 		'y': smh()}, 
    			 {'name': 'WeatherZone','y': wzn()}]
    	}]

def chart():
	return {
		'chart' : {
			'type': 'column'
		},
		'title' : {
			'text' : 'Current Temperature in Sydney'
		},		
		'xAxis': {
			'categories': ['BOM', 'SMH', 'WeatherZone'],
		},
		'yAxis': {
			'min': 0,
			'title': {
				'text': f'Temp ({degree_sign}C)'
				}
		},
		'series': aggregate_temps()
	}

