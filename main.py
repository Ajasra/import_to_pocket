import json
import os


def get_json_files():
    """
    Get all json files in the 'omnivore' directory
    """
    files = []
    for file in os.listdir('omnivore'):
        if file.endswith('.json'):
            files.append(f'omnivore/{file}')
    return files


def get_json_data(file):
    """
    Get the data from a json file
    """
    with open(file, 'r', encoding="utf-8") as f:
        return json.load(f)

def get_all_entries(data):
    """
    Get all entities from the data
    """
    entries = []
    for d in data:
        for i in range(len(d)):
            entries.append(d[i])
    return entries

def get_all_urls(data):
    """
    Get all urls from the data
    """
    urls = []
    for d in data:
        urls.append(d['url'])
    return urls

def save_all_urls(data):
    """
    Save all urls from the data to a file
    """
    with open('urls.txt', 'w') as f:
        for url in data:
            f.write(url + '\n')

def generate_bookmarks_html(urls, output_file='bookmarks.html'):
    """
    Generate an HTML file with the given URLs in the format of exported bookmarks.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n')
        f.write('<!-- This is an automatically generated file.\n')
        f.write('     It will be read and overwritten.\n')
        f.write('     DO NOT EDIT! -->\n')
        f.write('<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n')
        f.write('<TITLE>Bookmarks</TITLE>\n')
        f.write('<H1>Bookmarks</H1>\n')
        f.write('<DL><p>\n')
        f.write('    <DT><H3 ADD_DATE="0" LAST_MODIFIED="0" PERSONAL_TOOLBAR_FOLDER="true">Bookmarks</H3>\n')
        f.write('    <DL><p>\n')

        for url in urls:
            f.write(f'        <DT><A HREF="{url}" ADD_DATE="0">{url}</A>\n')

        f.write('    </DL><p>\n')
        f.write('</DL><p>\n')

def generate_links_html(urls, output_file='links.html'):
    """
    Generate an HTML file with the given URLs in the format of the provided links.html file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<ol>\n')

        for url in urls:
            f.write(f'<li><a href="{url}"></a>\n')

        f.write('</ol>\n')
        f.write('</body>\n')
        f.write('</html>\n')


files = get_json_files()
data = [get_json_data(f) for f in files]
entries = get_all_entries(data)
urls = get_all_urls(entries)
save_all_urls(urls)
generate_bookmarks_html(urls)
generate_links_html(urls)










