# Find all Links

This (very simple) Python script simply receives all links given a valid URL. A valid url must start with `http://`. For example, although using `www.google.com` in your web browser will work, it won't work for this script.

## Dependencies

In order to succesfully run this script, you'll need to have Python 3 installed. This will not work with Python 2.

In addition, you'll need to have [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) installed, as well as [validators](https://validators.readthedocs.io/en/latest/). You can use [pip](https://pypi.org/project/pip/).

## Examples of valid URLs

* `http://www.google.com`
* `http://google.com`
* `https://www.google.com`
* `https://google.com`