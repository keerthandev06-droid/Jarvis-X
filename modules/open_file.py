import os

from modules.file_search import search_files


def open_item(query):
    """
    Search for the best matching item and open it.
    """

    results = search_files(query)

    if not results:
        print("\nNo matching file, folder or application found.\n")
        return

    name, path, item_type = results[0]

    print(f"\nOpening: {name}")

    try:
        os.startfile(path)
    except Exception as e:
        print(f"\nUnable to open:\n{e}\n")