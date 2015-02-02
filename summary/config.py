"""
Summary config settings.
These can be overwritten after importing `summary` and before using it.
"""

### Package settings ###

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 (KHTML, like Gecko) Chrome/15.0.87'
ENCODING = 'utf-8' # None for autodetect
TIMEOUT = (10, 10) # (connect, read) # None for never

CHUNK_SIZE = 1024 # 1 KB
HTML_MAX_BYTESIZE = 1 * 1048576 # 1 MB

GET_ALL_DATA = False # False for better performance
# MAX_ITEMS = 2 # to choose from

USEFUL_QUERY_KEYS = [
    'v', 's', 'id', 'story_fbid', 'set', 'q', 'cid', 'tbm', 'fbid', 'u', 'p', 'next',
    'article_id', 'articleid', 'a', 'gid', 'mid', 'itemid', 'newsid', 'storyid', 'list',
    'piano_t', 'piano_d',
]
# USELESS_QUERY_KEYS = [
#   'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_hp_ref', 
#   'utm_cid', 'utm_term', 'utm_reader', 'utm_tone', 'utm', 'utm_keyword', 'utm_name', 
#   'refresh', 'ref', 'feature', '_r', 'smid', 'seid', 'ncid', 'awesm', 'url', 'mg', 
#   '_php', '_type', 'source', 'mod', 'partner', 'type', 'share', 'cmp', 'channel',
#   'ei', 'sa', 'buffer_share', 'bih', 'biw', 'list', 'ved', 'srid', 'fsrc', 'referer',
#   'shortlink', 'trk', 'src', 'mt', 'tripIdBase36', 'activityList', 'emc', 'uid',
#   'page', 'uploaded', 'mbid', 'l', '_i_location', 'siteedition', 'ftcamp', 'soc_src',
#   'pagewanted', 'client', 'c', 'rls', 'hs', 'rev', 'spref', 'curator', 'm', 't',
#   'app', 'feature', 'notif_t', 'index', 'g', 'cmpid', 'lang', 'aff', 'ir', 'st',
#   'ana', 'pid', 'sc', 'sns', 'op', 'goback', 'f', 'g', 'r', 'rid', 'a_dgi', 'ocid',
#   'past', 
# ]


### Filters settings ###

# AdblockURLFilter
ADBLOCK_EASYLIST_URL = 'easylist.txt'
    # 'https://easylist-downloads.adblockplus.org/easylist.txt'
ADBLOCK_EXTRALIST_URL = 'extralist.txt' 
    # 'https://dl.dropboxusercontent.com/u/134594/svven/extralist.txt'

# NoImageFilter
IMAGE_MAX_BYTESIZE = 1 * 1048576 # 1 MB

# SizeImageFilter
IMAGE_LIMIT_RATIO = 3 # if js crop center square
IMAGE_MIN_IMGSIZE = (94, 94)
IMAGE_MAX_IMGSIZE = (2064, 2064)

# MonoImageFilter
IMAGE_MONO_RULE = r'((_|\b)(white|blank|black|overlay)(_|\b))'

# Websites which require headless Javascript handling, e.g. via Selenium and PhantomJS
JS_WEBSITES = ["readwrite.com", "html5-ninja.com", "rally.org", "googleandyourbusiness.blogspot.co.uk"]
PHANTOMJS_BIN = "/usr/local/bin/phantomJs"
PHANTOMJS_USERAGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)

