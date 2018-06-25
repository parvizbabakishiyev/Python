#!/usr/bin/python
import subprocess
import re


# accepts stdout as parameter returns
def get_list_of_stats(stdo):
    full_output = str(out)
    mem_output = re.search('Mem:(.+)-/+', full_output)
    mem_result = mem_output.group(1)
    swap_output = re.search('Swap:(.+)', full_output)
    swap_result = swap_output.group(1)
    mem_list = mem_result.lstrip()
    mem_list = mem_list[:-3]
    swap_list = swap_result.lstrip()
    swap_list = swap_list[:-3]

    return mem_list.split(), swap_list.split()


p = subprocess.Popen('free -m', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

(out, err) = p.communicate()

mem, swap = get_list_of_stats(out)

mem_perc = round(100*int(mem[1]) / int(mem[0]), 2)
swap_perc = round(100*int(swap[1]) / int(swap[0]), 2)

print('Memory Usage: ' + str(mem_perc) + '%' + ' | Total: ' + mem[0] + ' | Used: ' + mem[1] + ' | Free: ' + mem[2])
print('Swap Usage:   ' + str(swap_perc) + '%' + ' | Total: ' + swap[0] + ' | Used: ' + swap[1] + ' | Free: ' + swap[2])