import re

txt = "johann.33es 2812%^@ there $ is ch.icken ($191.11.11nside of my h3art  t"

sub_test_txt_a = "the price is:  $1042.43 dadsfaaf"

sub_test_txt_b = "the price is:  $ten forty three"

found = re.search(r"\B\$\d+((\.|,)\d{2})", txt)
where = found.span()
print(where)
print(txt[where[0]: where[1]])
