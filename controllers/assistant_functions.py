
import sys
sys.path.insert(1, './utils')
import functions

def open_work():
    functions.open_browser_work()
    functions.open_email()
    functions.open_activity_log()
    functions.open_docker()
    functions.open_visual_studio()
    functions.open_spotify()
    return

def good_morning():
    return functions.get_weather()

def searchInInternet(search_term, youtube):
    functions.searchFor(search_term, youtube)
    return