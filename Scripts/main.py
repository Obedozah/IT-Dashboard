from system_info import gatherSystemInfo

if __name__ == "__main__":
    system_info = gatherSystemInfo.gather_system_info()
    print(system_info)