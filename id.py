import subprocess
import sys

def get_bundle_id(app_path):
    try:
        # Comando para obter o Bundle ID usando PlistBuddy
        command = f"/usr/libexec/PlistBuddy -c 'Print CFBundleIdentifier' '{app_path}/Contents/Info.plist'"
        result = subprocess.check_output(command, shell=True, universal_newlines=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Erro: {e}"

def get_app_path_from_drag_and_drop():
    try:
        # Verifica se um arquivo foi arrastado e solto no script
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
            if file_path.endswith(".app"):
                return file_path
    except Exception as e:
        print(f"Erro ao obter o caminho do arquivo: {e}")
    return None

if __name__ == "__main__":
    # Verifica se um arquivo foi arrastado e solto no script
    app_path = get_app_path_from_drag_and_drop()
    if app_path:
        bundle_id = get_bundle_id(app_path)
        print("Bundle ID:", bundle_id)
    else:
        print("Arraste e solte o aplicativo no script para obter o Bundle ID.")
