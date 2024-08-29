
if __name__ == '__main__':
    with open('untitled.gzmat', 'r') as f:
        lines = f.readlines()
    start_matrix = 5

    for i, line in enumerate(lines):
        if 'Variables:' in line:
            end_matrix = i

    variables = {}
    for line in lines[end_matrix+1:]:  # assuming variables start from line 29
        print(line.strip().split('='))
        line_split = line.strip().split('=')
        if len(line_split) == 2 and line_split[0] != '':
            var, value = line_split
            variables[var] = value

    z_matrix_lines = lines[start_matrix:end_matrix]
    counter = 0
    dict_atoms = {}
    z_matrix_lines_converted = []
    for i, line in enumerate(z_matrix_lines, 1):
        counter += 1
        line_split = line.strip().split(' ')
        line_split = [x for x in line_split if x != '']
        print("line split", line_split)

        label = line_split[0]
        new_label = label+str(counter)
        dict_atoms[str(i)] = new_label

        print("dict atoms", dict_atoms)

        if len(line_split) == 7:
            label, ref, dist, ref_ang, ang, ref_dihed, dihed = line_split
            new_line = f'{new_label} {dict_atoms[ref]} {variables[dist]} {
                dict_atoms[ref_ang]} {variables[ang]} {dict_atoms[ref_dihed]} {variables[dihed]}'
        elif len(line_split) == 5:
            label, ref, dist, ref_ang, ang = line_split
            new_line = f'{new_label} {dict_atoms[ref]} {
                variables[dist]} {dict_atoms[ref_ang]} {variables[ang]}'
        elif len(line_split) == 3:
            label, ref, dist = line_split
            print("label, ref, dist:", label, ref, dist)
            print("new_label, dict_atoms[ref], variables[dist]:",
                  new_label, dict_atoms[ref], variables[dist])
            new_line = f'{new_label} {dict_atoms[ref]} {variables[dist]}'
        else:
            label = line_split
            new_line = new_label
        print("new line", new_line)
        z_matrix_lines_converted.append(new_line)
        with open('z_matrix_conv.txt', 'w+') as f:
            f.write('\n'.join(z_matrix_lines_converted))
        print('Converted Z-Matrix saved to: z_matrix_conv.txt')
