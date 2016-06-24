# myweb
Python code to use HTTrack to scrape Dal myweb.dal.ca

1. Get the URLs you will be scraping into a .csv file with headers of `url` and `name`. For a few hundred, you can do it in under a couple of minutes after watching [the video here](https://www.linkedin.com/pulse/how-scrape-1000-google-search-result-links-5-minutes-graham-onak). I recommend muting it and playing it at 2x speed. Apply the technique for [a Google search](https://www.google.ca/search?q=site%3Amyweb.dal.ca) of `site:myweb.dal.ca`. 

2. If [HTTrack](https://www.httrack.com/) is installed, and you run `httracker.py`, and your csv file is named appropriately with the two column headers `name` and `url`, it should work via `python httracker.py`.

Here are some advantages of this technique:

* It limits all the files scraped to those that live on a `myweb.dal.ca` server

* It only scrapes directories on `myweb.dal.ca` that are popular enough to be reachable by Google spiders -- that is, linked to by the outside web.

Open questions:

* How great is the online gallery of what I think are [scanned copies of film photographs](http://myweb.dal.ca/waue/Photos/Around%20Here.html) of the maritimes by Professor Emeritus of Chemistry, [Walter A. Aue](http://myweb.dal.ca/waue/Dal/Vign01/Vign.html), from 2000-2001?

* Given that this method preserves the last time/date that a file was modified by the owner, what was the rate and timeline of Web 2.0 techniques diffusion among Dal community members?

The experience of browsing the directory structure of the public face of `myweb.dal.ca` is a bit like walking down the stacks of a library. You run your virtual hands along the spines, stop and flip through a person's stories. Maybe we shouldn't delete this stuff.

Also, the fact that some Chemistry professors used this resource as a way to experiment with technology and create works of public art suggests that maybe this private sandbox webhosting is a good resource to provide to a University community. It's perhaps not suprising that Dr. Aue [was an expert in chromatography](https://scholar.google.ca/scholar?hl=en&q=aue+chromatography).

I'd be happy to tell you at great length why it matters that such a resource be hosted on Canadian soil, ideally within the control of job-secure locally staffed IT people, but that might get too boring.


