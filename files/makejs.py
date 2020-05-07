pyfile = open('testpy.py', 'r', encoding = 'UTF-8')
count = -1
with open('open.js', 'w', encoding = 'UTF-8') as f:
	py = pyfile.readlines()
	cc, c, tab, local = 1, 0, 0, 0
	variables = []
	f.write('"use strict";' + '\n' * 2)
	f.write('''// Thanks for using py-to-js
// I develop this with hearth''' + '\n' * 2)
	for num in py:
		count += 1
		tab = py[count].count('\t')
		# basic concepts
		if '=' in num and not 'print' in num and not '==' in num and not '!=' in num:
			name = num.replace('\n', '')
			let = 'let '
			if name.startswith('\t'):
				let = '\tlet '
				name = name.replace('\t', '')
			if name in variables:
				let = ''
			variables.append(name)
			f.write( let + f"{name}" + ';' + '\n' * 2)
		elif 'if' in num:
			condition = num.replace('\n', '').replace('if', '').replace(':', '')
			if_ = 'if '
			if condition.startswith('\t'):
				condition = condition.replace('\t', '')
				if_ = '\tif '
				cc += 1
			else:
				cc = 1
			f.write( if_ + '(' + f'{condition}' + ' )' + ' {' + '\n')
		elif 'def' in num:
			con = num.replace('\n', '').replace('def', '').replace(':', '')
			def_ = 'function'
			if con.startswith('\t'):
				con = condition.replace('\t', '')
				def_ = '\tfunction'
				cc += 1
			else:
				cc = 1
			f.write( def_  + f'{con}' + ' {' + '\n')
		# basic commands
		elif 'print' in num:
			command = num.replace('\n', '')
			if command.startswith('\t'):
				command = command.replace('\t', '')
			f.write('\t' + f'{ command.replace("print", "console.log")}'+ ';' + '\n')
		try:
			if py[count + 1].count('\t') < tab and py[count + 1] != '\n':
				if local == 0:
					f.write('}' + '\n')
					c += 1
				elif local > 0:
					f.write('}' * local + '\n')
					c += 1 * local
					local = 0
			elif py[count + 1].count('\t') >= tab and py[count + 1].count('\t') != 0 and py[count + 1] != '\n':
				if 'def' in py[count + 1] or 'if' in py[count + 1]:
					local += 1
		except:
			pass
		try:
			if '\t' in py[count] and not '\t' in py[count + 1] and py[count + 1] != '\n':
				f.write('}' * (cc - c) + '\n' * 2)
				c = 0
		except:
			f.write('}' * (cc - c))
			c = 0
print('''Programm has been compiled..
1.def tests
2.add class''')