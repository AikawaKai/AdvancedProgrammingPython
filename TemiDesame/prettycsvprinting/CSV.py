def max_len(list_, column):
    return max([len(list_[i][column]) for i in range(0, len(list_))])

def strip_line(list_):
    return [line.strip("\n \"'") for line in list_]

def returnString(lines, header):
    header_width = sum(header) + ((len(header)-1)*3)+4
    line_header = '{:-^{}}'.format('',header_width)
    list_string = [["{:<{}}".format((lines[j][i]), header[i]) for i in range(len(header))] for j in range(len(lines))]
    list_string = ["| "+" | ".join(line)+" |" for line in list_string]
    list_string = [line_header] + [list_string[1]]+[line_header]+list_string[1:]+[line_header]
    return "\n".join(list_string)

def prettyCSV(file):
    file_o = open(file, 'r')
    lines = [strip_line(line.split(";")) for line in file_o]
    file_o.close()
    string = ""
    if len(lines)>0:
        header_len =[max_len(lines, i) for i in range(len(lines[0]))]
        string = returnString(lines, header_len)
    return string
