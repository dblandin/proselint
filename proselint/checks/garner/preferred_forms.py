# -*- coding: utf-8 -*-
"""MAU102: Preferred forms.

---
layout:     post
error_code: MAU102
source:     Garner's Modern American Usage
source_url: http://amzn.to/15wF76r
title:      preferred forms
date:       2014-06-10 12:31:19
categories: writing
---

Points out preferred forms.

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Suggest the preferred forms."""
    err = "MAU102"
    msg = "'{}' is the preferred form."

    preferences = [

        # Obsolete words
        ["imprimatur",        ["imprimature"]],

        # Proper nouns
        ["Halloween",         ["haloween", "hallowe'en"]],
        ["Khrushchev",        ["Khruschev", "Kruschev"]],
        ["Ku Klux Klan",      ["Klu Klux Klan"]],
        ["Pontius Pilate",    ["Pontius Pilot"]],

        # Plurals
        ["sopranos",          ["soprani"]],
        ["hippopotamuses",    ["hippopotami"]],

        # Misc. misspellings
        ["academically",      ["academicly"]],
        ["anilingus",         ["analingus"]],
        ["fluoride",          ["flouride"]],
        ["fluoridation",      ["flouridation"]],
        ["fluorescent",       ["flourescent"]],
        ["gist",              ["jist"]],
        ["glamour",           ["glamor"]],
        ["granddad",          ["grandad"]],
        ["grandpa",           ["granpa"]],
        ["highfalutin",       ["highfaluting", "highfalutin'", "hifalutin"]],
        ["financeable",       ["financable"]],
        ["praying mantis",    ["preying mantis"]],
        ["aren't i",          ["amn't i"]],
        ["aren't i",          ["an't i"]],
        ["spicy",             ["spicey"]],
        ["Hippocratic",       ["hypocratic"]],
        ["hirable",           ["hireable"]],
        ["holistic",          ["wholistic"]],
        ["ideology",          ["idealogy"]],
        ["idiosyncrasy",      ["ideosyncracy"]],
        ["improvise",         ["improvize"]],
        ["incurrence",        ["incurment"]],
        ["inevitability",     ["inevitableness"]],
        ["innovate",          ["inovate"]],
        ["inoculation",       ["innoculation", "inocculation"]],
        ["inundate",          ["innundate"]],
        ["inundated",         ["innundated"]],
        ["inundating",        ["innundating"]],
        ["inundates",         ["innundates"]],
        ["iridescent",        ["irridescent"]],
        ["kaleidoscope",      ["kaleidascope"]],
        ["knickknack",        ["knicknack"]],
        ["cummerbund",        ["kummerbund"]],
        ["lessor",            ["leasor"]],
        ["lessee",            ["leasee"]],
        ["liquefy",           ["liquify"]],
        ["loathsome",         ["loathesome"]],
        ["mademoiselle",      ["madamoiselle"]],
        ["jujitsu",           ["jiujutsu"]],
        ["minuscule",         ["miniscule"]],
        ["mischievous",       ["mischievious"]],
        ["occurred",          ["occured"]],
        ["plantar fasciitis", ["planter fasciitis", "plantar fascitis"]],
        ["pledgeable",        ["pledgable", "pledgeble"]],
        ["portentous",        ["portentuous", "portentious"]],
        ["preestablished",    ["prestablished"]],
        ["preexisting",       ["prexisting"]],
        ["presumptuous",      ["presumptious"]],
        ["remuneration",      ["renumeration"]],
        ["restaurateur",      ["restauranteur"]],
        ["stupefy",           ["stupify"]],
        ["subtly",            ["subtley"]],

        # Hyphenated words
        ["tortfeasor",        ["tort feasor", "tort-feasor"]],
        ["transship",         ["tranship", "trans-ship"]],
        ["transshipped",      ["transhipped", "trans-shipped"]],
        ["transshipping",     ["transhipping", "trans-shipping"]],
        ["long-standing",     ["longstanding"]],
        # ["longtime",         ["long time"]],

        # able vs. ible
        ["addable",           ["addible"]],
        ["adducible",         ["adduceable"]],
        ["impermissible",     ["impermissable"]],
        ["inadmissible",      ["inadmissable"]],
        ["inculcatable",      ["inculcatible"]],

        # er vs. or
        ["abettor",           ["abbeter"]],
        ["acquirer",          ["acquiror"]],
        ["promoter",          ["promotor"]],
        ["reckless",          ["wreckless"]],

        # in vs. un
        ["inadvisable",       ["unadvisable"]],
        ["inalienable",       ["unalienable"]],

        # Misc
        ["musical revue",     ["musical review"]],
        ["shoo-in",           ["shoe-in"]],

        # TODO, entries that are a bit complicated
        # announce
    ]

    return preferred_forms_check(text, preferences, err, msg)
