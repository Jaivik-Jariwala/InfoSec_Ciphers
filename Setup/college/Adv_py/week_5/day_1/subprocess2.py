import subprocess
def run_command(command):
    try:
        result = subprocess.Popen(command,stdout=subprocess.PIPE, srderr=subprocess.PIPE, shell=True, text=True)
        stdout, stderr = result.communicate()
        if result.returncode==0:
            print("command executed successfully ")
            print(stdout)
        else:
            print("command failded")
            print(stderr)
    except Exception as e:
        print("error :" , e)

if __name__ == "__main__":
    run_command('echo hi')