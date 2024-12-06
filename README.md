# Import links from OMNIVORE or URL's list to pocket (https://getpocket.com/)

Unfortunately, Omnivore closing out their servers, so I have to find another app for links and reading management. I decide to use Pocket for now. It doesn't have a proper tool to import links from Omnivore or from the link list you have. So here a fast python script for this.

## How to use
1. Export your links from Omnivore or from the list you have.
2. put them into the 'omnivore' folder.
3. Run script, it would generate 3 files:
   - 'links.txt' - list of all links from the 'omnivore' folder
   - 'bookmarks.html' - html file with all links for import to Pocket in the browser bookmark format
   - 'links.html' - html file with all links for import to Pocket in the instapaper format
4. Import 'bookmarks.html' or 'links.html' to Pocket based on your preference.
   - for 'bookmark' format - https://getpocket.com/import/browser/
   - for 'instapaper' format - https://getpocket.com/import/instapaper/