import re
#this file uses regular expressions to parse a text file and return a list of temperatures and humidities 
def parse_file(filename):
    digit_pattern = re.compile(r"(\d+\.\d+)")
    temperatures= []
    humidities = []
    with open(filename) as input_file:
        for input_line in input_file.read().splitlines():
            results = digit_pattern.findall(input_line)
            temperatures.append(float(results[0]))
            humidities.append(float(results[1]))
        return temperatures, humidities
            
returned_temperatures, returned_humidities = parse_file("experiment_1_data.txt")
print("temperatures=",returned_temperatures)
print("humidities=", returned_humidities)
