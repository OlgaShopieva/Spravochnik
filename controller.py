import do_import
import do_export
import view

def start():
    x = view.get_request()
    if x == "0":
        do_import.upload_data()
    else:
        a = view.find_data()
        do_export.download_data(a)


