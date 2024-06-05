import subprocess
import sys

def get_bundle_id(app_path):
    try:
        # Command to get the Bundle ID using PlistBuddy
        command = f"/usr/libexec/PlistBuddy -c 'Print CFBundleIdentifier' '{app_path}/Contents/Info.plist'"
        result = subprocess.check_output(command, shell=True, universal_newlines=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def get_app_path_from_drag_and_drop():
    try:
        # Check if a file was dragged and dropped onto the script
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
            if file_path.endswith(".app"):
                return file_path
    except Exception as e:
        print(f"Error getting file path: {e}")
    return None

if __name__ == "__main__":
    # Check if a file was dragged and dropped onto the script
    app_path = get_app_path_from_drag_and_drop()
    if app_path:
        bundle_id = get_bundle_id(app_path)
        print("Bundle ID:", bundle_id)
    else:
        print("Drag and drop the application onto the script to get the Bundle ID.")
