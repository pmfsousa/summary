"""
Wrapper for `requests`.
"""
import config, logging, requests
logger = logging.getLogger(__name__)

requests.packages.urllib3.disable_warnings()

def get(url, **kwargs):
    """
    Wrapper for `request.get` function to set params.
    """
    headers = kwargs.get('headers', {})
    headers['User-Agent'] = config.USER_AGENT # overwrite
    kwargs['headers'] = headers

    timeout = kwargs.get('timeout', config.TIMEOUT)
    kwargs['timeout'] = timeout

    kwargs['verify'] = False # no SSLError

    logger.debug("Getting: %s", url)
    return requests.get(url, **kwargs)

def phantomjs_get(url):
    """
    Perform the request via PhantomJS.
    """
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = config.USER_AGENT
    driver = webdriver.PhantomJS(desired_capabilities=dcap, executable_path=config.PHANTOMJS_BIN)
    driver.get(url)
    response = driver.page_source
    driver.quit()
    return response
