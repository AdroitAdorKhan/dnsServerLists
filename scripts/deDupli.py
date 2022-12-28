import sys, getopt, os

# print header
print("     __    ___            ___ ")
print(" ___/ /__ / _ \__ _____  / (_)")
print("/ _  / -_) // / // / _ \/ / / ")
print("\_,_/\__/____/\_,_/ .__/_/_/  ")
print("                 /_/   v.1.0  ")
print("\n")

# get the script name
scriptName = os.path.basename(sys.argv[0])

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["inputFile=","outputFile="])
   except getopt.GetoptError:
      print (scriptName, '-i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print (scriptName, '-i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--inputFile"):
         inputfile = arg
      elif opt in ("-o", "--outputFile"):
         outputfile = arg
   # whether  input file exists or not 
   if inputfile:
        # print input file name
        print ('[+] Input File:', inputfile)
        # count input file total lines 
        inputFileLines = sum(1 for line in open(inputfile))
        print ('[+] Input Lines:', inputFileLines)
        
        with open(inputfile, "r") as fp:
            lines = fp.readlines()
            lines.sort()
            new_lines = []
            for line in lines:
                #- Strip white spaces
                line = line.strip()
                if line not in new_lines:
                    new_lines.append(line)
        
        if outputfile:
            outputNewfile = outputfile
        else:
            #outputNewfile = "output.txt"
            outputNewfile = f'output-{inputfile}'

        with open(outputNewfile, "w") as fp:
            fp.write("\n".join(new_lines))
            
        # print output file name
        print ('[+] Output File:', outputNewfile)
        # count output file total lines 
        outputFileLines = sum(1 for line in open(outputNewfile))
        print ('[+] Output Lines:', outputFileLines)
        

if __name__ == "__main__":
   main(sys.argv[1:])