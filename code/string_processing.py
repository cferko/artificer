import codecs
BLOCKSIZE = 1048576 # or some other, desired size in bytes

my_replace_dict = {
                    'Eberron':'Estium',
                    'Dragonmarked':'Eldermarked',
                    'dragonmarked':'eldermarked',
                    ' dragon ' : ' Vestige ',
                    ' Dragons ' : ' Vestiges ',
                    ' dragons ': ' Vestiges ',
                    'dragonshards':'eldershards',
                    'Khorvaire':'Caeros',
                    'Treaty of Thronehold': 'Treaty of Starhaven',
                    'gnomes':'men',
                    'elves':'men',
                    'dwarves':'men',
                    'halflings':'men',
                    'eladrin':'men',
                    'draconic prophecy':'elder prophecy',
                    'Draconic prophecy':'elder prophecy',
                    'warforged':'Forgeling',
                    'Warforged':'Forgeling',
                    'Lightning Rail':'Zephyr',
                    'kalashtar':'Nantangil',
                    'Kalashat':'Nantangil',
                    'Dal Quor': 'Nan',
                    'Quori' : "Nan'fya",
                    'quori' : "Nan'fya",
                    "Khyber" : "Droam",
                    "Droam" : 'Belmead',
                    "Cannith" : "Cadon",
                    "Deneith": "Donric",
                    "Ghallanda":"Ghammara",
                    "Jorasco":"Jeordo",
                    "Kundarak":"Kjaldar",
                    "Lyrandar":"Larenthil",
                    "Medani":"Micaeli",
                    "Orien":"Oraite",
                    "Phiarlan":"Phaelanmry",
                    "Sivis":"Saryn",
                    "Vadalis":"Vernalis",
                    'Sharn': "Pran",}
                    
my_files = [f for f in os.listdir("../corpus/") if "converted" not in f]

for f in my_files:
    my_in_path = "../corpus/"+f
    my_out_path = "../corpus/converted_"+f
    with codecs.open(my_in_path, "r", "mbcs") as sourceFile:
        with codecs.open(my_out_path, "w", "utf-8") as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                for key in my_replace_dict.keys():
                    contents = contents.replace(key, my_replace_dict[key])
                if not contents:
                    break
                targetFile.write(contents)