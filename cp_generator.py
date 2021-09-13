# read in a file of genomne name and version
# TODO: make it work for original `UnrestrictedGenomes.html`
with open('genomeList.txt','r') as f:
    raw = f.readlines()
path_list = []
cmd_list = []

# prepare the path and command
# TODO: cp the files to a more structured directory system
for line in raw:
    line = line.strip('\n')
    org = line.split("\t")[0].strip()
    version = line.split("\t")[1].strip()
    path = f"./PhytozomeV13/{org}/{version}/annotation/{org}*{version}.protein.fa.gz"
    cmd = f"cp {path} ./phytoPep\n"
    cmd = cmd.replace("-","_")
    cmd_list.append(cmd)
print(len(raw))

# save the cmd
with open('cp.cmd','w') as f:
    f.writelines(cmd_list)

# TODO: execute the cmd in script