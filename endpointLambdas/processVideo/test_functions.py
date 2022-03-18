import pytest
from unittest.mock import Mock, patch
from sponsors_detector.process_text import (get_url_domain,
                                            match_links)

import spacy


@pytest.mark.parametrize("test_sentence, test_links",
                         [
                             ("Check out Storyblocks Video at https://www.storyblocks.com/linustech...", ["https://www.storyblocks.com/linustech"]),
                             ("Use my code 'JESSI' for $10 off your FIRST box at www.fabfitfun.com", ["www.fabfitfun.com"]),
                             ("Use code KELSEYK90 to get $90 off your first five HelloFresh boxes including free shipping on your first box at https://bit.ly/2OgZnRI. ",
                              ["https://bit.ly/2OgZnRI"]),
                             ("Go to https://www.casetify.com/kendall today to get 15% off your new favorite phone case",
                              ["https://www.casetify.com/kendall"]),
                             ("Thanks to http://getquip.com/h3 & http://stitchfix.com/h3 & http://mancrates.com/h3 & http://omahasteaks.com (search h3) for sponsoring us!", ["http://getquip.com/h3", "http://stitchfix.com/h3", "http://mancrates.com/h3", "http://omahasteaks.com"]),
                             ("Go to adamandeve.com and use promo code TAPIN for %50 off nearly any item and free shipping!",
                              ["adamandeve.com"])
                         ])
def test_find_link_in_disclaimer(test_sentence, test_links):
    links = match_links(test_sentence)
    assert len(links) == len(test_links) and links == test_links
