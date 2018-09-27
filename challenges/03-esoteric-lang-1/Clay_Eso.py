# By Clay The Arc


def parse(program: dict):
	# to write a program in DictLang your entire script must be nested dictionaries.
	# they work in order of the keys, so for best results, use this on Python languages with insertion ordered dicts
	# unless you hate yourself
	# example code code
	"""
	{ "main" : {
			"args" : {"letter" : "x",
			          "x" : 5 },
			"print" : {"value" : "hello world",
			           "type" : str }
	becomes:
	main(x=5):
		print(hello world)
	main()
	:param program:
	:return:
	"""
	
	
	for FuncName,Methods in program.items():
		args = Methods.pop("args")
		moron_list = []
		for k,v in Methods.items():
			value = v['type'](v['value'])
			moron_list.append(f"{k}({chr(34)} {value} {chr(34)})")
		func_str = ";".join(value for value in moron_list)
		cursed_string = f"lambda {args['letter']}: {func_str}"
		print(cursed_string)
		FuncName = eval(cursed_string)
		FuncName(args[args["letter"]])
	
foo = dict({ "main" : {
			"args" : {"letter" : "x",
			          "x" : 5 },
			"print" : {"value" : "hello world",
			           "type" : str }
						}})
parse(foo)
