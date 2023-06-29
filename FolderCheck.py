from pathlib import Path


#set up paths
data_path = Path("data/")
image_path = Path("imgs/")
dataset_path = Path("dataset/")
rosbag_path = Path("RosBags/")

#function to check if the neccessary folders is in project
def CheckIfNecessaryDirectoryExists():
    if image_path.is_dir():
        if data_path.is_dir():
            if dataset_path.is_dir():
                if rosbag_path.is_dir():
                    return True
                else:
                    print("You're missing RosBags folder!")
                    return False
            else:
                print("You're missing dataset folder!")
                return False
        else:
            print("You're missing data folder!")
            return False
    else:
        print("You're missing imgs folder!")
        return False