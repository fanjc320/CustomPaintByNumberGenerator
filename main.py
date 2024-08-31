import subprocess
import  generate

arg1 = ".\examples\boy.jpeg"
arg2 = "16"
arg3 = "16"

#generate "-i .\examples\boy.jpeg -c 16 -s 16 -n test"
# Run the called script with arguments
subprocess.run(['python', 'generate.py', arg1, arg2, arg3])