BOT_NAME = 'scraping_ebay'

SPIDER_MODULES = ['scraping_ebay.spiders']
NEWSPIDER_MODULE = 'scraping_ebay.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scraping_ebay (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# I reduce this to avoid blocking
CONCURRENT_REQUESTS = 3

