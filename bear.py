from os import system

def search(f):

    out_folder = 'finds'
    search_terms = ['be', 'er', 'ea', 'ba', 'ai']

    #for t in search_terms:
    #    f = open(out_folder + '/' + t, 'w+')
    #    f.close()

    targets = []
    for i in range(len(search_terms)):
        targets.append([])

    with open(f, 'r+') as f:
        lines = f.readlines()

        for i in range(0, len(lines)):
            lines[i] = lines[i].strip()
            lines[i] = lines[i].lower()

        for l in lines:
            for i in range(len(search_terms)):
                if search_terms[i] in l:
                    l = l.replace(search_terms[i], search_terms[i].upper())
                    targets[i].append(l + '\n') 

    for i in range(len(search_terms)):
        with open(out_folder + '/' + search_terms[i], 'w+') as f:
            f.writelines(targets[i])
                    

system('rm -rf finds')
system('mkdir finds')
#search("impropernouns.txt")
search("nouns.txt")
