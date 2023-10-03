# Define custom exceptions for requirement validation
class OSNotFoundException(Exception):
    pass

class OSSNotSupportedException(Exception):
    pass

class OSVersionNotSupportedException(Exception):
    pass

class PythonVersionNotFoundException(Exception):
    pass

class LibsNotFoundException(Exception):
    pass

class LibsVersionNotMentionedException(Exception):
    pass

def validate_requirements(requirements):
    # Validate the requirements
    if "OS" not in requirements:
        raise OSNotFoundException("OS not found")
    if requirements["OS"] not in ["Windows", "Linux"]:
        raise OSSNotSupportedException("OS not supported")
    if "OS_Version" not in requirements:
        raise OSVersionNotSupportedException("OS version not supported")
    if "Python_Version" not in requirements:
        raise PythonVersionNotFoundException("Python version not found")
    if "Libs" not in requirements:
        raise LibsNotFoundException("Libs not found")
    for lib, version in requirements["Libs"].items():
        if version is None:
            raise LibsVersionNotMentionedException(f"Version not mentioned for {lib}")

def generate_output(requirements):
    # Generate the output content
    output = "Output:\n"
    output += f"OS: {requirements['OS']}\n"
    output += f"OS Version: {requirements['OS_Version']}\n"
    output += f"Python Version: {requirements['Python_Version']}\n"
    output += "Libraries:\n"
    for lib, version in requirements["Libs"].items():
        output += f"{lib}: {version}\n"
    return output

def main():
    try:
        # Read the requirements from req.txt
        with open("/home/jaivikjariwala/Desktop/Advanced_py/week_3/task_!/req.txt", "r") as req_file:
            lines = req_file.readlines()
        
        requirements = {}
        for line in lines:
            key, value = line.strip().split("=")
            if key == "Libs":
                libs = {}
                libs_list = value.split(",")
                for lib in libs_list:
                    lib_name, lib_version = lib.strip().split(":")
                    libs[lib_name] = lib_version
                requirements[key] = libs
            else:
                requirements[key] = value
        
        # Validate and generate output
        validate_requirements(requirements)
        output = generate_output(requirements)
        
        # Write the output to output.txt
        with open("/home/jaivikjariwala/Desktop/Advanced_py/week_3/task_!/output.txt", "w") as output_file:
            output_file.write(output)
        print("Output file generated successfully.")
    except (OSNotFoundException, 
            OSSNotSupportedException, 
            OSVersionNotSupportedException, 
            PythonVersionNotFoundException, 
            LibsNotFoundException, 
            LibsVersionNotMentionedException) as e:
        print(f"Validation Error: {e}")

if __name__ == "__main__":
    main()
