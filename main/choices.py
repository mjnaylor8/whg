# datasets model field value choices

FORMATS = [
    ('delimited', 'Delimited'),
    ('lpf', 'Linked Places (GeoJSON-LDT)'),
    ('direct', 'Inserted to db directly'),
]

DATATYPES = [
    ('place', 'Places'),
    ('anno', 'Annotations'),
    ('source', 'Sources')
]

STATUS = [
    ('format_error', 'Invalid format'),
    ('format_ok', 'Valid format'),
    ('in_database', 'Inserted to database'),
    ('uploaded', 'File uploaded'),
    ('ready', 'Ready for submittal'),
    ('accepted', 'Accepted'),
]

AUTHORITIES = [
    ('tgn','Getty TGN'),
    ('dbp','DBpedia'),
    ('gn','Geonames'),
    ('wd','Wikidata'),
    ('spine','WHG Spine'),
]

AUTHORITY_BASEURI = {
    'align_tgn':'http://vocab.getty.edu/page/tgn/',
    'align_dbp':'http://dbpedia.org/page/',
    'align_gn':'http://www.geonames.org/',
    'align_wd':'https://www.wikidata.org/wiki/'
}

MATCHTYPES = {
    ('exact','exactMatch'),
    ('close','closeMatch'),
    ('related','related'),
}

AREATYPES = {
    ('#areas_codes','Country codes'),
    ('#areas_load','Paste GeoJSON'),
    ('#areas_search','Region/Polity record'),
    ('#areas_drawn','User drawn'),
}
